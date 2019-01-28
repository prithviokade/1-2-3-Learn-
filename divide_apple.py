
from tkinter import *
import random

    
class AppleDiv(object):
    def __init__(self, width, height, apples):
        self.width = width
        self.height = height
        self.char = 0
        self.apples = apples
        self.correctR = []
        
    def drawApples(self, canvas):
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = self.height - 10
        y1 = self.height - 60 
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "sky blue", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "ENTER", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
        
        #image from: http://diysolarpanelsv.com/apple-clipart-for-silhouette.html
        imageApple = PhotoImage(file='images/story/apple.png')
        label = Label(image=imageApple)
        label.image = imageApple
        space = (self.width - 20) // (self.apples)
        x = (self.width - (self.apples - 1)*space) //2
        
        if self.apples % 3 == 0:
            count = self.apples / 3
            for i in range(self.apples):
                if (i + 1) % count == 0:
                    self.correctR.append((x, 3 * self.height//4 + 100))
                canvas.create_image(x, 3*self.height //4 + 100, image = imageApple)
                x += space
            
            self.char = 3
            canvas.create_text(self.width // 2, self.height//4 - 80, text = "Chris gives some apples to Adam and Patricia \n and Megan, Katrina, and Jared get the rest.\n They want to share %d apples. \n Draw lines in the pile to \n evenly split the apples." % (self.apples), font = ("Comic Sans MS", 30, "bold"), justify = CENTER)
            #character images from: https://www.alimcjoy.com/alissa-mcclure/how-to-talk-with-kids-about-race/
            imagePeople = PhotoImage(file='images/story/%d.png' % self.char)
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4, self.height//2 + 100, image = imagePeople)
            
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char - 1))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 250, self.height//2 + 100, image = imagePeople)
            
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char + 2))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 500, self.height//2 + 100, image = imagePeople)
            
        elif self.apples % 5 == 0:
            count = self.apples / 5

            for i in range(self.apples):
                if (i + 1) % count == 0:
                    self.correctR.append((x, 3 * self.height//4 + 100))
                canvas.create_image(x, 3*self.height //4 + 100, image = imageApple)
                x += space
            
            self.char = 5
            canvas.create_text(self.width // 2, self.height//4 - 80, text = "Chris gives his 5 friends %d of his apples. \n Adam, Patricia, Megan, Katrina, and Jared \n want to share %d apples. \n Draw lines in the pile to \n evenly split the apples." % (self.apples, self.apples), font = ("Comic Sans MS", 30, "bold"), justify = CENTER)
            imagePeople = PhotoImage(file='images/story/%d.png' % self.char)
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 - 125, self.height//2 + 100, image = imagePeople)
            
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char - 1))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 65, self.height//2 + 100, image = imagePeople)
            
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char - 2))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 265, self.height//2 + 100, image = imagePeople)
            
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char - 3))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 465, self.height//2 + 100, image = imagePeople)
            
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char - 4))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 665, self.height//2 + 100, image = imagePeople)
        
        elif self.apples % 4 == 0:
            count = self.apples / 4
            for i in range(self.apples):
                if (i + 1) % count == 0:
                    self.correctR.append((x, 3 * self.height//4 + 100))
                canvas.create_image(x, 3*self.height //4 + 100, image = imageApple)
                x += space
                
            self.char = 4
            canvas.create_text(self.width // 2, self.height//4 - 80, text = "Chris gives Jared some apples and \nPatricia, Megan, Katrina, and Adam \n the remaining apples. \n They want to share %d apples. \n Draw lines in the pile to \n evenly split the apples." % (self.apples), font = ("Comic Sans MS", 30, "bold"), justify = CENTER)
            imagePeople = PhotoImage(file='images/story/%d.png' % self.char)
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 - 100, self.height//2 + 100, image = imagePeople)
            
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char - 1))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 100, self.height//2 + 100, image = imagePeople)
            
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char - 2))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 300, self.height//2 + 100, image = imagePeople)
        
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char - 3))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 500, self.height//2 + 100, image = imagePeople)
            
        elif self.apples % 2 == 0:
            count = self.apples / 4
            for i in range(self.apples):
                if (i + 1) % count == 0:
                    self.correctR.append((x, 3 * self.height//4 + 100))
                canvas.create_image(x, 3*self.height //4 + 100, image = imageApple)
                x += space
                
            self.char = 2
            canvas.create_text(self.width // 2, self.height//4 - 80, text = "Chris gives Jared, Patricia, and Megan \n some apples and Adam and Katrina \n get the rest. \n They want to share %d apples. \n Draw lines in the pile to \n evenly split the apples." % (self.apples), font = ("Comic Sans MS", 30, "bold"), justify = CENTER)
            imagePeople = PhotoImage(file='images/story/%d.png' % self.char)
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4, self.height//2 + 100, image = imagePeople)
            
            imagePeople = PhotoImage(file='images/story/%d.png' % (self.char - 1))
            label = Label(image=imagePeople)
            label.image = imagePeople
            canvas.create_image(self.width//4 + 250, self.height//2 + 100, image = imagePeople)
            
    def drawLine(self, canvas, draw):
        for coord in range(len(draw)):
            if coord != len(draw) - 1:
                x1, y1, cmd1 = draw[coord]
                x2, y2, cmd2 = draw[coord + 1]
                if cmd1 == "color":
                    canvas.create_line(x1, y1, x2, y2, fill = "dark green", width = 15)
        
    def checkAnswer(self, draw):
        count = 0
        if draw == []:
            return False
        
        for i in range(len(draw)):
            (x,y,cmd) = draw[i]
            for j in range(len(self.correctR)):
                (xR,yR) = self.correctR[j]
                if xR + 30 <= x <= xR + 90:
                    count += 1
        return (count == len(draw))
