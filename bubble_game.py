from tkinter import *

import random

class Bubble(object):
    def __init__(self,width,height,name,data, dataPG):
        self.width = width
        self.height = height
        self.imageW = 170
        self.name = name
        self.data = data
        self.dataPG = dataPG
        
        #popping bubbles, made my own images for the process
        #initial image from: https://hplibrary.org/events/bubble-time-cancelled
        self.bubbleType = ['images/large_bubble/bubbleL.png',
                           'images/large_bubble/pop1_bubbleL.png',
                           'images/large_bubble/pop2_bubbleL.png',
                           'images/large_bubble/pop3_bubbleL.png',
                           'images/large_bubble/pop4_bubbleL.png',
                           'images/large_bubble/pop5_bubbleL.png']
                  
        self.addAsked = 0
        self.addCorrect = 0
        self.subAsked = 0
        self.subCorrect = 0
        self.multAsked = 0
        self.multCorrect = 0
        
        self.wrong = []
    
    def __eq__(self, other):
        return isinstance(other, Bubble) and self.name == other.name
    
    def __repr__(self):
        return "%s bubble game data" % self.name 
    
    def __hash__(self):
        return hash(self.name)
    
    def returnName(self):
        return self.name
    
    def scoreForLB(self):
        return (self.data + self.addCorrect + self.subCorrect + self.multCorrect)

    def scorePrintLB(self):
        print(self.data)
        return self.data
        
    def scoreForPG(self):
        if self.dataPG == None or self.dataPG == 0:
            return ((self.addCorrect, self.subCorrect, self.multCorrect), (self.addAsked, self.subAsked, self.multAsked))
        else:
            self.addCorrect += self.dataPG[0][0] 
            self.subCorrect += self.dataPG[0][1] 
            self.multCorrect += self.dataPG[0][2] 
            self.addAsked += self.dataPG[1][0]
            self.subAsked += self.dataPG[1][1]
            self.multAsked += self.dataPG[1][2]
            return ((self.addCorrect, self.subCorrect, self.multCorrect), (self.addAsked, self.subAsked, self.multAsked))
            
    def createBubbles(self):
        margin = 15
        x = random.randint(self.imageW//2, 
                           5 * self.width//8 - margin - self.imageW//2)
        y = 0
        id = 0
        popping = False
        
        if Bubble.askRandom(self): #ask random combinations of questions
            math = random.choice(['add','sub','mult'])
            
        else: #ask questions user has historically struggled with
            if self.wrong != []:
                improve = random.choice(["pastWrong", "topicWrong"])
            else: 
                improve = "topicWrong"
                
            if improve == "pastWrong":
                newBub = random.choice(self.wrong)
                num1, num2, math = newBub
            elif improve == "topicWrong":
                addAvg = self.addCorrect / self.addAsked
                subAvg = self.subCorrect / self.subAsked
                multAvg = self.multCorrect / self.multAsked
                nextQType = min(addAvg, subAvg, multAvg)
                if addAvg == nextQType:
                    math = "add"
                if subAvg == nextQType:
                    math = "sub"
                if multAvg == nextQType:
                    math = "mult"
                    
        (num1, num2) = Bubble.chooseNum(self, math)
        
        if math == "add":
            self.addAsked += 1
        if math == "sub":
            self.subAsked += 1
        if math == "mult":
            self.multAsked += 1
        
        return [x,y,id,popping,num1,num2,math]
        
    def chooseNum(self,math):
        if math == "add":
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
            if num1 + num2 < 10:
                return (num1, num2)
            else:
                return Bubble.chooseNum(self, math)
        elif math == 'sub':
            num1 = random.randint(8,10)
            num2 = random.randint(0,8)
            if 0 <= num1 - num2 < 10:
                return(num1, num2)
            else:
                return Bubble.chooseNum(self, math)
        else: #math == 'mult'
            num1 = random.randint(2,9)
            num2 = random.randint(0,9)
            if 0 <= num1 * num2 < 10:
                return(num1, num2)
            else:
                return Bubble.chooseNum(self, math)
            
    def askRandom(self): 
    #ask at least 5 of each type of question to gt sufficient data on struggles 
        if self.addAsked <= 5:
            return True
        elif self.subAsked <= 5:
            return True
        elif self.multAsked <= 5:
            return True
        return False


    def drawBubbles(self,canvas,bubbleInfo):
        if bubbleInfo != []:
            for bubble in bubbleInfo:
                x,y,id,popping,num1,num2,math = bubble
                imageBubbles = PhotoImage(file=self.bubbleType[id])
                label = Label(image=imageBubbles)
                label.image = imageBubbles
                canvas.create_image(x, y, image = imageBubbles)
                
                if popping == False:
                    if math == 'add':
                        canvas.create_text(x,y,text = "%d + %d" % (num1, num2), 
                        font = ("Comic Sans MS",25,"bold"), fill = "maroon1")
                    elif math == 'sub':
                        canvas.create_text(x,y,text = "%d - %d" % (num1, num2), 
                        font = ("Comic Sans MS",25,"bold"),
                        fill = "deep sky blue")
                    else: #math == 'mult'
                        canvas.create_text(x,y,text = "%d x %d" % (num1, num2), 
                        font = ("Comic Sans MS",25,"bold"), fill = "lime green")
                    
    def expectedAnswer(self, bubbleInfo):
    #returns expected answer in a list
        if bubbleInfo != []:
            for bubble in bubbleInfo:
                x,y,id,popping,num1,num2,math = bubble
                if math == "add":
                    return [num1 + num2]
                elif math == "sub":
                    return [num1 - num2]
                elif math == "mult":
                    return [num1 * num2]
    
    def popping(self, bubbleInfo):
    #bubble pops if correct, increases correct score for that topic by 1
        for bubble in bubbleInfo:
            bubble[3] = True #popping = True
            
            if bubble[6] == "add":
                self.addCorrect += 1
            elif bubble[6] == "sub":
                self.subCorrect += 1
            elif bubble[6] == "mult":
                self.multCorrect += 1
        return bubbleInfo
    
    def notPopping(self, bubbleInfo):
        for bubble in bubbleInfo:
            x,y,id,popping,num1,num2,math = bubble
            self.wrong.append((num1,num2,math)) #store wrong question for future

            if bubble[6] == "add":
                self.addCorrect -= 1
            elif bubble[6] == "sub":
                self.subCorrect -= 1
            elif bubble[6] == "mult":
                self.multCorrect -= 1
                
    def instructions(self,canvas):
        #image from: https://www.vectorstock.com/royalty-free-vector/soap-bubbles-on-white-background-vector-20759635
        imageBubBkg = PhotoImage(file='images/large_bubble/bubble_bkg.png')
        label = Label(image=imageBubBkg)
        label.image = imageBubBkg
        canvas.create_image(self.width//2, self.height//2, image = imageBubBkg)
        canvas.create_rectangle(self.width//4, self.height//4, 
                                3*self.width//4, 3*self.height//4, 
                                fill = "white", width = 3, outline = "sky blue")
        fontsize = 43
        canvas.create_text(self.width//2, self.height//2 - 4.5 * fontsize, 
                           text = "INSTRUCTIONS:", 
                           font = ("Comic Sans MS", 40, "bold"), fill = "steelblue")
        canvas.create_text(self.width//2, self.height//2 - 3 * fontsize, 
                           text = "Every falling bubble", 
                           font = ("Comic Sans MS", 35, "bold"), fill = "pink")
        canvas.create_text(self.width//2, self.height//2 - 2 * fontsize, 
                           text = "has a question inside.",
                           font = ("Comic Sans MS", 35, "bold"), fill = "pink")
        canvas.create_text(self.width//2, self.height//2 - fontsize, 
                           text = "Draw your answer in", 
                           font = ("Comic Sans MS", 35, "bold"), fill = "pink")
        canvas.create_text(self.width//2, self.height//2,
                           text = "the box to the right", 
                           font = ("Comic Sans MS", 35, "bold"), fill = "pink")
        canvas.create_text(self.width//2, self.height//2 + fontsize, 
                           text = "to pop the bubble.", 
                           font = ("Comic Sans MS", 35, "bold"), fill = "pink")
        canvas.create_text(self.width//2, self.height//2 + 2 * fontsize, 
                           text = "Pop as many bubbles",
                           font = ("Comic Sans MS", 35, "bold"), fill = "pink")
        canvas.create_text(self.width//2, self.height//2 + 3 * fontsize, 
                           text = "as you can!!!",
                           font = ("Comic Sans MS", 35, "bold"), fill = "pink")
                           
        #draw back button to exit instructions
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "BACK", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
    
    def drawOnScreen(self,canvas,draw):
        #draw side bar
        canvas.create_line(5 * self.width//8, 0, 5 * self.width//8, self.height,
                           fill = "sky blue")
        
        margin = 15
        #draw screen
        canvas.create_rectangle(5 * self.width//8 + margin, 
                                self.height//2 - 172.5, 
                                self.width - margin, 
                                self.height // 2 + 172.5, 
                                width = 2, outline = "light sky blue", fill = "white")
        
        #draw clear button
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = self.height//2 + 180
        y1 = self.height//2 + 230
        canvas.create_rectangle(x0, y0, x1, 
                            y1, fill = "sky blue", outline = "white")
        canvas.create_text( (x0 + x1) // 2, (y0 + y1) // 2,
                fill = "white",text = "CLEAR",font = ("Comic Sans MS", 20, "bold"))
        
        #draw enter button
        x0 = 5 * self.width//8 + margin
        x1 = 5 * self.width//8 + margin + 120
        y0 = self.height//2 + 180
        y1 = self.height//2 + 230
        canvas.create_rectangle(x0, y0, x1, y1, fill = "pink", outline = "white")
        canvas.create_text( (x0 + x1) // 2, (y0 + y1) // 2,
                fill = "white",text = "ENTER",font = ("Comic Sans MS", 20, "bold"))
                
        #draw instructions button
        canvas.create_oval(self.width - 40, self.height - 40, 
                           self.width - 10, self.height - 10, 
                           fill = "steel blue", outline = "white")
        canvas.create_text(self.width - 25, self.height - 25, 
                           text = "?", fill = "white", 
                           font = ("Comic Sans MS", 10, "bold"))
        
        #draw exit button
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "EXIT", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
        
        #draw on screen
        for coord in range(len(draw)):
            if coord != len(draw) - 1:
                x1, y1, cmd1 = draw[coord]
                x2, y2, cmd2 = draw[coord + 1]
                if cmd1 == "color":
                    canvas.create_line(x1, y1, x2, y2, fill = "black", width = 25)

