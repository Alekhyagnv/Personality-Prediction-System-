# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:58:47 2020

@author: saikumar
"""

import tkinter as tk
from tkinter.ttk import *
import csv
import pandas as pd
from numpy import *
import numpy as np
from sklearn import preprocessing
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import neighbors

def test():
    data =pd.read_csv('train dataset.csv')
    array = data.values
    for i in range(len(array)):
        if array[i][0]=="Male":
            array[i][0]=1
        else:
            array[i][0]=0
    
    df=pd.DataFrame(array)
    maindf =df[[0,1,2,3,4,5,6]]
    mainarray=maindf.values
    print (mainarray)
    temp=df[7]
    train_y =temp.values
    train_y=temp.values
    for i in range(len(train_y)):
        train_y[i] =str(train_y[i])
    mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
    mul_lr.fit(mainarray, train_y)
    testdata =pd.read_csv('test.csv')
    test = testdata.values
    for i in range(len(test)):
        if test[i][0]=="Male":
            test[i][0]=1
        else:
            test[i][0]=0
    df1=pd.DataFrame(test)
    testdf =df1[[0,1,2,3,4,5,6]]
    maintestarray=testdf.values
    print(maintestarray)
    y_pred = mul_lr.predict(maintestarray)
    for i in range(len(y_pred)) :
        y_pred[i]=str((y_pred[i]))
    DF = pd.DataFrame(y_pred,columns=['Predicted Personality'])
    DF.index=DF.index+1
    DF.index.names = ['Person No']
    DF.to_csv("output.csv")



    

def save_csv():
    v1=r1.get()
    v2=r2.get()
    v3=r3.get()
    v4=r4.get()
    v5=r5.get()
    v6=r6.get()
    v7=r7.get()
    fields = ["Gender","Age","openness","neuroticism","conscientiousness","agreeableness","extraversion"]
    with open('test.csv','w+') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerow([v1,v2,v3,v4,v5,v6,v7])
        
    test()
    
    with open("output.csv") as f:
        reader=csv.reader(f)
        
        for row in reader:
            w["text"]=row[1]
            print(row[1])
            
            
data =pd.read_csv('train dataset.csv')
array = data.values

master = tk.Tk()
master.geometry('300x300')
style = Style()
style.configure("Sbutton",font = ('calibri',20, 'bold'), borderwidth= '4')
style.map('Sbutton',foreground=[('active','!disabled','green')],background=[('active','black')])
r1 = tk.StringVar(master)
r1.set("Male")
r2 = tk.StringVar(master)
r2.set("15")
r3 = tk.StringVar(master)
r3.set("1")
r4 = tk.StringVar(master)
r4.set("1")
r5 = tk.StringVar(master)
r5.set("1")
r6 = tk.StringVar(master)
r6.set("1")
r7 = tk.StringVar(master)
r7.set("1")
#v = OptionMenu(master, v, "Male", "Female").grid(row=0)
l=Label(master,text="").grid(row=0)
l8=Label(master,text="").grid(row=1)
l1=Label(master, text="               Gender                       :     ").grid(row=4)
l2=Label(master, text="               Age                            :     ").grid(row=5)
l3=Label(master, text="               openness                   :     ").grid(row=6)
l4=Label(master, text="               neuroticism               :     ").grid(row=7)
l5=Label(master, text="               conscientiousness      :     ").grid(row=8)
l6=Label(master, text="               agreeableness             :     ").grid(row=9)
l7=Label(master, text="               extraversion                :     ").grid(row=10)
w=tk.Label(master, text="output",fg="green", font = ("Helvetica",12, "bold"))
w.grid(row=14, sticky="E")

h1 = OptionMenu(master, r1, "Male", "Male","Female")
h2 = OptionMenu(master, r2, "15","15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
h3 = OptionMenu(master, r3, "1","1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
h4 = OptionMenu(master, r4, "1","1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
h5 = OptionMenu(master, r5, "1","1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
h6 = OptionMenu(master, r6, "1", "1","2", "3", "4", "5", "6", "7", "8", "9", "10")
h7 = OptionMenu(master, r7, "1", "1","2", "3", "4", "5", "6", "7", "8", "9", "10")
e8 = Entry(master)

h1.grid(row=4, column=1)
h2.grid(row=5, column=1)
h3.grid(row=6, column=1)
h4.grid(row=7, column=1)
h5.grid(row=8, column=1)
h6.grid(row=9, column=1)
h7.grid(row=10, column=1)


b1=Label(master,text="").grid(row=11)
b = Button(master, text='Show', command=save_csv).grid(row=12,sticky="E")
b2=Label(master,text="").grid(row=13)

master.mainloop()