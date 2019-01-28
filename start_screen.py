from tkinter import *

import random

class Start(object):
    def __init__(self, width, height, name):
        self.name = name
        self.width = width
        self.height = height
        self.rows = 20
        self.cols = 20
        
        #mode centers
        self.flashCent = (3 * self.width//4,self.height//4)
        self.rainCent = (3 * self.width//4 - 100,self.height//2)
        self.storyCent = (3 * self.width//4 + 25, 3 * self.height//4)
        
    def __eq__(self, other):
        return isinstance(other, Start) and self.width == other.width and self.height == other.height and self.name == other.name
     
    def __repr__(self):
        return "%s" % self.name
        
    def __hash__(self):
        return hash(self.name)
    
    def sendInfo(self):
        return (self.name)
    
    def loading(self, canvas, id):
        canvas.create_rectangle(0,0,self.width,self.height, 
                                fill = "sky blue", outline = "sky blue")
        if id == 3: canvas.create_text(self.width//2, self.height//2, 
                    font = ("Comic Sans MS", 35, "bold"), fill = "white", 
                    text = "loading...")
        elif id == 2: canvas.create_text(self.width//2, self.height//2, 
                      font = ("Comic Sans MS", 35, "bold"), fill = "white", 
                      text = "loading..")
        elif id == 1: canvas.create_text(self.width//2, self.height//2, 
                      font = ("Comic Sans MS", 35, "bold"), fill = "white", 
                      text = "loading.")
        elif id == 0: canvas.create_text(self.width//2, self.height//2, 
                      font = ("Comic Sans MS", 35, "bold"), fill = "white", 
                      text = "loading")
    
    def inputName(self, canvas, name, imageCoord):
        #image from: https://illustimage.com/en/?id=2420
        imageApple = PhotoImage(file='images/login/apple.png')
        imageX, imageY = imageCoord
        canvas.create_image(imageX, imageY, image = imageApple)
        label = Label(image=imageApple)
        label.image = imageApple
        
        #image from: https://m.aliexpress.com/item/32389750660.html
        imageWelx = PhotoImage(file='images/login/welcome.png')
        imageX, imageY = imageCoord
        canvas.create_image(imageX, 225 - 140, image = imageWelx)
        label = Label(image=imageWelx)
        label.image = imageWelx
        
        imageLogo = PhotoImage(file='images/login/logo.png')
        canvas.create_image(self.width - 120, self.height - 70, image = imageLogo)
        label = Label(image=imageLogo)
        label.image = imageLogo
        
        x0 = self.width//3
        x1 = 2*self.width//3
        y0 = self.height//2 + 30
        y1 = self.height//2 + 100
        canvas.create_text(((x0+x1)//2), (y0 + y1)//2 - 100, font = ("Comic Sans MS", 40, "bold"), text = "Enter your name here:")
        canvas.create_rectangle (x0, y0, x1, y1, fill = "sky blue")
        self.name = name
        canvas.create_text((x0+x1)//2, (y0 + y1)//2, text = self.name, font = ("Comic Sans MS", 35, "bold"))
    
    #initially learned from 112 notes 
    #(I didn't actually look at the 112 notes, but I know it's similar)
    def getCellBounds(self, col, row):
        colWidth = self.width / self.cols
        rowHeight = self.height / self.rows
        x0 = col * colWidth - 15
        x1 = (col + 1) * colWidth - 15
        y0 = row * rowHeight - 15
        y1 = (row + 1) * rowHeight - 15 
        return (x0, y0, x1, y1) 
        
    def drawBackground(self,canvas):
        for row in range(self.rows + 1):
            for col in range(self.cols + 1):
                (x0, y0, x1, y1) = Start.getCellBounds(self, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, 
                                        outline = "SkyBlue1", width = 2)
        
    
    def drawTitle(self,canvas,image1,image2,image3,learn):
        image1X,image1Y = image1
        image2X,image2Y = image2
        image3X,image3Y = image3
        learnX,learnY = learn
        
        #draws 1 2 3 LEARN
        #images from: https://techflourish.com/categories/cute-number-1-clipart.html
        imageOne = PhotoImage(file='images/title/1.png')
        imageTwo = PhotoImage(file='images/title/2.png')
        imageThree = PhotoImage(file='images/title/3.png')
        #image from: https://www.123rf.com/photo_10192141_illustration-of-kids-posing-with-the-word-learn.html
        imageLearn = PhotoImage(file='images/title/Learn.png')
        canvas.create_image(image1X, image1Y, image = imageOne)
        label = Label(image=imageOne)
        label.image = imageOne
        canvas.create_image(image2X, image2Y, image = imageTwo)
        label = Label(image=imageTwo)
        label.image = imageTwo
        canvas.create_image(image3X, image3Y, image = imageThree)
        label = Label(image=imageThree)
        label.image = imageThree
        canvas.create_image(learnX, learnY, image = imageLearn)
        label = Label(image=imageLearn)
        label.image = imageLearn
        
    def drawBubbleOpt(self, canvas):
        x,y = self.rainCent
        y1 = y + 90
        
        canvas.create_rectangle(x - 165, y - 92, x + 170, y, 
                        fill = "DarkOliveGreen2",width = 3)
        canvas.create_text(((x - 165) + (x + 170)) // 2, (y - 90 + y)//2, text = "Play!", fill = "white", font = ("Comic Sans MS", 25, "bold"))               
        
        canvas.create_rectangle(x - 165, y, x + 170, y1, 
                        fill = "DarkOliveGreen2",width = 3)  
        canvas.create_text(((x - 165) + (x + 170)) // 2, (y + y1) //2, text = "Leaderboard", fill = "white", font = ("Comic Sans MS", 25, "bold")) 
        
        
        
    def drawClickModes(self,canvas):
        #flashcards
        x,y = self.flashCent
        canvas.create_oval(x - 150, y - 80, x + 150, y + 80, 
                        fill = "steelblue", width = 3)
        canvas.create_oval(x - 155, y - 79, x + 155, y + 79, width = 3)
        canvas.create_oval(x - 151, y - 84, x + 151, y + 86, width = 3)
        #canvas.create_oval(x - 97, y - 39, x + 103, y + 41, width = 1)
        canvas.create_text(x,y,text = "Advanced\nFlashcards",fill = "white", justify = CENTER, font = ("Comic Sans MS", 25, "bold"))
        
        #raingame
        x,y = self.rainCent
        canvas.create_oval(x - 159, y - 90, x + 164, y + 90, 
                        fill = "DarkOliveGreen3",width = 3)
        canvas.create_oval(x - 163, y - 87, x + 165, y + 88, width = 3)
        canvas.create_oval(x - 162, y - 91, x + 169, y + 83, width = 3)
        #canvas.create_rectangle(x - 97, y - 37, x + 103, y + 43, width = 2)
        canvas.create_text(x,y,text = "Bubble Burst!",fill = "white",
                            font = ("Comic Sans MS", 25, "bold"))
        
        #story
        x,y = self.storyCent
        canvas.create_oval(x - 140, y - 80, x + 140, y + 80, fill = "orange2",
                        width = 2)
        canvas.create_oval(x - 145, y - 80, x + 141, y + 77, width = 3)
        #canvas.create_oval(x - 93, y - 43, x + 87, y + 37, width = 1)
        canvas.create_oval(x - 139, y - 77, x + 143, y + 83, width = 3)
        canvas.create_text(x,y,text = "Apple Picking!",fill = "white",
                            font = ("Comic Sans MS", 25, "bold"))
        
        #log out
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = 10
        y1 = 60
        
        #username
        canvas.create_text(((x0 - 150) + (x1 - 150)) //2, (y0 + y1) // 2, text = "user: %s" % self.name, 
                           fill = "black", font = ("Comic Sans MS", 15, "bold"))
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "LOG OUT", 
                           fill = "white", font = ("Comic Sans MS", 15, "bold"))
    
        #parent feedback
        margin = 15
        x0 = self.width - margin - 200
        x1 = self.width - margin
        y0 = self.height - 10
        y1 = self.height - 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "sky blue", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "Progress Report", 
                           fill = "white", font = ("Comic Sans MS", 15, "bold"))