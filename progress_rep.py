import module_manager
module_manager.review()

from tkinter import *

from start_screen import Start
from flashcards_ import Flashcards
from bubble_game import Bubble

import random
import copy

class Report(object):
    def __init__(self, width, height, userName, bubble, flashcard, data = None):
        self.width = width 
        self.height = height
        self.user = userName
        self.bubble = bubble
        self.flashcard = flashcard
        self.data = data
        
    def __repr__(self):
        return "%s's progress report" % self.user 
    
    def __eq__(self, other):
        return(isinstance(other, Report) and self.name == other.name)
        
    def __hash__(self):
        return hash(self.name)
    
    def returnName(self):
        return self.user
    
    def display(self, canvas):
        #image from: https://www.123rf.com/
        imagePR = PhotoImage(file='images/prgr.png')
        label = Label(image=imagePR)
        label.image = imagePR
        canvas.create_image(self.width//4, self.height//4, image = imagePR)
        canvas.create_text(3 * self.width // 4 - 50, self.height//4 - 100, text = "%s's" % self.user, font = ("Comic Sans MS", 60, "bold"))
        canvas.create_text(3 * self.width // 4 - 50, self.height//4 , text = "Progress", font = ("Comic Sans MS", 60, "bold"))
        canvas.create_text(3 * self.width // 4 - 50, self.height//4 + 100, text = "Report", font = ("Comic Sans MS", 60, "bold"))
        
        canvas.create_text(50, self.height // 2 + 50, text = "ADDITION", font = ("Comic Sans MS", 40, "bold"), anchor = W)
        canvas.create_rectangle(self.width - 350, self.height // 2 + 30, self.width - 50, self.height//2 + 70, width = 2)
        
        canvas.create_text(50, self.height // 2 + 150, text = "SUBTRACTION", font = ("Comic Sans MS", 40, "bold"), anchor = W)
        canvas.create_rectangle(self.width - 350, self.height // 2 + 130, self.width - 50, self.height//2 + 170, width = 2)
        
        canvas.create_text(50, self.height // 2 + 250, text = "MULTIPLICATION", font = ("Comic Sans MS", 40, "bold"), anchor = W)
        canvas.create_rectangle(self.width - 350, self.height // 2 + 230, self.width - 50, self.height//2 + 270, width = 2)
        
        canvas.create_text(50, self.height // 2 + 350, text = "DIVISION", font = ("Comic Sans MS", 40, "bold"), anchor = W)
        canvas.create_rectangle(self.width - 350, self.height // 2 + 330, self.width - 50, self.height//2 + 370, width = 2)
        
        
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "EXIT", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
    
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = self.height - 10
        y1 = self.height - 60 
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "sky blue", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "SAVE", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
        
    def displayData(self,canvas):
        [addPerc, subPerc, multPerc, divPerc] = Report.findData(self)
        print([addPerc, subPerc, multPerc, divPerc])
        x0 = self.width - 350
        xAddW = 300 * addPerc
        xSubW = 300 * subPerc
        xMultW = 300 * multPerc
        xDivW = 300 * divPerc
        canvas.create_rectangle(x0, self.height // 2 + 30, x0 + xAddW,  self.height//2 + 70, fill = "maroon1")
        canvas.create_rectangle(x0, self.height // 2 + 130, x0 + xSubW,  self.height//2 + 170, fill = "deep sky blue")
        canvas.create_rectangle(x0, self.height // 2 + 230, x0 + xMultW,  self.height//2 + 270, fill = "lime green")
        canvas.create_rectangle(x0, self.height // 2 + 330, x0 + xDivW,  self.height//2 + 370, fill = "gold")
        
    
    def findData(self): 
        if self.bubble.scoreForPG() != None:
            ((bubAdd, bubSub, bubMult), (bubAddA, bubSubA, bubMultA)) = self.bubble.scoreForPG()
        else: 
            ((bubAdd, bubSub, bubMult), (bubAddA, bubSubA, bubMultA)) = ((0,0,0),(0,0,0))
        if self.flashcard.dataForAlias() != None:
            ((flashAdd,flashSub,flashMult, flashDiv), (flashAddA, flashSubA, flashMultA, flashDivA)) = self.flashcard.dataForAlias()
        else: 
            ((flashAdd,flashSub,flashMult, flashDiv), (flashAddA, flashSubA, flashMultA, flashDivA)) = ((0,0,0,0),(0,0,0,0))
        if bubAddA + flashAddA == 0:
            addPerc = 0
        else:
            addPerc = (bubAdd + flashAdd) / (bubAddA + flashAddA)
            if addPerc <= 0:
                addPerc = 0
            elif addPerc > 1:
                addPerc = 1
        
        if bubSubA + flashSubA == 0:
            subPerc = 0
        else:
            subPerc = (bubSub + flashSub) / (bubSubA + flashSubA)
            if subPerc <= 0:
                subPerc = 0
            elif subPerc > 1:
                subPerc = 1
                
        if bubMultA + flashMultA == 0:
            multPerc = 0
        else:
            multPerc = (bubMult + flashMult) / (bubMultA + flashMultA)
            if multPerc <= 0:
                multPerc = 0
            elif multPerc > 1:
                multPerc = 1
        
        if flashDivA == 0:
            divPerc = 0
        else:
            divPerc = (flashDiv) / (flashDivA)
            if divPerc <= 0:
                divPerc = 0
            elif multPerc > 1:
                divPerc = 1
                
        return ([addPerc, subPerc, multPerc, divPerc])


