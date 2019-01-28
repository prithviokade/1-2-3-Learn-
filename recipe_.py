
from tkinter import *
import random
import copy

class Intro(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def chooseChar(self, canvas):
        #https://www.alimcjoy.com/alissa-mcclure/how-to-talk-with-kids-about-race/
        canvas.create_text(self.width // 2, self.height//4 - 100, text = "Choose your character!", font = ("Comic Sans MS", 60, "bold"))
        imagePeople = PhotoImage(file='images/story/people.png')
        label = Label(image=imagePeople)
        label.image = imagePeople
        canvas.create_image(self.width//2, self.height//2, image = imagePeople)
        canvas.create_rectangle( 25 , (self.height // 2) - 210, (self.width) - 810, (self.height // 2) + 201, width = 2, outline = "light pink")
        canvas.create_rectangle( (self.width) - 810, (self.height // 2) - 210, (self.width) - 620, (self.height // 2) + 201, width = 2, outline = "light pink")
        canvas.create_rectangle( (self.width) - 620, (self.height // 2) - 210, (self.width) - 420, (self.height // 2) + 201, width = 2, outline = "light pink")
        canvas.create_rectangle( (self.width) - 420, (self.height // 2) - 210, (self.width) - 220, (self.height // 2) + 201, width = 2, outline = "light pink")
        canvas.create_rectangle( (self.width) - 220, (self.height // 2) - 210, (self.width) - 25, (self.height // 2) + 201, width = 2, outline = "light pink")
        
        canvas.create_text(107.5, self.height//2 + 231, text = "Adam", font = ("Comic Sans MS", 25, "bold"))
        canvas.create_text((self.width) - 715, self.height//2 + 231, text = "Patricia", font = ("Comic Sans MS", 25, "bold"))
        canvas.create_text((self.width) - 520, self.height//2 + 231, text = "Megan", font = ("Comic Sans MS", 25, "bold"))
        canvas.create_text((self.width) - 320, self.height//2 + 231, text = "Katrina", font = ("Comic Sans MS", 25, "bold"))
        canvas.create_text(877.5, self.height//2 + 231, text = "Jared", font = ("Comic Sans MS", 25, "bold"))
        
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "EXIT", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
                           
class Recipe(object):
    def __init__(self, width, height, char, name):
        self.width = width
        self.height = height
        self.char = char
        self.apples = 10
        self.name = name
        self.coord = []
        self.food = ["flour", "sugar", "salt", "butter", "egg", "lemon", "apples", "sugar2", "butter2", "cinn"]
        
        self.flour = []
        self.flourClick = []
    
    def stepOne(self, canvas):
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "EXIT", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
                           
        canvas.create_text(self.width // 2, self.height//4 - 100, text = "%s wants to bake an apple pie! \n Click the recipe below to help." % (self.name), font = ("Comic Sans MS", 40, "bold"), justify = CENTER)
        #character images from https://www.alimcjoy.com/alissa-mcclure/how-to-talk-with-kids-about-race/
        imagePeople = PhotoImage(file='images/story/%d.png' % self.char)
        label = Label(image=imagePeople)
        label.image = imagePeople
        canvas.create_image(self.width//4, self.height//2, image = imagePeople)
        
        #https://www.123rf.com/clipart-vector/recipe.html?sti=n9xrtt2p8gaqhbzwg4|
        imageRec = PhotoImage(file='images/story/recipe.png')
        label = Label(image=imageRec)
        label.image = imageRec
        canvas.create_image(3 * self.width //4, self.height //2, image = imageRec)
        canvas.create_rectangle(3 * self.width //4 - 94, self.height //2 - 112, 3 * self.width //4 + 94,self.height //2 + 112)
        
        #http://diysolarpanelsv.com/apple-clipart-for-silhouette.html
        imageApple = PhotoImage(file='images/story/apple.png')
        label = Label(image=imageApple)
        label.image = imageApple
        x = 70
        for i in range(self.apples):
            canvas.create_image(x, 3*self.height //4, image = imageApple)
            x += 90
    
    def stepTwo(self, canvas):
        #edited original recipe image 
        imageRec = PhotoImage(file='images/story/recIng.png')
        label = Label(image=imageRec)
        label.image = imageRec
        canvas.create_image(self.width //2, self.height //2 + 50, image = imageRec)
        canvas.create_text(self.width//2, 80, text = "Help %s measure the ingredients \n by clicking on the box next to the ingredient." % self.name, justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
        
    def drawBoxes(self, canvas, listBox):
        count = 0
        for (x0,y0,x1,y1,check) in listBox:
            canvas.create_rectangle(x0, y0, x1, y1, width = 2)
            if check == True:
                count += 1
                canvas.create_rectangle(x0, y0, x1, y1, width = 2, fill = "green")
        if count == 10:
            canvas.create_rectangle(0,0,self.width,self.height, fill = "white", outline = "sky blue")
            canvas.create_text(self.width//2, self.height//3, text = "Good job! \n %s was able to bake the \n perfect apple pie \n thanks to your help!" % self.name, justify = CENTER, font = ("Comic Sans MS", 50, "bold"))
            
            #http://worldartsme.com/smelling-apple-pie-clipart.html#gal_post_18232_smelling-apple-pie-clipart-1.jpg
            image = PhotoImage(fil = 'images/story/pie.png')
            label = Label(image=image)
            label.image = image
            canvas.create_image (self.width //2, 3 * self.height//4, image = image)
            
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "EXIT", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
                
        
            
    def returnCoord(self):
        return self.coord
    
    def returnFoodCoord(self, index):
        if index == 0:
            return self.flourClick
    
    def makeFood(self, canvas, index, flourC, sugarSPC, recList, eggList, lemList, drawNumber, s2Coord):
        item = self.food[index]
        if item == "flour":
            canvas.create_text(self.width//2, 80, text = "We need 2 1/2 cups of flour. \n Click on a cup to pour in 1/4 cup of flour.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawFlour(self, canvas, flourC)
        elif item == "sugar":
            canvas.create_text(self.width//2, 80, text = "We need 4 teaspoons of sugar. \n Click on a spoon to fill it up.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawSugarSP(self, canvas, sugarSPC)
        elif item == "salt":
            canvas.create_text(self.width//2, 80, text = "We need 1/4 teaspoons of salt. \n Click on the circle that is 1/4 green.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawSaltCircles(self, canvas, recList)
        elif item == "butter":
            canvas.create_text(self.width//2, 80, text = "We need 14 tablespoons of butter. \n Click on the equation that equals 14.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawQuestions14(self, canvas, recList)
        elif item == "egg": 
            canvas.create_text(self.width//2, 80, text = "We need 2 eggs. \n Click on the eggs to crack them.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawEggs(self, canvas, eggList)
        elif item == "lemon":
            canvas.create_text(self.width//2, 80, text = "We need 2 tablespoons of sugar. \n Click on a spoon to fill it up.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawTB(self, canvas, lemList)
        elif item == "apples":
            canvas.create_text(self.width//2, 80, text = "We need 9 apples. \n Click on the equation that equals 9.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawQuestions9(self,canvas,recList)
        elif item == "sugar2":
            canvas.create_text(self.width//2, 80, text = "We need 2/3 cup of sugar. \n Click on a cup to pour in 1/3 cup of flour.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawSug2(self, canvas, s2Coord)
        elif item == "butter2":
            canvas.create_text(self.width//2, 80, text = "We need 1/8 cup of butter. \n Click on the circle that is 1/8 green.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawButterCircles(self,canvas,recList)
        elif item == "cinn":
            canvas.create_text(self.width//2, 80, text = "We need 1/4 teaspoon cinnamon. \n What is 1/4 as a decimal? \n Type in your answer.", justify = CENTER, font = ("Comic Sans MS", 30, "bold"))
            Recipe.drawCinn(self, canvas, drawNumber)
            
        margin = 15
        x0 = margin
        x1 = margin + 120
        y0 = 10
        y1 = 60
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "IndianRed1", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "BACK", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
    
    def drawSug2(self, canvas, s2Coord):
        #edited https://www.istockphoto.com/ca/illustrations/measuring-cup multiple times
        imageCup0 = PhotoImage(file='images/story/emptMC.png')
        label = Label(image=imageCup0)
        label.image = imageCup0
        
        imageCup13 = PhotoImage(file='images/story/13MC.png')
        label = Label(image=imageCup13)
        label.image = imageCup13
        
        imageCup23 = PhotoImage(file='images/story/23MC.png')
        label = Label(image=imageCup23)
        label.image = imageCup23
    
        imageCup44 = PhotoImage(file='images/story/fullMC.png')
        label = Label(image=imageCup44)
        label.image = imageCup44
        
        for cups in range(len(s2Coord)):
            (x0, y0, x1, y1, im) = s2Coord[cups]
            x = (x0 + x1) //2
            y = (y0 + y1)//2
            if im == 0:
                canvas.create_image(x, y, image = imageCup0)
            elif im == 1:
                canvas.create_image(x, y, image = imageCup13)
            elif im == 2:
                canvas.create_image(x, y, image = imageCup23)
            elif im == 3:
                canvas.create_image(x, y, image = imageCup44)
            canvas.create_rectangle(x0,y0,x1,y1)
        
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
        
        #enter answer    
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = self.height - 10
        y1 = self.height - 60 
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "sky blue", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "ENTER", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
                           
    
    def drawFlour(self, canvas, flourC):
        #edited https://www.istockphoto.com/ca/illustrations/measuring-cup myself
        imageCup0 = PhotoImage(file='images/story/emptMC.png')
        label = Label(image=imageCup0)
        label.image = imageCup0
        
        imageCup14 = PhotoImage(file='images/story/14MC.png')
        label = Label(image=imageCup14)
        label.image = imageCup14
        
        imageCup12 = PhotoImage(file='images/story/12MC.png')
        label = Label(image=imageCup12)
        label.image = imageCup12
        
        imageCup34 = PhotoImage(file='images/story/34MC.png')
        label = Label(image=imageCup34)
        label.image = imageCup34
        
        imageCup44 = PhotoImage(file='images/story/fullMC.png')
        label = Label(image=imageCup44)
        label.image = imageCup44
    
        for cups in range(len(flourC)):
            (x0, y0, x1, y1, im) = flourC[cups]
            x = (x0 + x1) //2
            y = (y0 + y1)//2
            if im == 0:
                canvas.create_image(x, y, image = imageCup0)
            elif im == 1:
                canvas.create_image(x, y, image = imageCup14)
            elif im == 2:
                canvas.create_image(x, y, image = imageCup12)
            elif im == 3:
                canvas.create_image(x, y, image = imageCup34)
            elif im == 4:
                canvas.create_image(x, y, image = imageCup44)
            canvas.create_rectangle(x0,y0,x1,y1)
        
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
        
        #enter answer    
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = self.height - 10
        y1 = self.height - 60 
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "sky blue", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "ENTER", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
                           
                           
    def drawSugarSP(self, canvas, sugL):
        #edited https://www.shutterstock.com/search/teaspoon
        imageEmp = PhotoImage(file='images/story/emptSP.png')
        label = Label(image=imageEmp)
        label.image = imageEmp
        
        imageFull = PhotoImage(file='images/story/fullSP.png')
        label = Label(image=imageFull)
        label.image = imageFull
        
        for (x0,y0,empt) in sugL:
            if empt == True:
                canvas.create_image(x0,y0,image = imageEmp)
            elif empt == False:
                canvas.create_image(x0,y0,image = imageFull)
            canvas.create_rectangle(x0 - 314//2, y0 - 128//2, x0 + 314//2, y0 + 128//2)

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
        
        #enter answer    
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = self.height - 10
        y1 = self.height - 60 
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "sky blue", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "ENTER", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
        
    def drawSaltCircles(self, canvas, recList):
        #https://commons.wikimedia.org/wiki/File:Fraction_Circles_Shaded.png
        image = PhotoImage(file='images/story/circFrac.png')
        label = Label(image=image)
        label.image = image
        canvas.create_image(self.width//2, self.height//2, image = image)
        
        for (x0,y0,x1,y1) in recList:
            canvas.create_rectangle(x0,y0,x1,y1)
            
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
        
    def drawQuestions14(self, canvas, recList):
        #made image 
        image = PhotoImage(file='images/story/14qs.png')
        label = Label(image=image)
        label.image = image
        canvas.create_image(self.width//2, self.height//2, image = image)
        
        for (x0,y0,x1,y1) in recList:
            canvas.create_rectangle(x0,y0,x1,y1)
            
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
                               
    def drawEggs(self, canvas, eggList):
        #https://www.graphicsfuel.com/2011/01/broken-egg-psd-download/
        egg = PhotoImage(file='images/story/egg.png')
        label = Label(image=egg)
        label.image = egg
        
        #https://www.kisspng.com/png-chicken-eggshell-clip-art-crack-704509/preview.html
        Cregg = PhotoImage(file='images/story/cracked.png')
        label = Label(image=Cregg)
        label.image = Cregg

        for (x,y,crack) in eggList:
            if crack == False:
                canvas.create_image(x,y,image = egg)
            elif crack == True:
                canvas.create_image(x,y,image = Cregg)
            canvas.create_rectangle(x - 100, y - 192//2, x + 100, y + 192//2)
            
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
        
        #enter answer    
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = self.height - 10
        y1 = self.height - 60 
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "sky blue", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "ENTER", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
    
    def drawTB(self, canvas, lemL):
        #edited https://www.abcteach.com/documents/clip-art-measuring-spoons-teaspoon-coloring-page-i-abcteachcom-45632
        imageEmp = PhotoImage(file='images/story/emptTB.png')
        label = Label(image=imageEmp)
        label.image = imageEmp
        
        imageFull = PhotoImage(file='images/story/lemTB.png')
        label = Label(image=imageFull)
        label.image = imageFull
        
        for (x0,y0,empt) in lemL:
            if empt == True:
                canvas.create_image(x0,y0,image = imageEmp)
            elif empt == False:
                canvas.create_image(x0,y0,image = imageFull)
            canvas.create_rectangle(x0 - 305//2, y0 - 100//2, x0 + 305//2, y0 + 100//2)

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
        
        #enter answer    
        margin = 15
        x0 = self.width - margin - 120
        x1 = self.width - margin
        y0 = self.height - 10
        y1 = self.height - 60 
        canvas.create_rectangle(x0, y0, x1, y1, 
                                fill = "sky blue", outline = "white")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text = "ENTER", 
                           fill = "white", font = ("Comic Sans MS", 20, "bold"))
    
    def drawButterCircles(self,canvas,recList):
        #https://commons.wikimedia.org/wiki/File:Fraction_Circles_Shaded.png
        image = PhotoImage(file='images/story/circFrac.png')
        label = Label(image=image)
        label.image = image
        canvas.create_image(self.width//2, self.height//2, image = image)
        
        for (x0,y0,x1,y1) in recList:
            canvas.create_rectangle(x0,y0,x1,y1)
            
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
                           
    def drawQuestions9(self,canvas,recList):
        #made myself
        image = PhotoImage(file='images/story/9qs.png')
        label = Label(image=image)
        label.image = image
        canvas.create_image(self.width//2, self.height//2, image = image)
        
        for (x0,y0,x1,y1) in recList:
            canvas.create_rectangle(x0,y0,x1,y1)
            
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
    
    def drawCinn(self, canvas, drawNum):
        canvas.create_rectangle(self.width//2 - 200, self.height //2 - 100, self.width//2 + 200, self.height//2 + 100, fill = "light pink")
        canvas.create_text(self.width//2, self.height//2, text = drawNum, font = ("Comic Sans MS", 50, "bold"))
                
