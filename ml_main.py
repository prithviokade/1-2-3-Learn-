#Austin's module manager
import module_manager
module_manager.review()

from sklearn import svm
from sklearn import datasets

from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset modified from http://deeplearning.net/tutorial/gettingstarted.html
import _pickle as p
import gzip

# adjustments made with help from 
# https://stackoverflow.com/questions/11305790/pickle-incompatibility-of-numpy-arrays-between-python-2-and-3


class Classif(object):
    def __init__(self):
        self.classif = svm.SVC(gamma='scale')
    
    #trains the classifier   
    def train(self):
        file = gzip.open('mnist.pkl.gz', 'rb')
        trainSet, validSet, testSet = p.load(file, encoding = 'iso-8859-1')
        file.close()
        
        trainSetD, trainSetT = trainSet #trainSetData, trainSetTarget
        
        self.classif.fit(trainSetD[:10000], trainSetT[:10000])
        # classif.fit(trainSetD[10001:15000], trainSetT[10001:15000])
        # classif.fit(trainSetD[15001:20000], trainSetT[15001:20000])

    #makes image small
    def resizeImage(self, img, Vsize):
        (x,y) = img.size
        ratio = Vsize / y
        img = img.resize((int(x * ratio), int(y * ratio)))
        return img

    #saves new image
    def saveImage(self, path, size, img):
        if path == None and size == None:
            img.save("num", "png")
        else: 
            img = resizeImage(path, size)
            filename = path.split(".")[0]
            img.save(filename, "png")

    #makes image grey
    #calculation formula: 
    #https://stackoverflow.com/questions/41971663/use-numpy-to-convert-rgb-pixel-array-into-grayscale
    def shiftColor(self,imread):
        return np.dot(imread[...,:3], [0.299, 0.587, 0.114])

    def centerImage(self, pix, img, expected):
        color = "white"
        bkg = Image.new(img.mode, (28,28), color)
        
        (x,y) = img.size
        
        # from PIL documentation http://effbot.org/imagingbook/image.htm
        if expected == [7]:
            bkg.paste(img, (14 - x//2, 8))
        elif expected == [9]:
            bkg.paste(img, (14 - x//2, 6))
        else:
            bkg.paste(img, (14 - x//2, 4))
        
        Classif.saveImage(self, None, None, bkg)
        return bkg
     
    #crops out whitespace
    def crop(self, path):
        img = Image.open(path)
        
        (x,y) = img.size
        color = "white"
        mode = img.mode
        backgroundImg = Image.new(mode, (x,y), color)
    
        #ImageChops documentation https://pillow.readthedocs.io/en/3.1.x/reference/ImageChops.html
        invert = ImageChops.difference(img, backgroundImg)
        foreground = invert.getbbox()
        newImg = img.crop(foreground)
        
        size = 20
        newImg = Classif.resizeImage(self, newImg, 20)
        return newImg

    #returns classifier-readable data
    def greyData(self, path, expected):
        img = Classif.crop(self, path)
        
        img2 = plt.imread("num.test.png")
        greyImg = Classif.shiftColor(self, img2)
        pix = (1 - (greyImg // 255)).astype(int)
        
        perfImg = Classif.centerImage(self, pix, img, expected)
        
        perfImg2 = plt.imread("num")
        greyImg2 = Classif.shiftColor(self, perfImg2)
        perfPix = (1 - (greyImg2 // 255)).astype(int)
        #print(perfPix)
        #this prints the 28 x 28 pixel concentration matrix, just to better visualize the image
        
        return perfPix
        
    def predict(self, path, expected):
        pix = Classif.greyData(self,path, expected)
        IM = pix.flatten().reshape(1,-1)
        
        predicted = self.classif.predict(IM)
        return predicted
        
