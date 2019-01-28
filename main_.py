import module_manager
module_manager.review()

from start_screen import Start
from bubble_game import Bubble
from ml_main import Classif
from flashcards_ import Flashcards
from leaderboard_ import Leaderboard
from progress_rep import Report
from orchard_ import Orch
from divide_apple import AppleDiv
from recipe_ import Intro, Recipe

from tkinter import *
from PIL import ImageGrab

import random
import copy


def init(data):
    data.mode = "loading"
    data.timerCalls = 0

    #loading
    data.textID = 3
    data.dir = 1
    data.classif = Classif()
    
    #start
    data.drawName = ""
    data.appleCoord = [225,220]
    data.allStart = dict()
    data.start = Start(data.width, data.height, "tempName")
    data.image1 = (70,170)
    data.image2 = (225,170)
    data.image3 = (405,170)
    data.learn = (225,665) 
    data.bubbleNewColor = False
    data.flashNewColor = False
    data.storyNewColor = False
    data.logONC = False
    data.PFNC = False

    
    #bubble
    data.allBubbles = dict()
    data.bubble = Bubble(data.width,data.height, "tempName",0, None)
    data.draw = []
    data.imageW = 170
    data.bubbleInfo = []
    
    #flashcards
    data.fc = Flashcards(data.width,data.height,"tempName")
    data.allFC = dict()
    data.questionList = []
    data.drawNum = ""
    data.correct = None
    data.currTime = 0
    data.typeMath = None
    
    #leaderboard
    data.lb = Leaderboard(data.width, data.height, data.allStart, data.allBubbles)
    
    #report
    data.allProgress = dict()
    data.progress = Report(data.width, data.height, "tempName", data.bubble, data.fc)
    
    #orchard
    data.land = data.width * 3
    data.charPos = 100
    data.speed = 4
    data.walk = 1
    data.rWalk = 2
    data.lWalk = -1
    data.treePos = [600, 950, 1250, 1600, 2000, 2350, 2700, 3000, 3250]
    data.scrollX = 0
    data.scrollMarg = 100
    data.orch = Orch(data.width, data.height, data.land, data.charPos, data.treePos)
    data.question = data.orch.createQBT()
    data.draw2 = []
    data.score = 0
    data.orchFinish = False
    data.startTime = 0
    
    #divide
    data.apples = random.choice([8,9,10,12,14,15])
    data.draw3 = []
    data.divCorr = None
    data.currTimeD = 0
    
    #recipe
    data.intro = Intro(data.width, data.height)
    data.char = None
    data.step = 0
    data.name = ""
    data.recipe = None
    data.boxList = [[625, 437, 645, 457, False], [625, 465, 645, 485, False], [625, 493, 645, 513, False], [625, 521, 645, 541, False], [625, 549, 645, 569, False], [625, 625, 645, 645, False], [625, 653, 645, 673, False], [625, 681, 645, 701, False], [625, 709, 645, 729, False], [625, 737, 645, 757, False]]
    data.foodIndex = None
    data.fCoord = [[294, 153, 706, 423, 0], [294, 423, 706, 693, 0], [294, 693, 706, 963, 0]]
    data.fCorrect = 0
    data.sCoord = [[500, 253, True], [500, 353, True], [500, 453, True], [500, 553, True], [500, 653, True], [500, 753, True], [500, 853, True]]
    data.sCorrect = 0
    data.recList = [[63, 299, 281, 500], [281, 299, 499, 500], [499, 299, 717, 500], [717, 299, 935, 500], [63, 500, 281, 701], [281, 500, 499, 701], [499, 500, 717, 701], [717, 500, 935, 701]]
    data.eggList = [[100, 500, False], [300, 500, False], [500, 500, False], [700, 500, False], [900, 500, False]]
    data.eCorrect = 0
    data.s2Coord = [[294, 153, 706, 423, 0], [294, 423, 706, 693, 0], [294, 693, 706, 963, 0]]
    data.s2Correct = 0
    data.lemList = [[500, 253, True], [500, 353, True], [500, 453, True], [500, 553, True], [500, 653, True], [500, 753, True], [500, 853, True]]
    data.lCorrect = 0
    data.drawNumber = ""
    data.incorrect = False
    data.currTimeR = 0
    data.currTimeRC = 0
    data.i = None
 
#mouse tracking when pressed 
def motion(event):
    x, y = event.x, event.y
    return((x, y))
    
def startMP(event,data):
    #clicking into modes
    x,y = 3 * data.width//4 - 100, data.height//2
    if x - 159 <= event.x <= x + 164 and y - 90 <= event.y <= y + 90:
        data.mode = "bubbleChoose"
    x,y = 3 * data.width//4,data.height//4
    if x - 150 <= event.x <= x + 150 and y - 80 <= event.y <= y + 80:
        data.mode = "flashcardsChoose"
    x,y = 3 * data.width//4 + 25, 3 * data.height//4
    if x - 140 <= event.x <= x + 140 and y - 80 <= event.y <= y <= y + 80:
        data.mode = "orch"
    
    #log out    
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if x0 <= event.x <= x1 and y0 <= event.y <= y1:
        if data.bubble.returnName() != "tempName" and data.bubble.returnName() in data.allBubbles:
            score = data.bubble.scoreForLB()
            dataPG = data.bubble.scoreForPG()
            data.allBubbles[data.drawName] = Bubble(data.width, data.height, data.start.sendInfo(), score, dataPG)
        
        if data.progress.returnName() != "tempName" and data.progress.returnName() in data.allProgress:
            perc = data.progress.findData()
            data.allProgress[data.drawName] = Report(data.width, data.height, data.drawName, data.bubble, data.fc, perc)
            
        if data.fc.returnName() != "tempName" and data.fc.returnName() in data.allFC:
            nums = data.fc.dataForAlias()
            print("if log out", nums)
            data.allFC[data.drawName] = Flashcards(data.width, data.height, data.drawName, nums)
        data.mode = "input"
        data.progress = Report(data.width, data.height, "tempName", data.bubble, data.fc)
        data.bubble = Bubble(data.width,data.height, "tempName",0, 0)
        data.fc = Flashcards(data.width,data.height,"tempName")
        data.drawName = ""
    
    #progress report    
    margin = 15
    x0 = data.width - margin - 200
    x1 = data.width - margin
    y0 = data.height - 10
    y1 = data.height - 60
    if x0 <= event.x <= x1 and y0 >= event.y >= y1:
        name = data.start.sendInfo()
        if name not in data.allProgress:
            data.progress = Report(data.width, data.height, name, data.bubble, data.fc, None)
            currProgress = copy.copy(data.progress)
            data.allProgress[name] = currProgress
        else:
            perc = data.allProgress[name].findData()
            if name in data.allBubbles:
                data.bubble = data.allBubbles[name]
            if name in data.allFC:
                data.fc = data.allFC[name]
            data.progress = Report(data.width, data.height, name, data.bubble, data.fc, perc)
        data.mode = "progress"

def bubbleChooseMP(event,data):
    x,y = (3 * data.width//4 - 100,data.height//2)
    yCh = y + 90
    
    if x - 165 <= event.x <= x + 170 and y - 90 <= event.y <= y: 
        name = data.start.sendInfo()
        if name not in data.allBubbles:
            data.bubble = Bubble(data.width, data.height, name, 0, None)
            currBubble = copy.copy(data.bubble)
            data.allBubbles[name] = currBubble
        else:
            score = data.allBubbles[name].scoreForLB()
            dataPG = data.allBubbles[name].scoreForPG()
            data.bubble = Bubble(data.width, data.height, name, score, dataPG)
        data.mode = "bubble"
        
    elif x - 165 <= event.x <= x + 170 and y <= event.y <= yCh:
        if data.drawName in data.allBubbles:
            if data.bubble.returnName() == data.drawName:
                score = data.bubble.scoreForLB()
                dataPG = data.allBubbles[data.drawName].scoreForPG()
                data.allBubbles[data.drawName] = Bubble(data.width, data.height, data.start.sendInfo(), score, dataPG)
        data.mode = "leaderboard"
    
    else:
        data.mode = "start"  
        margin = 15
        x0 = data.width - margin - 120
        x1 = data.width - margin
        y0 = 10
        y1 = 60  
        #log out    
        if x0 < event.x < x1 and y0 < event.y < y1:
            data.mode = "input"
            data.drawName = ""
        #clicking into modes
        x,y = 3 * data.width//4 - 100, data.height//2
        if x - 159 <= event.x <= x + 164 and y - 90 <= event.y <= y + 90:
            data.mode = "bubbleChoose"
        x,y = 3 * data.width//4,data.height//4
        if x - 150 <= event.x <= x + 150 and y - 80 <= event.y <= y + 80:
            data.mode = "flashcardsChoose"
        x,y = 3 * data.width//4 + 25, 3 * data.height//4
        if x - 140 <= event.x <= x + 140 and y - 80 <= event.y <= y <= y + 80:
            data.mode = "story"

def bubbleMP(event, data):
    margin = 15
    
    #exiting game
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        score = data.bubble.scoreForLB()
        dataPG = data.bubble.scoreForPG()
        data.allBubbles[data.drawName] = Bubble(data.width, data.height, data.start.sendInfo(), score, dataPG)
        data.mode = "start"
        data.bubbleInfo = []
    #clearing the screen
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = data.height//2 + 180
    y1 = data.height//2 + 230
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        data.draw = []
    
    #instructions
    x0 = data.width - 40
    x1 = data.width - 10
    y0 = data.height - 40
    y1 = data.height - 10
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        data.mode = "bubbleInstructions"
    
    #entering answer
    x0 = 5 * data.width//8 + margin
    x1 = 5 * data.width//8 + margin + 120
    y0 = data.height//2 + 180
    y1 = data.height//2 + 230
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        cropX0 = data.topPlX + (5 * data.width//8 + 25)
        cropX1 = data.topPlX + (data.width - margin)
        cropY0 = data.topPlY + (data.height//2 - 174)
        cropY1 = data.topPlY + (data.height // 2 + 163)
        filename = "num.test.png"
        #PIL documentation http://effbot.org/imagingbook/pil-index.htm
        im = ImageGrab.grab().crop((cropX0,cropY0,cropX1,cropY1)).save(filename)
        expected = data.bubble.expectedAnswer(data.bubbleInfo)
        predicted = data.classif.predict(filename, expected)
        print(predicted)  #
        print(expected)   #
        if predicted == expected:
            data.bubbleInfo = data.bubble.popping(data.bubbleInfo)
        else:
            data.bubble.notPopping(data.bubbleInfo)
        data.draw = []
                
    #drawing in the screen
    (x,y) = motion(event)
    margin = 15
    if (5 * data.width//8 + margin<= x < data.width - margin and 
        data.height//2 - 172.5 < y < data.height // 2 + 172.5):
            if str(event.type) == "ButtonRelease":
                data.draw.append((x,y,"none"))
            else: 
                data.draw.append((x,y,"color"))

        
def bubbleInstructionsMP(event, data):
    #exit instructions
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        data.mode = "bubble"
    
def leaderboardMP(event, data):
    #exit leaderboard
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        data.mode = "start"

def flashcardsChooseAlias(event, data):
    name = data.start.sendInfo()
    if name not in data.allFC:
        data.fc = Flashcards(data.width, data.height, name, None)
        currFC = copy.copy(data.fc)
        data.allFC[name] = currFC
    else:
        info = data.allFC[name].dataForAlias()
        print("if choosing old name mode fc", info)
        data.fc = Flashcards(data.width, data.height, name, info)
        currFC = copy.copy(data.fc)
        data.allFC[name] = currFC

def flashcardsChooseMP(event, data):
    x0 = data.width//4
    y0 = data.height//3
    rectangleW = data.width//2
    rectangleH = 70
    x1 = x0 + rectangleW
    y1 = y0 + rectangleH
    y2 = y1 + rectangleH 
    y3 = y2 + rectangleH
    y4 = y3 + rectangleH
    y5 = y4 + rectangleH
    
    if x0 < event.x < x1 and y0 < event.y < y1:
        data.typeMath = "add"
        flashcardsChooseAlias(event, data)
        data.mode = "flashcards"
        
    elif x0 < event.x < x1 and y1 < event.y < y2:
        data.typeMath = "sub"
        flashcardsChooseAlias(event, data)
        data.mode = "flashcards"
        
    elif x0 < event.x < x1 and y2 < event.y < y3:
        data.typeMath = "mult"
        flashcardsChooseAlias(event, data)
        data.mode = "flashcards"
        
    elif x0 < event.x < x1 and y3 < event.y < y4:
        data.typeMath = "div"
        flashcardsChooseAlias(event, data)
        data.mode = "flashcards"
        
    elif x0 < event.x < x1 and y4 < event.y < y5:
        data.typeMath = "all"
        flashcardsChooseAlias(event, data)
        data.mode = "flashcards"
        
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if x0 < event.x < x1 and y0 < event.y < y1:
        data.mode = "start"


def flashcardsMP(event, data):
    #exit
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        info = data.fc.dataForAlias()
        print("if exiting", info)
        data.allFC[data.drawName] = Flashcards(data.width, data.height, data.drawName, info)
        data.mode = "start"
        data.questionList = []
        
        
    #instructions
    x0 = data.width - 40
    x1 = data.width - 10
    y0 = data.height - 40
    y1 = data.height - 10
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        data.mode = "fcInstructions"
    
def fcInstructionsMP(event, data):
    #exit instructions
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        data.mode = "flashcards"

def progressMP(event, data):
    #exit report
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
        data.mode = "start"
    
    #save report 
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = data.height - 10
    y1 = data.height - 60
    if (x0 <= event.x <= x1 and y0 >= event.y >= y1):
        cropX0 = data.topPlX + 20
        cropX1 = data.topPlX + data.width
        cropY0 = data.topPlY + 70
        cropY1 = data.topPlY + data.height - 70
        filename = "123Learn.Progress.Report.png"
        im = ImageGrab.grab().crop((cropX0,cropY0,cropX1,cropY1)).save(filename)

def orchMP(event, data):
    #drawing in the screen
    (x,y) = motion(event)
    margin = 15
    if (margin <= x <= 3 * data.width//8 - margin and 
        data.height//4 - 222.5 < y < data.height // 4 + 122.5):
            if str(event.type) == "ButtonRelease":
                data.draw2.append((x,y,"none"))
            else: 
                data.draw2.append((x,y,"color"))
    
    #clear
    x0 = 3 * data.width//8 - margin + 10
    x1 = 3 * data.width//8 - margin + 130
    y0 = data.height//4 - 222.5
    y1 = data.height//4 - 222.5 + 50
    if x0 <= event.x <= x1 and y0 <= event.y <= y1:
        data.draw2 = []
        
    #enter 
    margin = 15                
    x0 = 3 * data.width//8 - margin + 10
    x1 = 3 * data.width//8 - margin + 130
    y0 = data.height//4 - 222.5 + 60
    y1 = data.height//4 - 222.5 + 110
    if x0 <= event.x <= x1 and y0 <= event.y <= y1:
        cropX0 = data.topPlX + (25)
        cropX1 = data.topPlX + (3 * data.width//8 - margin)
        cropY0 = data.topPlY + (data.height//4 - 222.5)
        cropY1 = data.topPlY + (data.height // 4 + 112.5)
        filename = "num.test.png"
        #PIL documentation http://effbot.org/imagingbook/pil-index.htm
        im = ImageGrab.grab().crop((cropX0,cropY0,cropX1,cropY1)).save(filename)
        expected = data.orch.expectedAnswer(data.question)
        predicted = data.classif.predict(filename, expected)
        print(predicted)  #
        print(expected)   #
        if predicted == expected:
            data.treePos.pop(0)
            data.question.pop(0)
            data.speed = 4
            data.score += 6
        data.draw2 = []
        
    if data.orchFinish == True:
        x0 = data.width//2 - 100 
        y0 = data.height//2 - 30
        x1 =data.width//2 + 100
        y1 = data.height//2 + 30
        if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            data.mode = "div"
        
def divAppleMP(event, data):
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = data.height - 10
    y1 = data.height - 60 
    if x0 <= event.x <= x1 and y0 >= event.y >= y1:
        data.divCorr = data.div.checkAnswer(data.draw3)
        
    (x,y) = motion(event)
    if 0 <= x <= data.width and 2 * data.height // 3 <= y <= data.height - 70:
        if str(event.type) == "ButtonRelease":
            data.draw3.append((x,y,"none"))
        else: 
            data.draw3.append((x,y,"color"))
            
    if data.divCorr == True:
        x0 = data.width//2 - 100 
        y0 = data.height//2 - 30
        x1 =data.width//2 + 100
        y1 = data.height//2 + 30
        if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            data.mode = "intro"

def recipeMP(event,data):
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if x0 <= event.x <= x1 and y0 <= event.y <= y1:
        data.mode = "start"
    if data.step == 1:
        x0 = 3 * data.width //4 - 94
        x1 = 3 * data.width //4 + 94
        y0 = data.height //2 - 112
        y1 = data.height //2 + 112
        if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            data.step = 2
    
    if data.step == 2:
        for i in range(len(data.boxList)):
            (x0, y0, x1, y1, check) = data.boxList[i]
            if x0 <= event.x <= x1 and y0 <= event.y <= y1 and check == False:
                data.i = i
                data.step = 3
                
    if data.step == 4:
        data.foodIndex = data.i
        margin = 15
        x0 = margin
        x1 = margin + 120
        y0 = 10
        y1 = 60
        if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            data.step = 2
            
            
        if data.foodIndex == 0:
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = 10
            y1 = 60
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                data.mode = "start"
            
            for i in range(len(data.fCoord)):
                (x0,y0,x1,y1,im) = data.fCoord[i]
                if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                    if im <= 3:
                        data.fCoord[i][4] += 1
                        data.fCorrect += 1
            #enter
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = data.height - 10
            y1 = data.height - 60 
            if x0 <= event.x <= x1 and y0 >= event.y >= y1:
                if data.fCorrect == 10:
                    data.boxList[data.foodIndex][4] = True
                    data.step = 2
                else:
                    data.incorrect = True
                    data.fCorrect = 0
                    for i in range(len(data.fCoord)):
                        data.fCoord[i][4] = 0
                    
                    
        if data.foodIndex == 1:
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = 10
            y1 = 60
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                data.mode = "start"
            
            for i in range(len(data.sCoord)):
                (x0,y0,empt) = data.sCoord[i]
                if x0 - 314 //2 <= event.x <= x0 + 314//2 and y0 - 128//2<= event.y <= y0 + 128//2:
                    if empt == True:
                        data.sCoord[i][2] = False
                        data.sCorrect += 1
            #enter
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = data.height - 10
            y1 = data.height - 60 
            if x0 <= event.x <= x1 and y0 >= event.y >= y1:
                if data.sCorrect == 4:
                    data.boxList[data.foodIndex][4] = True
                    data.step = 2
                else:
                    data.incorrect = True
                    data.sCorrect = 0
                    for i in range(len(data.sCoord)):    
                        data.sCoord[i][2] = True
        
        if data.foodIndex == 2:
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = 10
            y1 = 60
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                data.mode = "start"
            
            for i in range(len(data.recList)):
                (x0,y0,x1,y1) = data.recList[i]
                if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                    if i == 2:
                        data.boxList[data.foodIndex][4] = True
                        data.step = 2
                    else:
                        data.incorrect = True
                        
        if data.foodIndex == 3:
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = 10
            y1 = 60
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                data.mode = "start"
                
            for i in range(len(data.recList)):
                (x0,y0,x1,y1) = data.recList[i]
                if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                    if i == 5:
                        data.boxList[data.foodIndex][4] = True
                        data.step = 2
                    else:
                        data.incorrect = True
                        
        if data.foodIndex == 4:
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = 10
            y1 = 60
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                data.mode = "start"
            
            for i in range(len(data.eggList)):
                (x,y,crack) = data.eggList[i]
                if x - 100 <= event.x <=  x + 100 and  y - 192//2 <= event.y <= y + 192//2:
                    if crack == False:
                        data.eggList[i][2] = True
                        data.eCorrect += 1
            
            #enter
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = data.height - 10
            y1 = data.height - 60 
            if x0 <= event.x <= x1 and y0 >= event.y >= y1:
                if data.eCorrect == 2:
                    data.boxList[data.foodIndex][4] = True
                    data.step = 2
                else:
                    data.incorrect = True
                    data.eCorrect = 0
                    for i in range(len(data.eggList)):
                        data.eggList[i][2] = False
                    
        if data.foodIndex == 5:
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = 10
            y1 = 60
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                data.mode = "start"
            
            for i in range(len(data.lemList)):
                (x0,y0,empt) = data.lemList[i]
                if x0 - 305 //2 <= event.x <= x0 + 305//2 and y0 - 100//2<= event.y <= y0 + 100//2:
                    if empt == True:
                        data.lemList[i][2] = False
                        data.lCorrect += 1
            #enter
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = data.height - 10
            y1 = data.height - 60 
            if x0 <= event.x <= x1 and y0 >= event.y >= y1:
                if data.lCorrect == 2:
                    data.boxList[data.foodIndex][4] = True
                    data.step = 2
                else:
                    data.incorrect = True
                    data.lCorrect = 0
                    for i in range(len(data.lemList)):
                        data.lemList[i][2] = True
                    
        if data.foodIndex == 6:
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = 10
            y1 = 60
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                data.mode = "start"
                
            for i in range(len(data.recList)):
                (x0,y0,x1,y1) = data.recList[i]
                if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                    if i == 4:
                        data.boxList[data.foodIndex][4] = True
                        data.step = 2
                    else:
                        data.incorrect = True
        
        if data.foodIndex == 7:
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = 10
            y1 = 60
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                data.mode = "start"
            
            for i in range(len(data.s2Coord)):
                (x0,y0,x1,y1,im) = data.s2Coord[i]
                if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                    if im <= 2:
                        data.s2Coord[i][4] += 1
                        data.s2Correct += 1
                    
            #enter
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = data.height - 10
            y1 = data.height - 60 
            if x0 <= event.x <= x1 and y0 >= event.y >= y1:
                if data.s2Correct == 2:
                    data.boxList[data.foodIndex][4] = True
                    data.step = 2
                else:
                    data.incorrect = True
                    data.s2Correct = 0
                    for i in range(len(data.s2Coord)):
                        data.s2Coord[i][4] = 0
        if data.foodIndex == 8:
            margin = 15
            x0 = data.width - margin - 120
            x1 = data.width - margin
            y0 = 10
            y1 = 60
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                data.mode = "start"
            
            for i in range(len(data.recList)):
                (x0,y0,x1,y1) = data.recList[i]
                if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                    if i == 6:
                        data.boxList[data.foodIndex][4] = True
                        data.step = 2
                    else:
                        data.incorrect = True

def introAppMP(event,data):
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if x0 <= event.x <= x1 and y0 <= event.y <= y1:
        data.mode = "start"
    if 25 <= event.x <= (data.width) - 810 and (data.height // 2) - 210 <= event.y <= (data.height // 2) + 201:
        data.char = 1
        data.name = "Adam"
    elif (data.width) - 810 <= event.x <= (data.width) - 620  and (data.height // 2) - 210 <= event.y <= (data.height // 2) + 201:
        data.char = 2
        data.name = "Patricia"
    elif (data.width) - 620 <= event.x <= (data.width) - 420  and (data.height // 2) - 210 <= event.y <= (data.height // 2) + 201:
        data.char = 3
        data.name = "Megan"
    elif (data.width) - 420 <= event.x <= (data.width) - 220  and (data.height // 2) - 210 <= event.y <= (data.height // 2) + 201:
        data.char = 4
        data.name = "Katrina"
    elif (data.width) - 220 <= event.x <= (data.width) - 25  and (data.height // 2) - 210 <= event.y <= (data.height // 2) + 201:
        data.char = 5
        data.name = "Jared"
    data.recipe = Recipe(data.width, data.height, data.char, data.name)
    data.mode = "recipe" 
    data.step = 1

def motion2(event, data):
    x,y = event.x, event.y
    #from https://stackoverflow.com/questions/22925599/mouse-position-python-tkinter (given to me by Kyra)
    #tracks mouse around screen
    
    xB,yB = 3 * data.width//4 - 100, data.height//2
    if xB - 159 <= x <= xB + 164 and yB - 90 <= y <= yB + 90:
        data.bubbleNewColor = True
    else: 
        data.bubbleNewColor = False
        
    xF,yF = 3 * data.width//4,data.height//4
    if xF - 150 <= x <= xF + 150 and yF - 80 <= y <= yF + 80:
        data.flashNewColor = True
    else: 
        data.flashNewColor = False
    
    xS,yS = 3 * data.width//4 + 25, 3 * data.height//4
    if xS - 140 <= x <= xS + 140 and yS - 80 <= y <= yS + 80:
        data.storyNewColor = True
    else: 
        data.storyNewColor = False
    
    margin = 15
    x0 = data.width - margin - 120
    x1 = data.width - margin
    y0 = 10
    y1 = 60
    if x0 <= event.x <= x1 and y0 <= event.y <= y1:
        data.logONC = True
    else:
        data.logONC = False
    
    margin = 15
    x0 = data.width - margin - 200
    x1 = data.width - margin
    y0 = data.height - 10
    y1 = data.height - 60
    if x0 <= event.x <= x1 and y0 >= event.y >= y1:
        data.PFNC = True
    else:
        data.PFNC = False
    

def mousePressed(event, data):
    if data.mode == "start":
        startMP(event,data)

    elif data.mode == "bubble":
        bubbleMP(event,data)
    
    elif data.mode == "bubbleChoose":
        bubbleChooseMP(event,data)

    elif data.mode == "bubbleInstructions":
        bubbleInstructionsMP(event,data)
    
    elif data.mode == "leaderboard":
        leaderboardMP(event, data)
        
    elif data.mode == "flashcardsChoose":
        flashcardsChooseMP(event, data)
        
    elif data.mode == "flashcards":
        flashcardsMP(event, data)
        
    elif data.mode == "fcInstructions":
        fcInstructionsMP(event, data)
        
    elif data.mode == "progress":
        progressMP(event, data)
    
    elif data.mode == "orch":
        orchMP(event,data)
    
    elif data.mode == "div":
        divAppleMP(event, data)
    
    elif data.mode == "intro":
        introAppMP(event,data)
        
    elif data.mode == "recipe":
        recipeMP(event,data)
        
    
def flashcardsKP(event, data):
    #type answer
    if event.keysym.isdigit():
        data.drawNum = data.drawNum + event.keysym
    
    #backspace to fix mistakes
    if event.keysym == "BackSpace":
        data.drawNum = data.drawNum[:len(data.drawNum) - 1]
    
    #enter answer
    if event.keysym == "Return":
        expected = data.fc.expectedAnswer(data.questionList)
        if expected == int(data.drawNum):
            data.fc.correct(True, data.questionList)
            data.correct = True
            data.questionList.pop()
            data.drawNum = ""
        else:
            data.fc.correct(False, data.questionList)
            data.correct = False
            data.drawNum = ""

def inputKP(event,data):
    #type answer
    if event.char != "":
        if ord("A") <= ord(event.char) <= ord("z"):
            data.drawName = data.drawName + event.char
    
    #backspace to fix mistakes
    if event.keysym == "BackSpace":
        data.drawName = data.drawName[:len(data.drawName) - 1]
    
    #enter answer
    if event.keysym == "Return":
        data.start = Start(data.width, data.height, data.drawName)
        if data.drawName not in data.allStart:
            currStart = copy.copy(data.start)
            data.allStart[data.drawName] = currStart
        data.mode = "start"
        
def recipeKP(event, data):
    if event.keysym == "p":
        for i in range(len(data.boxList)):
            data.boxList[i][4] = True
            
    if data.foodIndex == 9:
        if event.keysym.isdigit() or event.keysym == "period":
            data.drawNumber = data.drawNumber + event.char
        
        #backspace to fix mistakes
        if event.keysym == "BackSpace":
            data.drawNumber = data.drawNumber[:len(data.drawNumber) - 1]
        
        #enter answer
        if event.keysym == "Return":
            if data.drawNumber == "0.25" or data.drawNumber == ".25":
                data.boxList[data.foodIndex][4] = True
                data.step = 2
            else:
                data.incorrect = True
                data.drawNumber = ""

def keyPressed(event, data):
    if data.mode == "input":
        inputKP(event,data)
    if data.mode == "flashcards":
        flashcardsKP(event, data)
    
    if data.mode == "bubble":
        if event.keysym == "c":
            data.bubbleInfo = data.bubble.popping(data.bubbleInfo)
            
    if data.mode == "orch":
        if event.keysym == "o":
            data.treePos.pop(0)
            data.question.pop(0)
            data.speed = 4
            data.score += 6
    
    if data.mode == "recipe":
        recipeKP(event,data)
            

def timerFired(data):
    data.timerCalls += 1
    
    if data.mode == "loading":
        if data.timerCalls % 7 == 0:
            data.textID += data.dir
        if data.textID > 3:
            data.textID = 0
    
    # #machine learns!
    if data.timerCalls == 5:
        data.classif.train()
        data.mode = "input"
    
    if data.mode == "input":
        data.appleCoord[1] += 2
        if data.appleCoord[1] == 230:
            data.appleCoord[1] = 220

    if data.mode == "start":
        #title
        
        if data.timerCalls % 3 == 0:
            data.image1 = (random.randint(70,80),random.randint(170,180))
            data.image2 = (random.randint(225,235),random.randint(170,180))
            data.image3 = (random.randint(405,415),random.randint(170,180))
            data.learn = (random.randint(225,235),random.randint(665,670))
    
    elif data.mode == "bubble":
        #new bubbles
        if data.bubbleInfo == []:
            data.bubbleInfo.append(data.bubble.createBubbles())
        if data.bubbleInfo != []:
            for bubble in data.bubbleInfo:
                if bubble[1] - data.imageW >= data.height:
                    data.bubble.notPopping(data.bubbleInfo)
                    data.bubbleInfo.remove(bubble) 
                else:
                    bubble[1] += 15
    
        if data.bubbleInfo != []:
            for bubble in data.bubbleInfo:
                x,y,id,popping,num1,num2,math = bubble
                if popping == True:
                    bubble[2] += 1
                if id == 5:
                    data.bubbleInfo.remove(bubble)
                    
    elif data.mode == "flashcards":
        if data.questionList == []:
            data.questionList.append(data.fc.createQuestion(data.typeMath))
        
        if data.correct == True or data.correct == False:
            data.currTime += 1
            if data.currTime == 5:
                data.correct = None
                data.currTime = 0
                
    elif data.mode == "orch":
        data.startTime += 1
        if data.startTime >= 20:
            data.scrollX += data.speed 
            data.walk = data.rWalk
            data.rWalk += 1
            if data.rWalk == 6:
                data.rWalk = 1
        
        if data.treePos != []:
            if data.charPos + data.scrollX >= data.treePos[0] - 3 * data.scrollX:
                data.walk = 5
                data.speed = 0
        if data.treePos == []:
            if data.charPos + data.scrollX >= 2500 - data.scrollX:
                data.speed = 0
                data.orchFinish = True

    elif data.mode == "div":
        if data.divCorr == False:
            data.currTimeD += 1
            if data.currTimeD == 7:
                data.divCorr = None
                data.draw3 = []
                data.currTimeD = 0
                
    elif data.mode == "recipe":
        if data.incorrect == True:
            data.currTimeR += 1
            if data.currTimeR == 5:
                data.incorrect = False
                data.currTimeR = 0
        
        if data.step == 3:
            data.currTimeRC += 1
            if data.currTimeRC == 2:
                data.step = 4
                data.currTimeRC = 0
    
def loadingDA(canvas, data):
    data.start.loading(canvas, data.textID)

def startDA(canvas, data):
    data.start.drawBackground(canvas)
    data.start.drawTitle(canvas,data.image1,data.image2,data.image3,data.learn)
    data.start.drawClickModes(canvas)
    if data.bubbleNewColor == True:
        x,y = (3 * data.width//4 - 100,data.height//2)
        canvas.create_oval(x - 159, y - 90, x + 164, y + 90, 
                        fill = "DarkOliveGreen2",width = 3)
        canvas.create_oval(x - 163, y - 87, x + 165, y + 88, width = 3)
        canvas.create_oval(x - 162, y - 91, x + 169, y + 83, width = 3)
        canvas.create_text(x,y,text = "Bubble Burst!",fill = "white",
                            font = ("Comic Sans MS", 25, "bold"))
                            
    if data.flashNewColor == True:
        x,y = (3 * data.width//4,data.height//4)
        canvas.create_oval(x - 150, y - 80, x + 150, y + 80, 
                        fill = "SteelBlue3", width = 3)
        canvas.create_oval(x - 155, y - 79, x + 155, y + 79, width = 3)
        canvas.create_oval(x - 151, y - 84, x + 151, y + 86, width = 3)
        canvas.create_text(x,y,text = "Advanced\nFlashcards",fill = "white", justify = CENTER, font = ("Comic Sans MS", 25, "bold"))
        
    if data.storyNewColor == True:
        x,y = (3 * data.width//4 + 25, 3 * data.height//4)
        canvas.create_oval(x - 140, y - 80, x + 140, y + 80, fill = "sandy brown",
                        width = 2)
        canvas.create_oval(x - 145, y - 80, x + 141, y + 77, width = 3)
        canvas.create_oval(x - 139, y - 77, x + 143, y + 83, width = 3)
        canvas.create_text(x,y,text = "Apple Picking!",fill = "white",
                            font = ("Comic Sans MS", 25, "bold"))
        
    if data.logONC == True:
        margin = 15
        x0 = data.width - margin - 120
        x1 = data.width - margin
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "LightPink1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "LOG OUT", 
                           fill = "white", font = ("Comic Sans MS", 15, "bold"))
                           
    if data.PFNC == True:
        margin = 15
        x0 = data.width - margin - 200
        x1 = data.width - margin
        y0 = data.height - 10
        y1 = data.height - 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "LightBlue1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "Progress Report", 
                           fill = "white", font = ("Comic Sans MS", 15, "bold"))

def bubbleDA(canvas, data):
    #background
    imageBubBkg = PhotoImage(file='images/large_bubble/bubble_bkg.png')
    label = Label(image=imageBubBkg)
    label.image = imageBubBkg
    canvas.create_image(data.width//2, data.height//2, image = imageBubBkg)
    
    #bubbles
    data.bubble.drawBubbles(canvas,data.bubbleInfo)
    
    #screen
    data.bubble.drawOnScreen(canvas,data.draw)

def bubbleInstructionsDA(canvas, data):
    data.bubble.instructions(canvas)
    
def flashcardsChooseDA(canvas, data):
    data.fc.chooseTypeQuestion(canvas)
    
def flashcardsDA(canvas, data):
    data.fc.drawBackground(canvas)
    data.fc.drawQuestion(canvas, data.questionList)
    data.fc.drawAnswer(canvas, data.drawNum)
    data.fc.screenKeys(canvas)
    if data.correct == True:
        data.fc.correctDraw(canvas, True)
    elif data.correct == False:
        data.fc.correctDraw(canvas, False)
        
def fcInstructionsDA(canvas, data):
    data.fc.instructions(canvas)
    
def leaderboardDA(canvas, data):
    data.lb.display(canvas)
    data.lb.displayRank(canvas)
    
def inputDA(canvas, data):
    data.start.drawBackground(canvas)
    data.start.inputName(canvas, data.drawName, data.appleCoord)   
    
def progressDA(canvas, data):
    data.progress.display(canvas)
    data.progress.displayData(canvas)
    
def orchDA(canvas, data):
    data.orch.drawLand(canvas, data.scrollX, data.question, data.score)
    data.orch.drawChar(canvas, data.scrollX,data.walk)
    data.orch.drawOnScreen(canvas, data.draw2)
    if data.orchFinish == True:
        canvas.create_rectangle(data.width//2 - 100, data.height//2 - 30, data.width//2 + 100, data.height//2 + 30, fill = "green", outline = "green")
        canvas.create_text(data.width//2, data.height//2, text = "NEXT", font = ("Comic Sans MS", 40, "bold"), fill = "white")

def divAppleDA(canvas, data):
    if data.divCorr == None:
        data.div = AppleDiv(data.width, data.height, data.apples)
        data.div.drawApples(canvas)
        data.div.drawLine(canvas, data.draw3)
    if data.divCorr == True:
        canvas.create_rectangle(0,0,data.width, data.height,fill = "white", outline = "white")
        canvas.create_text(data.width//2, data.height//3, text = "Good job!", font = ("Comic Sans MS", 60, "bold"), fill = "green")
        canvas.create_rectangle(data.width//2 - 100, data.height//2 - 30, data.width//2 + 100, data.height//2 + 30, fill = "green", outline = "green")
        canvas.create_text(data.width//2, data.height//2, text = "NEXT", font = ("Comic Sans MS", 40, "bold"), fill = "white")
    elif data.divCorr == False:
        canvas.create_rectangle(0,0,data.width,data.height, fill = "light pink", outline = "light pink")
        canvas.create_text(data.width//2, data.height//2, font = ("Comic Sans MS", 40, "bold"), text = "Try Again!")
    
def recipeDA(canvas,data):
    if data.step == 1:
        data.recipe.stepOne(canvas)
    elif data.step == 2:
        data.recipe.stepTwo(canvas)
        data.recipe.drawBoxes(canvas, data.boxList)
    elif data.step == 4:
        data.recipe.makeFood(canvas, data.i, data.fCoord, data.sCoord, data.recList, data.eggList, data.lemList, data.drawNumber, data.s2Coord)
        
    if data.incorrect == True:
        canvas.create_rectangle(0,0,data.width,data.height, fill = "light pink", outline = "light pink")
        canvas.create_text(data.width//2, data.height//2, font = ("Comic Sans MS", 40, "bold"), text = "Try Again!")
    
def redrawAll(canvas, data):
    if data.mode == "loading":
        loadingDA(canvas, data)
    
    elif data.mode == "input":
        inputDA(canvas, data)
    
    if data.mode == "start":
        startDA(canvas, data)
        
    elif data.mode == "bubble":
        bubbleDA(canvas, data)
    
    elif data.mode == "bubbleChoose":
        startDA(canvas, data)
        data.start.drawBubbleOpt(canvas)
    
    elif data.mode == "bubbleInstructions":
        bubbleInstructionsDA(canvas, data)
    
    elif data.mode == "leaderboard":
        leaderboardDA(canvas, data)
    
    elif data.mode == "flashcards":
        flashcardsDA(canvas, data)
    
    elif data.mode == "flashcardsChoose":
        flashcardsChooseDA(canvas, data)
        
    elif data.mode == "fcInstructions":
        fcInstructionsDA(canvas, data)
        
    elif data.mode == "progress":
        progressDA(canvas, data)
    
    elif data.mode == "orch":
        orchDA(canvas, data)
    
    elif data.mode == "div":
        divAppleDA(canvas, data)
        
    elif data.mode == "intro":
        data.intro.chooseChar(canvas)
    
    elif data.mode == "recipe":
        recipeDA(canvas,data)

#run function from 112 notes, but modified

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)
    
    #modified 
    def motion2Wrapper(event,canvas,data):
        motion2(event, data)
        redrawAllWrapper(canvas, data)
        
    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 25 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    
    #modified:
    screenW = root.winfo_screenwidth()
    screenH = root.winfo_screenheight()
    topPlX = screenW//2 - data.width//2
    topPlY = screenH//2 - data.height//2
    data.topPlX = topPlX
    data.topPlY = topPlY
    #center tkinter screen
    #learned from documentation: http://zetcode.com/gui/tkinter/introduction/
    root.geometry("%dx%d+%d+%d" % (data.width, data.height, topPlX, 0))
    root.title("1 2 3 Learn!")
    init(data)

    #create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    
    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
                            
    #modified for mouse tracking:
    root.bind("<B1-Motion>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<ButtonRelease-1>", lambda event:
                            mousePressedWrapper(event,canvas,data))
    root.bind("<Motion>", lambda event:
                            motion2Wrapper(event,canvas,data))
    timerFiredWrapper(canvas, data)
    
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 1000)
