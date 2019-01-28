from tkinter import *

import random

class Flashcards(object):
    def __init__(self, width, height, name, data = None):
        self.name = name
        self.width = width
        self.height = height
        self.flashcards = []
        self.questionList = []
        self.data = data
        
        self.addAsked = 0
        self.addCorrect = 0
        self.subAsked = 0
        self.subCorrect = 0
        self.multAsked = 0
        self.multCorrect = 0
        self.divAsked = 0
        self.divCorrect = 0
        
    def __eq__(self, other):
        return isinstance(other, Flashcards) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def createQuestion(self, mathType):
        if mathType != "all":
            math = mathType
        
        elif mathType == "all":
            if Flashcards.askRandom(self):
                math = random.choice(['add','sub','mult','div'])
            else:
                addAvg = self.addCorrect / self.addAsked
                subAvg = self.subCorrect / self.subAsked
                multAvg = self.multCorrect / self.multAsked
                divAvg = self.divCorrect / self.divAsked
                nextQType = min(addAvg, subAvg, multAvg, divAvg)
                if addAvg == nextQType:
                    math = "add"
                if subAvg == nextQType:
                    math = "sub"
                if multAvg == nextQType:
                    math = "mult"
                if divAvg == nextQType:
                    math = "div"
        if math == 'add':
            self.addAsked += 1
            print("add")
            num1 = random.randint(0,20)
            num2 = random.randint(0,20)
        elif math == 'sub':
            print("sub")
            self.subAsked += 1
            num1 = random.randint(15,25)
            num2 = random.randint(0,15)
        elif math == 'div':
            print("div")
            self.divAsked += 1
            (num1, num2) = random.choice([(10,1),(10,2),(10,5),(10,10),(9,1),(9,3),
                                           (9,9),(8,1),(8,2),(8,4),(8,8),(7,1),(7,7),
                                           (6,1), (6,2),(6,3),(6,6),(5,1),(5,5),
                                           (4,1),(4,2),(4,4),(3,1),(3,3),(2,1),(2,2),(1,1)])
        else: #math == 'mult'
            self.multAsked += 1
            num1 = random.randint(0,10)
            num2 = random.randint(0,10)
        return [num1,num2,math]
        
    def askRandom(self):
        if self.addAsked <= 5:
            return True
        elif self.subAsked <= 5:
            return True
        elif self.multAsked <= 5:
            return True
        return False
        
    def chooseTypeQuestion(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height, fill = "white", outline = "white")
        rectangleW = self.width//2
        rectangleH = 70
        x0 = self.width//4
        y0 = self.height//3
        x1 = x0 + rectangleW
        y1 = y0 + rectangleH
        canvas.create_rectangle(x0,y0,x1,y1, fill = "light salmon")
        canvas.create_text((x0 + x1)//2, (y0 + y1)//2, fill = "white", text = "Addition", font = ("Comic Sans MS", 40, "bold"))
        y2 = y1 + rectangleH 
        canvas.create_rectangle(x0,y1,x1,y2, fill = "LightGoldenRod1")
        canvas.create_text((x0 + x1)//2, (y1 + y2)//2, fill = "white", text = "Subtraction", font = ("Comic Sans MS", 40, "bold"))
        y3 = y2 + rectangleH
        canvas.create_rectangle(x0,y2,x1,y3, fill = "pale green")
        canvas.create_text((x0 + x1)//2, (y2 + y3)//2, fill = "white", text = "Multiplication", font = ("Comic Sans MS", 40, "bold"))
        y4 = y3 + rectangleH
        canvas.create_rectangle(x0,y3,x1,y4, fill = "sky blue")
        canvas.create_text((x0 + x1)//2, (y3 + y4)//2, fill = "white", text = "Division", font = ("Comic Sans MS", 40, "bold"))
        y5 = y4 + rectangleH
        canvas.create_rectangle(x0,y4,x1,y5, fill = "plum2")
        canvas.create_text((x0 + x1)//2, (y4 + y5)//2, fill = "white", text = "All", font = ("Comic Sans MS", 40, "bold"))
        
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
    
    def returnName(self):
        return self.name

        
    def dataForAlias(self):
        if self.data == None:
            return ((self.addCorrect, self.subCorrect, self.multCorrect, self.divCorrect), (self.addAsked, self.subAsked, self.multAsked, self.divAsked))
        else:
            self.addCorrect += self.data[0][0] 
            self.subCorrect += self.data[0][1] 
            self.multCorrect += self.data[0][2] 
            self.divCorrect += self.data[0][3]
            self.addAsked += self.data[1][0]
            self.subAsked += self.data[1][1]
            self.multAsked += self.data[1][2]
            self.divAsked += self.data[1][3]
            return ((self.addCorrect, self.subCorrect, self.multCorrect, self.divCorrect), (self.addAsked, self.subAsked, self.multAsked, self.divAsked))
        
    def drawBackground(self,canvas):
        #image from: https://all-free-download.com/free-vector/download/blackboard-books-pencil-vector_294419.html
        imBack = PhotoImage(file = "images/flashcards/chalk.png")
        canvas.create_image(self.width//2, self.height//2, image = imBack)
        label = Label(image=imBack)
        label.image = imBack
        
        #instructions 
    
    def drawQuestion(self,canvas, questionList):
        for questionInfo in questionList:
            num1, num2, math = questionInfo
            if math == "add":
                canvas.create_text(2 * self.width//3 + 55, self.height//4, 
                                   text = "%d" % num1, 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
                canvas.create_text(2 * self.width//3 - 10, self.height//4 + 120, 
                                   text = "+ %d" % num2, 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
                canvas.create_text(2 * self.width//3, self.height//4 + 140, 
                                   text = "___", 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
            if math == "sub":
                canvas.create_text(2 * self.width//3 + 55, self.height//4, 
                                   text = "%d" % num1, 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
                canvas.create_text(2 * self.width//3 - 10, self.height//4 + 120, 
                                   text = "- %d" % num2, 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
                canvas.create_text(2 * self.width//3, self.height//4 + 140, 
                                   text = "___", 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
            if math == "mult":
                canvas.create_text(2 * self.width//3 + 55, self.height//4, 
                                   text = "%d" % num1, 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
                canvas.create_text(2 * self.width//3 - 10, self.height//4 + 120, 
                                   text = "x %d" % num2, 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
                canvas.create_text(2 * self.width//3, self.height//4 + 140, 
                                   text = "___", 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
            if math == "div":
                canvas.create_text(2 * self.width//3 + 55, self.height//4, 
                                   text = "%d" % num1, 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
                canvas.create_text(2 * self.width//3 - 10, self.height//4 + 120, 
                                   text = "÷ %d" % num2, 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
                canvas.create_text(2 * self.width//3, self.height//4 + 140, 
                                   text = "___", 
                                   font = ("Comic Sans MS", 100, "bold"), fill = "white")
                                   
    def drawAnswer(self,canvas,num):
        canvas.create_text(2 * self.width//3 + 55, self.height//4 + 280, 
                           text = num, 
                           font = ("Comic Sans MS", 100, "bold"), fill = "white")
        
    def expectedAnswer(self, questionInfo):
        for question in questionInfo:
            num1, num2, math = question
            if math == "add":
                return num1 + num2
            elif math == "sub":
                return num1 - num2
            elif math == "mult":
                return num1 * num2
            elif math == "div":
                return num1 / num2
    
    def correct(self,correctness, questionInfo):
        for question in questionInfo:
            num1, num2, math = question
            if correctness == True:
                if math == "add":
                    self.addCorrect += 1
                    print(self.addCorrect)
                elif math == "sub":
                    self.subCorrect += 1
                elif math == "mult":
                    self.multCorrect += 1
                elif math == "div":
                    self.divCorrect += 1
            elif correctness == False:
                if math == "add":
                    self.addCorrect -= 1
                elif math == "sub":
                    self.subCorrect -= 1
                elif math == "mult":
                    self.multCorrect -= 1
                elif math == "div":
                    self.divCorrect -= 1
                    
    def correctDraw(self, canvas, correctness):
        if correctness == True:
            canvas.create_text(2 * self.width//3, self.height//4 - 120, 
                                   text = "Good Job!", 
                                   font = ("Comic Sans MS", 80, "bold"), fill = "mint cream")
        elif correctness == False:
            canvas.create_text(2 * self.width//3, self.height//4 - 140, 
                                text = "Try Again!", 
                                font = ("Comic Sans MS", 80, "bold"), fill = "lavender blush")
    
    def screenKeys(self, canvas):
        #instructions
        canvas.create_oval(self.width - 40, self.height - 40, 
                           self.width - 10, self.height - 10, 
                           fill = "dark green")
        canvas.create_text(self.width - 25, self.height - 25, 
                           text = "?", fill = "white", 
                           font = ("Comic Sans MS", 10, "bold"))
                           
        #exit 
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "EXIT", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
        
    def instructions(self, canvas):
        Flashcards.drawBackground(self, canvas)
        
        canvas.create_rectangle(self.width//4, self.height//4, 
                                3*self.width//4, 3*self.height//4, 
                                fill = "white", width = 3, outline = "dark green")
        fontsize = 43
        canvas.create_text(self.width//2, self.height//2 - 4.5 * fontsize, 
                           text = "INSTRUCTIONS:", 
                           font = ("Comic Sans MS", 40, "bold"), fill = "dark green")
        canvas.create_text(self.width//2, self.height//2 - 2 * fontsize, 
                           text = "Type your answer", 
                           font = ("Comic Sans MS", 35, "bold"), fill = "gray79")
        canvas.create_text(self.width//2, self.height//2 - fontsize, 
                           text = "and press enter.",
                           font = ("Comic Sans MS", 35, "bold"), fill = "gray79")
        canvas.create_text(self.width//2, self.height//2, 
                           text = "Keep practicing!", 
                           font = ("Comic Sans MS", 35, "bold"), fill = "gray79")

                           
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