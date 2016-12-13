# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter

"""
i = Image.open('images/numbers/0.1.png')
iar = np.asarray(i) #3d Array
#whole array is the image, broken down into rows which are pixels,
#and each number in the rows correspond to RGB
print('')
plt.imshow(iar)
plt.show
"""
def createExamples():
    numberArrayExamples = open('numArrayEx.txt','a')
    numWeHave = range(0,10)
    versionWeHave = range(1,10)
    
    for eachNum in numWeHave:
        for eachVer in versionWeHave:
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVer) + '.png'
            #imgFilePath = 'images/sign.png'
            exImage = Image.open(imgFilePath)
            exImageArray = np.array(exImage)
            exImageArray1 = str(exImageArray.tolist())
            lineToWrite = str(eachNum) + '::' + exImageArray1+'\n'
            numberArrayExamples.write(lineToWrite)

def threshold (imageArray): #function that makes the image pure black and white
    balanceArray = []# find the average colour of the image, and anything above it will be white, anything below will be black
    newArray = imageArray
    for eachRow in imageArray:
        for eachPixel in eachRow:
            avgNum = reduce(lambda x, y: x+y, eachPixel[:3])/len(eachPixel[:3])
            balanceArray.append(avgNum)
    balance = reduce(lambda x, y: x+y, balanceArray)/len(balanceArray)
   
    eachPixel.flags.writeable = True
    for eachRow in newArray:
        for eachPixel in eachRow:
            if (reduce(lambda x, y: x+y, eachPixel[:3])/len(eachPixel[:3]) > balance):
                eachPixel[0] = 255
                eachPixel[1] = 255
                eachPixel[2] = 255
                eachPixel[3] = 255

            else:
                eachPixel[0] = 0
                eachPixel[1] = 0
                eachPixel[2] = 0
                eachPixel[3] = 255
    
    return newArray

def Compare(blackAndWhiteArray,filePath):
    matchedArray = 0
    matchedArray = []
    loadExamples = open('numArrayEx.txt','r').read()
    loadExamples = loadExamples.split('\n')
    picture = Image.open(filePath)
    imageArray = blackAndWhiteArray #3d Array
    imageArrayLoad = imageArray.tolist()
    
    inQuestion = str(imageArrayLoad)
    for eachExample in loadExamples:
        if len(eachExample) > 3:
            splitExample = eachExample.split('::')
            currentNum = splitExample[0]
            currentArray = splitExample[1]
            
            eachPixelExample = currentArray.split('],')
            eachPixelInQ = inQuestion.split('],')
            x = 0
            while x < len(eachPixelExample):
                if eachPixelExample[x] == eachPixelInQ[x]:
                    matchedArray.append(int(currentNum))
                x += 1
    
    x = Counter(matchedArray)
    print x
    graphX = []
    graphY = [] 
    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
    
    fig = plt.figure() 
    ax = plt.subplot2grid((10,10),(0,0), rowspan = 2, colspan = 10)
    barChart = plt.subplot2grid((10,10),(3,0), rowspan = 7, colspan = 10)
    
    ax.imshow(imageArray)
    barChart.bar(graphX, graphY, align = 'center')
    plt.ylim(400)
    xloc = plt.MaxNLocator(12)
    barChart.xaxis.set_major_locator(xloc)
    
    plt.show()
    
filePath = 'images/testpic7.png'
picture = Image.open(filePath)
imageArray = np.array(picture)

createExamples()
    
blackAndWhiteArray = threshold(imageArray)
fig = plt.figure() 
ax = plt.subplot2grid((8,6),(0,0), rowspan = 4, colspan = 4)
ax.imshow(imageArray)
plt.show()

Compare(blackAndWhiteArray,filePath)



