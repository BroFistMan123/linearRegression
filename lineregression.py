# -*- coding: utf-8 -*-
"""LineRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jq3SspDotNVJu1HFT0UTf_bn8j8K9brw
"""

import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
class LinearRegression:

  def __init__(self, data):
    self.data = data
    self.yInt=0
    self.slope=0
    self.mean=()
    
  

  def printGraph(self,datapoint):
    originalPt=self.data
    x_val = [x[0] for x in datapoint]
    y_val = [x[1] for x in datapoint]
    origX=[x[0] for x in originalPt]
    origY=[x[1] for x in originalPt]
    plt.plot(origX,origY,'ob')
    
    plt.plot(x_val,y_val)
    plt.plot(x_val,y_val,'or')
    plt.show()
  def tableFormat(self,dataset):
    t = PrettyTable(['X', 'Y'])
    for i in range(len(dataset)):
      t.add_row([dataset[i][0],dataset[i][1]])
    return t
    
  def getMean(self):
    data=self.data
    xSum=0
    ySum=0
    for i in range(len(data)):
      xSum+=data[i][0]
     
      ySum+=data[i][1]
    xDiv=xSum/len(data)
    yDiv=ySum/len(data)
    
    self.mean=(xDiv,yDiv)

    return self.mean
  def getSlope(self):
    data=self.data
    numerator=0
    denominator=0
    for i in range(len(data)):
      numerator+=(data[i][0]-self.mean[0])*(data[i][1]-self.mean[1])
      denominator+=(data[i][0]-self.mean[0])**2
    self.slope=(numerator/denominator)
    return self.slope
  def getyInt(self):
    b=self.mean[1]-(self.slope*self.mean[0])
    self.yInt=b
    return self.yInt
  def predictValues(self,trainSet):
    predVal=[]
    for i in range(len(trainSet)):
      y=(self.slope*trainSet[i])+self.yInt
      predVal.append((trainSet[i],y))
    
    return predVal
  def runRegression(self):
    print("Given Training Datasets:",self.data)
    print("Mean:", self.getMean())
    print("Slope:",self.getSlope())
    print("Y-Intercept:",self.getyInt())
  def getPercent(self, dataset):
    origY=self.data
    yMean=self.mean
    numerator=0
    denominator=0
    for i in range(len(dataset)):
      numerator+=(origY[i][1]-dataset[i][1])**2
      denominator+=(origY[i][1]-yMean[1])**2
    r=1-(numerator/denominator)
    return r
    

    # return (x,y)
#GENERATING INPUT METHOD
# input_list=[]
# for i in range(100):
#   input_list.append((i,i+3))
# tupleA=tuple(input_list)
  


#DECLARED TUPLE METHOD
tupleA=((1,3),(2,4),(3,2),(4,4),(5,5))
p1=LinearRegression(tupleA)
print(p1.tableFormat(p1.data))
p1.runRegression()
trainingSet=[1,2,3,4,5]
dataset=p1.predictValues(trainingSet)
print("Dataset for Predicted Values: ",dataset)
p1.printGraph(dataset)
p1.getPercent(dataset)

data =  [(1, 2), (2, 4),
 (3, 6), (4,8),
 (5, 10), (6, 12)]
x_val = []
# x_val = [x[0] for x in data]
# y_val = [x[1] for x in data]
y_val = []

for x in data:
  print(x[0])
  x_val.append(x[0])

for x in data:
  print(x[1])
  y_val.append(x[1])
print (x_val)
print (y_val)
plt.plot(x_val,y_val)
plt.plot(x_val,y_val,'or')
plt.show()

from prettytable import PrettyTable
t = PrettyTable(['Name', 'Age'])
t.add_row(['Alice', 24])
t.add_row(['Bob', 19])
print(t)

#CSV implementation
import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("/content/movie_metadata.csv") 
# Preview the first 5 lines of the loaded data 
datasets=[]
# for row in data.itertuples():

  # if row['z']==nan or row['y']==nan or row['x']==nan:
  #   continue
  # print(row)
  # print(row[0],row[1],row[2],row[3])
  # datasets.append((row['x'],row['y'],row['z']))

def getCSV(data,x,y,columnname): 
  datalist={}                 #expects a string param
  xCol=data.columns.get_loc(x)+1
  yCol=data.columns.get_loc(y)+1  #I plus one kay murag sa 1 mag sugod ang table pag update sa itertuple.

  zCol=data.columns.get_loc(columnname)+1
  
  # print("location x: ",xCol,"location y: ",yCol,"location z: ",zCol)
  
  for row in data.itertuples():
    
    datalist.update({row[zCol]:(row[xCol],row[yCol])})
  print(datalist)

data = data.dropna(how='any',axis=0) 
getCSV(data,"gross","budget","movie_title")

