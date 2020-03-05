from tkinter import *
global M,G,CH,Total

def on():
    global M,G,CH,Total
    Total=0
    CH=0
    M=0
    G=0
    l1=Label(ventana,text=CH).grid(column=0,row=2)
    l2=Label(ventana,text=M).grid(column=1,row=2)
    l3=Label(ventana,text=G).grid(column=2,row=2)
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
def small():
    global CH

    CH=CH+1
    l1=Label(ventana,text=CH,bg="yellow",font="Arial 12").grid(column=0,row=2)
    
def medium():
    global M
    M=M+1
    l2=Label(ventana,text=M,bg="blue",font="Arial 12").grid(column=1,row=2)
    
def big():
    global G
    G=G+1
    l3=Label(ventana,text=G,bg="yellow",font="Arial 12").grid(column=2,row=2)

def off():
    global M,G,CH,Total
    Total=0
    CH=0
    M=0
    G=0
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
ventana=Tk()
ventana.config(width=600, height=800)
b0=Button(ventana,text="ON",bg="Green",font="Arial 12",command=on, width=8, height=3)
b0.grid(column=0, row=0)

b1=Button(ventana,text="SMALL",bg="Blue",font="Arial 12",command=small,width=8, height=3)
b1.grid(column=0,row=1)

b2=Button(ventana,text="MEDIUM",bg="Yellow",font="Arial 12",command=medium,width=8, height=3)
b2.grid(column=1,row=1)

b3=Button(ventana,text="BIG",bg="Blue",font="Arial 12",command=big,width=8, height=3)
b3.grid(column=2,row=1)
b4=Button(ventana,text="OFF",bg="RED",font="Arial 12",command=off,width=8, height=3) 
b4.grid(column=1,row=0)
b1.config(state=DISABLED)
b2.config(state=DISABLED)
b3.config(state=DISABLED)
