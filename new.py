from tkinter import *
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os.path



root=Tk()
def clicked():
    try:
        if os.path.exists("empsal.csv"):
            
            df=pd.read_csv("empsal.csv")
            x=df['expyr']
            y=df['salary']
            xmat=x.values.reshape(-1,1)
            reg=LinearRegression()
            reg.fit(xmat,y)
            
            new_expr = DoubleVar()
            new_expr = float(en.get())
            new_expr = [[new_expr]]  # Converting the input in 2D
            prediction = reg.predict(new_expr)# prediction is numpy ndarray. Need to access 0th element
            prediction = ("%.2f" % prediction[0])  # 
            lu=Label(root,text="Salary is "+ str(prediction))
            lu.grid(row=3,column=3)
    except  FileNotFoundError as e:
        print("Djeje")

def dee():
    root.quit()

lb=Label(root,text="Predict Salary given Experience in years")
Btclick=Button(root,text="Predict Salary Expected",bg="orange",command=clicked)
Btquit=Button(root,text="Exit",bg="orange",command=dee)
lb2=Label(root,text="Enter Experience in years: ")
en=Entry(root,width=30)

lb.grid(row=0,column=3)
Btclick.grid(row=1,column=3)
Btquit.grid(row=1,column=5)
lb2.grid(row=2,column=3)
en.grid(row=2,column=4)






root.mainloop()
