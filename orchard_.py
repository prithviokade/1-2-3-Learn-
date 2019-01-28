
from tkinter import *
import random
import copy

class Orch(object):
    def __init__(self, width, height, land, charPos, treePos):
        self.width = width
        self.height = height
        self.charPos = charPos
        self.land = land
        self.treePos = treePos
    
    def drawLand(self, canvas, scrollX, questions,score):
        canvas.create_rectangle(0, 0, self.land, 2*self.height //3, fill = "azure", outline = "azure")
        canvas.create_rectangle(0, 2*self.height //3, self.land, self.height, fill = "green4", outline = "green4")
        canvas.create_text(3*self.width //4, 100, text = "Chris wants to pick apples \n for 5 of his friends. \n Draw the sum of the \n numbers in each tree \n to pick the apples!", font = ("Comic Sans MS", 20, "bold"), justify = CENTER)
        
        #image from: http://worldartsme.com/apple-basket-clipart.html#gal_post_10444_apple-basket-clipart-1.jpg
        basket = PhotoImage(file = 'images/story/basket.png')
        label = Label(image = basket)
        label.image = basket
        canvas.create_image(self.width - 150, self.height - 150, image = basket)
        canvas.create_text(self.width - 150, self.height - 150, text = str(score),font = ("Comic Sans MS", 30, "bold"), fill = "black")
        
        #https://www.123rf.com/clipart-vector/apple_tree.html?sti=ldtkeeblscxweg93rp|
        tree = PhotoImage(file='images/story/tree.png')
        label = Label(image=tree)
        label.image = tree
        
        for i in range(len(self.treePos)):
            x = self.treePos[i]
            quest = questions[i]
            canvas.create_image(x - (3 * scrollX),2 * self.height //3 - 320//2, image = tree)
            canvas.create_text(x - 3 * scrollX - 95, 2 * self.height //3 - 190,text = str(quest[0]), font = ("Comic Sans MS", 20, "bold"), fill = "black")
            canvas.create_text(x - 3 * scrollX + 95, 2 * self.height //3 - 165,text = str(quest[1]), font = ("Comic Sans MS", 20, "bold"), fill = "black")
            canvas.create_text(x  - 3 * scrollX + 43, 2 * self.height //3 - 232,text = str(quest[2]), font = ("Comic Sans MS", 20, "bold"), fill = "black")
            canvas.create_text(x - 3 * scrollX - 40, 2 * self.height //3 - 150,text = str(quest[3]), font = ("Comic Sans MS", 20, "bold"), fill = "black")
            canvas.create_text(x - 3 * scrollX - 40, 2 * self.height //3 - 258,text = str(quest[4]), font = ("Comic Sans MS", 20, "bold"), fill = "black")
        
        #image from https://www.cybera.com/race-challenge/nascar-flags-outlined/
        fin = PhotoImage(file='images/story/finish.png')
        label = Label(image=fin)
        label.image = fin
        canvas.create_image(2000 - scrollX, 2 * self.height //3 - 50, image = fin)
        canvas.create_text(2000 - scrollX, 2 * self.height //3 - 170, text = "FINISH!", font = ("Comic Sans MS", 20, "bold"))
    
    #initially learned from side scrolling 112 class
    def drawChar(self, canvas, scrollX, walk):
        if walk > 0:
            #image from https://www.youtube.com/watch?v=MtmG9EFmnW8 screenshot
            b = PhotoImage(file='images/story/b%d.png' % walk) 
            label = Label(image=b)
            label.image = b
            canvas.create_image(self.charPos + scrollX, 2*self.height//3 - 70, image = b)
        elif walk < 0:
            bb = PhotoImage(file='images/story/bb%d.png' % (-1 * walk))
            label = Label(image=bb)
            label.image = bb
            canvas.create_image(self.charPos + scrollX, 2*self.height//3 - 70, image = bb)
    
    def drawOnScreen(self, canvas, draw):
        margin = 15
        #draw screen
        canvas.create_rectangle(margin, 
                                self.height//4 - 222.5, 
                                3 * self.width//8 - margin, 
                                self.height // 4 + 122.5, 
                                width = 2, outline = "light sky blue", fill = "white")
        
        #draw on screen
        for coord in range(len(draw)):
            if coord != len(draw) - 1:
                x1, y1, cmd1 = draw[coord]
                x2, y2, cmd2 = draw[coord + 1]
                if cmd1 == "color":
                    canvas.create_line(x1, y1, x2, y2, fill = "black", width = 25)
        
        #draw clear button
        x0 = 3 * self.width//8 - margin + 10
        x1 = 3 * self.width//8 - margin + 130
        y0 = self.height//4 - 222.5
        y1 = self.height//4 - 222.5 + 50
        canvas.create_rectangle(x0, y0, x1, 
                            y1, fill = "sky blue", outline = "white")
        canvas.create_text( (x0 + x1) // 2, (y0 + y1) // 2,
                fill = "white",text = "CLEAR",font = ("Comic Sans MS", 20, "bold"))
        
        #draw enter button
        x0 = 3 * self.width//8 - margin + 10
        x1 = 3 * self.width//8 - margin + 130
        y0 = self.height//4 - 222.5 + 60
        y1 = self.height//4 - 222.5 + 110
        canvas.create_rectangle(x0, y0, x1, y1, fill = "pink", outline = "white")
        canvas.create_text( (x0 + x1) // 2, (y0 + y1) // 2,
                fill = "white",text = "ENTER",font = ("Comic Sans MS", 20, "bold"))
    
    def expectedAnswer(self, question):
        return [sum(question[0])] 
        
    #initially learned from 112 class, backtracking template
    def createQBT(self):
        answers = []
        setA = []
        for i in range(len(self.treePos)):
            options = random.sample(range(-5,10),10)
            a = Orch.createQBTHelp(self, [], answers, setA, options)
            answers.append(a)
            setA.append(set(tuple(a)))
        return answers
        
    def isValid(self, lst, answers, setA, num):
        lst.append(num)
        sCQ = set(tuple(lst))
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] == lst[i+1]:
                return False
        if sCQ in setA:
            return False
        if len(lst) == 5:
            if sum(lst) >= 10 or sum(lst) < 0:
                return False
        return True
    
    def createQBTHelp(self, lst, answers, setA, options):
        if len(lst) >= 5:
            return lst
        for i in range(len(options)):
            num = options[i]
            if Orch.isValid(self, copy.copy(lst), answers, setA, num):
                lst.append(num)
                tmpSolution = Orch.createQBTHelp(self, lst, answers, setA, options[1:])
                if tmpSolution != None:
                    return tmpSolution
                lst.pop()
        return None
        