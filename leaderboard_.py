import module_manager
module_manager.review()

from tkinter import *

from start_screen import Start

import random
import copy

class Leaderboard(object):
    def __init__(self, width, height, users, bubbles):
        self.width = width 
        self.height = height
        self.users = users
        self.bubbles = bubbles
        self.rank = []
        self.d = { }
    
    def display(self, canvas):
        imageLB = PhotoImage(file='images/ldbrd.png')
        label = Label(image=imageLB)
        label.image = imageLB
        canvas.create_image(self.width//2, self.height//2, image = imageLB)
        
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "EXIT", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
    
    def displayRank(self,canvas):
        contents = Leaderboard.readFile(self, "leaderboard_data.txt")
        Leaderboard.rankUsers(self)
        copyRank = copy.deepcopy(self.rank)
        xN = self.width // 2 - 77
        xD = 2 * self.width // 3 + 95
        y = self.width // 3 - 10
        for (user, score) in self.rank:
            canvas.create_text(xN, y, text = "%s" % user, font = ("Comic Sans MS", 40))
            canvas.create_text(xD, y, text = "%d" % score, font = ("Comic Sans MS", 40))
            y += 60
    
    #112 notes, reads file that path leads to
    def readFile(self, path):
        with open(path, "rt") as f:
            return f.read()
            
    #112 notes, writes in file that path leads to
    def writeFile(self, path, contents):
        with open(path, "wt") as f:
            f.write(contents)
    
    def rankUsers(self):
        contents = Leaderboard.readFile(self, "leaderboard_data.txt")
        cont = str(self.rank) 
        self.rank = []
        lstUsers = []
        for key in self.users:
            if key in self.bubbles:
                lstUsers.append(key)
            
        for i in range(len(lstUsers)):
            name = lstUsers[i]
            self.d[name] = 0
            
        for i in range(len(lstUsers)):
            name = lstUsers[i]
            score = self.bubbles[name].scorePrintLB()
            self.d[name] = score
        
        while len(self.rank) != len(lstUsers):
            Currmax = max(self.d, key = self.d.get)
            self.rank.append((Currmax, self.d[Currmax]))
            del self.d[Currmax]
        
        return self.rank    
