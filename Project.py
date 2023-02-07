# libraries used
import os
from re import L
from tkinter import *
from turtle import bgcolor
from typing_extensions import Self
from PIL import ImageTk,Image
from tkinter import ttk

from pyparsing import col


# function to display code
def last():
    f=open("main.cpp","r+")
    data1=f.read()
    
    cpp=Label(area2,width=398,height=800,bg='white',font=('Helvetica',12),text=data1,justify='left')
    cpp.pack(side='left',anchor='nw',fill='both')

# function to pass to compiler
def start(data):
    global ROW1

    st3=Canvas(area1,width=y,height=40,bg="white",highlightthickness=0)
    st3.grid(row=ROW1,column=0,columnspan=8)

    st3.create_oval(y//2-60,5,y//2+60,30,fill="#83f28f")
    st3.create_text(y//2,18,text= "END" )

    file = open("main.cpp","w")
    file.write("#include <iostream>\n#include <stdlib.h>\nusing namespace std;\n\nint main() {\n\n")

    for i in data:
        i.parse(file)

    file.write('\nreturn 0;\n\n}')
    file.close()

    os.system("g++ -o main main.cpp")
    os.system("main")

    last()
    
# global variables
global x
global y
global z
global ROW1
global COL1
global n

# intial values of global variables
x=600
y=600
z=8
ROW1=2
COL1=0
n=1


g=open("numbers.txt","r")
data2=g.read()


# mouse dragging functions
def move(event):
    co.config(text="( x :" + str(event.x) + " y :" + str(event.y) + " )")

# keyboard key functions
def U1(event):
    global ROW1
    global COL1
    ROW1+=-1
    pos.config(text="(" + str(ROW1) + ":" +str(COL1)+")")
    
def D1(event):
    global ROW1
    global COL1

    ROW1+=1
    pos.config(text="(" + str(ROW1) + ":" +str(COL1)+")")
    
def R1(event):
    global ROW1
    global COL1
    
    if(COL1==7):
        COL1=0
    else:
        COL1+=1
    pos.config(text="(" + str(ROW1) + ":" +str(COL1)+")")
    
def L1(event):
    global ROW1
    global COL1
    
    if(COL1==0):
        COL1=7
    else:
        COL1-=1
    pos.config(text="(" + str(ROW1) + ":" +str(COL1)+")")
    
# list for inputting objects of all classes
source = []

# clear function to clean the canvas
def CLEAR():

    global y
    global z
   
    for widgets in area1.winfo_children():
      widgets.destroy()

    for widget in area2.winfo_children():
      widget.destroy()

    r1=Canvas(area1,width=75,height=15,bg="#E5BEED",highlightthickness=0)
    r1.grid(row=0,column=0)
    r1.create_text(35,7,text='0')
    r2=Canvas(area1,width=75,height=15,bg="white",highlightthickness=0)
    r2.grid(row=0,column=1)
    r2.create_text(35,7,text='1')
    r3=Canvas(area1,width=75,height=15,bg="#E5BEED",highlightthickness=0)
    r3.grid(row=0,column=2)
    r3.create_text(35,7,text='2')
    r4=Canvas(area1,width=75,height=15,bg="white",highlightthickness=0)
    r4.grid(row=0,column=3)
    r4.create_text(35,7,text='3')
    r5=Canvas(area1,width=75,height=15,bg="#E5BEED",highlightthickness=0)
    r5.grid(row=0,column=4)
    r5.create_text(35,7,text='4')
    r6=Canvas(area1,width=75,height=15,bg="white",highlightthickness=0)
    r6.grid(row=0,column=5)
    r6.create_text(35,7,text='5')
    r7=Canvas(area1,width=75,height=15,bg="#E5BEED",highlightthickness=0)
    r7.grid(row=0,column=6)
    r7.create_text(35,7,text='6')
    r8=Canvas(area1,width=75,height=15,bg="white",highlightthickness=0)
    r8.grid(row=0,column=7)
    r8.create_text(35,7,text='7')

    st2=Canvas(area1,width=y,height=40,bg="white",highlightthickness=0)
    st2.grid(row=1,column=0,columnspan=8)

    st2.create_oval(y//2-60,5,y//2+60,30,fill="#83f28f")
    st2.create_text(y//2,18,text= "START" )

    st2.create_line(y//2,30,y//2,40)
    st2.create_line(y//2,40,y//2-5,35)
    st2.create_line(y//2,40,y//2+5,35)

    num=Label(area2,width=2,height=800,bg='white',text=data2)
    num.pack(side='left',anchor='nw')

    source.clear()

# functions for in-out buttons
def M1():
    global x
    global y
    global z
    
    if(x<y):
        x=2*x
    inout.config(text=str(y//x))
    z=8//(y//x)

def M2():
    global x
    global y
    global z
    
    x=x//2
    inout.config(text=str(y//x))
    z=8//(y//x)

def A1():
    line1(area1)

def A2():
    line2(area1)

def A3():
    global n
    if(n==0):
        n=1
        forif.config(text=str(n))
    else:
        n=0
        forif.config(text=str(n))

# function to draw reverse line
class line1():

    global z
    global x
    global y
    global ROW1
    global COL1

    def __init__(self,master):
        self.canvas = Canvas(master,bg="white",width=x,height=40,highlightthickness=0,bd=0)
        self.canvas.grid(row=ROW1,column=COL1,columnspan=z)
        self.canvas.create_line(x//2,0,x//2,40)
        self.canvas.create_line(x//2,0,x//2-5,5)
        self.canvas.create_line(x//2,0,x//2+5,5) 

class line2():

    global z
    global x
    global y
    global ROW1
    global COL1

    def __init__(self,master):
        self.canvas = Canvas(master,bg="white",width=x,height=40,highlightthickness=0,bd=0)
        self.canvas.grid(row=ROW1,column=COL1,columnspan=z)
        self.canvas.create_line(x//2,0,x//2,40)
        self.canvas.create_line(x//2,40,x//2-5,35)
        self.canvas.create_line(x//2,40,x//2+5,35) 

# class for creating a variable of particular data type
class create:
    
    global x
    global y
    global z
    global ROW1
    global COL1
    
    def __init__(self,dtype,name,value=None):
        self.dtype = dtype
        self.name = name
        self.value = value
        self.canvas = None
    
    def draw(self,area):
        if(z==1):
            self.canvas = Canvas(area,width=x,height=40,bg="white",highlightthickness=0)
            self.canvas.grid(row=ROW1,column=COL1,columnspan=z)
            self.canvas.create_rectangle(x//2-30,0, x//2+30,30,fill="#7B9E89")
            self.canvas.create_text(x//2,15,text=str(self.name) +' = '+ str(self.value) )
            self.canvas.create_line(x//2,30,x//2,40)
            self.canvas.create_line(x//2,40,x//2-5,35)
            self.canvas.create_line(x//2,40,x//2+5,35)

        self.canvas = Canvas(area,width=x,height=40,bg="white",highlightthickness=0)
        self.canvas.grid(row=ROW1,column=COL1,columnspan=z)
        self.canvas.create_rectangle(x//2-60,0, x//2+60,30,fill="#7B9E89")
        self.canvas.create_text(x//2,15,text=str(self.name) +' = '+ str(self.value) )
        self.canvas.create_line(x//2,30,x//2,40)
        self.canvas.create_line(x//2,40,x//2-5,35)
        self.canvas.create_line(x//2,40,x//2+5,35)

    def parse(self,file):
        
        if self.value:
            file.write(f"{self.dtype} {self.name} = {self.value};\n")
        else:
            file.write(f"{self.dtype} {self.name};\n")

# class for assigning a variable a value
class assign:

    global x
    global y
    global z
    global ROW1
    global COL1
    
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.canvas = None

    def draw(self,area):
        self.canvas = Canvas(area,width=x,height=40,bg="white",highlightthickness=0)
        self.canvas.grid(row=ROW1,column=COL1,columnspan=z)
        self.canvas.create_rectangle(x//2-60,0,x//2+60,30,fill="#7B9E89")
        self.canvas.create_text(x//2,18,text=str(self.name) +' = '+ str(self.value) )
        self.canvas.create_line(x//2,30,x//2,40)
        self.canvas.create_line(x//2,40,x//2-5,35)
        self.canvas.create_line(x//2,40,x//2+5,35)

    def parse(self,file):
        file.write(f"{self.name} = {self.value};\n")

# class for displaying output
class output:

    global x
    global y
    global z
    global ROW1
    global COL1
    

    def __init__(self,value):
        self.value = value
        self.canvas = None
        

    def draw(self,area):
        self.canvas = Canvas(area,width=x,height=40,bg="white",highlightthickness=0)
        self.canvas.grid(row=ROW1,column=COL1,columnspan=z)
        self.canvas.create_polygon(x//2-30,1,x//2+60,1,x//2+30,30,x//2-60,30,fill='#9593D9',outline="black")
        self.canvas.create_text(x//2,18,text= str(self.value) )

        self.canvas.create_line(x//2+30,30,x//2+60,30)
        # self.canvas.create_line(x//2+25,30,x//2+55,25)
        # self.canvas.create_line(x//2+25,30,x//2+55,35)

        self.canvas.create_line(x//2,30,x//2,40)
        self.canvas.create_line(x//2,40,x//2-5,35)
        self.canvas.create_line(x//2,40,x//2+5,35)


    def parse(self,file):
        file.write(f"cout << {self.value} << endl;\n")

# class for inputting a value
class input:

    global x
    global y
    global z
    global ROW1
    global COL1


    def __init__(self,name):
        self.name = name

    def draw(self,area):
        self.canvas = Canvas(area,width=x,height=40,bg="white",highlightthickness=0)
        self.canvas.grid(row=ROW1,column=COL1,columnspan=z)
        self.canvas.create_polygon(x//2-30,1,x//2+60,1,x//2+30,30,x//2-60,30,fill='#9593D9',outline="black")
        self.canvas.create_text(x//2,18,text=" enter in " + str(self.name) )

        self.canvas.create_line(x//2-35,6,x//2-60,6)
        # self.canvas.create_line(x//2-60,6,30,x//2+55,1)
        # self.canvas.create_line(x//2-60,6,30,x//2+55,11)

        self.canvas.create_line(x//2,30,x//2,40)
        self.canvas.create_line(x//2,40,x//2-5,35)
        self.canvas.create_line(x//2,40,x//2+5,35)

    def parse(self,file):
        file.write(f"cin >> {self.name};\n")

# class for if and else condition
class _if:

    global x
    global y
    global z
    global ROW1
    global COL1

    
    def __init__(self,condition):

        self.condition = condition
        self.block = []
        self.eblock = []


    def draw(self,area):
        self.canvas = Canvas(area,width=x,height=40,bg="white",highlightthickness=0)
        self.canvas.grid(row=ROW1,column=COL1,columnspan=z)

        self.canvas.create_polygon(x//2-90,15,x//2,1,x//2+90,15,x//2,30,fill="#FFD449",outline="black")
        self.canvas.create_text(x//2,15,text= ' if ' + str(self.condition) )

        self.canvas.create_line(x//2,30,x//2,40)
        self.canvas.create_line(x//2,40,x//2-5,35)
        self.canvas.create_line(x//2,40,x//2+5,35)

    def parse(self,file):

        file.write(f"if ({self.condition}){{\n")
        for i in self.block: 
            i.parse(file)
            file.write("}\n")

        if self.eblock:
            file.write(f"else {{\n")
            for i in self.eblock: 
                i.parse(file)
            file.write("}\n")

# class for a while loop
class _while:

    global x
    global y
    global z
    global ROW1
    global COL1
    
    def __init__(self,condition):
        self.condition = condition
        self.block = []

    def draw(self,area):
        self.canvas = Canvas(area,width=x,height=40,bg="white",highlightthickness=0)
        self.canvas.grid(row=ROW1,column=COL1,columnspan=z)

        self.canvas.create_polygon(x//2-90,20,x//2,1,x//2+90,20,x//2,39,fill="cyan",outline="black")
        self.canvas.create_text(x//2,20,text= ' while ' + str(self.condition) )
        
        self.canvas.create_line(x//2-90,20, x//4,20)
        self.canvas.create_line(x//4,20, x//4,40)
        self.canvas.create_line(x//4,40, x//4-5,35)
        self.canvas.create_line(x//4,40, x//4+5,35)

        self.canvas.create_line(x//2+90,20, 3*x//4,20)
        self.canvas.create_line(3*x//4,20, 3*x//4,40)
        self.canvas.create_line(3*x//4,40, 3*x//4-5,35)
        self.canvas.create_line(3*x//4,40, 3*x//4+5,35)

        # self.canvas.create_line(x//2,30, x//2,40)
        # self.canvas.create_line(x//2,40, x//2-5,35)
        # self.canvas.create_line(x//2,40, x//2+5,35)

    def parse(self,file):
        file.write(f"while ({self.condition}){{\n")
        for i in self.block: 
            i.parse(file)
        file.write("}\n")

# class for a for loop
class _for:

    global x
    global y
    global ROW1
    global COL1
    
    def __init__(self,beg,end,step):
        self.beg = beg
        self.end = end
        self.step = step
        self.block = []

    def draw(self,area):
        self.canvas = Canvas(area,width=x,height=40,bg="white",highlightthickness=0)
        self.canvas.grid(row=ROW1,column=COL1,columnspan=z)
        self.canvas.create_text(x//2,18,text= f" from {self.beg} till {self.end} by {self.step} " )
        self.canvas.create_polygon(x//2-20,20,x//2,1,x//2+20,20,x//2,30,fill='#7D5C65')
        self.canvas.create_line(x//2,30,x//2,40)
        self.canvas.create_line(x//2,40,x//2-5,35)
        self.canvas.create_line(x//2,40,x//2+5,35)

    def parse(self,file):
        file.write(f"for (int i={self.beg}; i<={self.end}; i=i+{self.step}){{\n")
        for i in self.block: 
            i.parse(file)
        file.write("}\n")

# main window for diplaying program
main = Tk(None,None,'project',1)
main.state("zoomed")
main.config(bg="black")

# icon at the top
main.iconbitmap("2.ico")

# labelframe for placing program options
top=LabelFrame(main,text="options",bg="#7D5C65",padx=10,pady=10)
top.pack(side='top',anchor=NW,padx=5,pady=5,fill=X)

# labelframe for placing tools
tools=LabelFrame(main,bg="#736B92",text="tools",padx=10,pady=10)
tools.pack(side='left',anchor=NW,padx=5,pady=5,fill=Y)

# labelframe for displaying the flowchart  
graphic=LabelFrame(main,bg="#7C90DB",text="flowchart",padx=10,pady=10)
graphic.pack(side='left',padx=5,pady=5,anchor=NW)

# labelframe for displaying code
code=LabelFrame(main,bg="#7C90DB",text="code",padx=10,pady=10)
code.pack(side='right',padx=5,pady=5,anchor=NW)

# frame for displaying flowchart to create scrollbar
frame1= Frame(graphic,width=620,height=800)
frame1.pack(fill='both',expand=1)

# frame for displaying code to create scrollbar
frame2= Frame(code,width=420,height=800)
frame2.pack(fill='both',expand=1)

# canvas for displaying flowchart to create scrollbar
canvas1=Canvas(frame1,width=620,height=800,bg='white')
canvas1.pack(side='left',fill='both',expand=1,padx=0,pady=0)

# canvas for displaying flowchart to create scrollbar
canvas2=Canvas(frame2,width=420,height=800)
canvas2.pack(side='left',fill='both',expand=1)

# scrollbar for flowchart canvas
scrollbar1= ttk.Scrollbar(frame1,orient=VERTICAL,command=canvas1.yview)
scrollbar1.pack(side='right',fill=Y)

# scrollbar for code canvas
scrollbar2= ttk.Scrollbar(frame2,orient=VERTICAL,command=canvas2.yview)
scrollbar2.pack(side='right',fill=Y)

# adding scrollbar for flowchart canvas
canvas1.configure(yscrollcommand=scrollbar1.set)
canvas1.bind('<Configure>',lambda e:canvas1.configure(scrollregion=canvas1.bbox("all")))

# adding scrollbar for code canvas
canvas2.configure(yscrollcommand=scrollbar2.set)
canvas2.bind('<Configure>',lambda e:canvas2.configure(scrollregion=canvas2.bbox("all")))

# Frame where flowchart is drawn
area1=Frame(canvas1,width=600,height=800,bg='white')

# Frame where code is drawn
area2=Frame(canvas2,width=400,height=800,bg="#E5BEED")

# window to place frame for flowchart 
canvas1.create_window((0,0),window=area1,anchor='nw',width=600,height=800)

# window to place frame for code 
canvas2.create_window((0,0),window=area2,anchor='nw',width=400,height=800)

# creating start of flow chart
s1=Canvas(area1,width=75,height=15,bg="#E5BEED",highlightthickness=0)
s1.grid(row=0,column=0)
s1.create_text(35,7,text='0')
s2=Canvas(area1,width=75,height=15,bg="white",highlightthickness=0)
s2.grid(row=0,column=1)
s2.create_text(35,7,text='1')
s3=Canvas(area1,width=75,height=15,bg="#E5BEED",highlightthickness=0)
s3.grid(row=0,column=2)
s3.create_text(35,7,text='2')
s4=Canvas(area1,width=75,height=15,bg="white",highlightthickness=0)
s4.grid(row=0,column=3)
s4.create_text(35,7,text='3')
s5=Canvas(area1,width=75,height=15,bg="#E5BEED",highlightthickness=0)
s5.grid(row=0,column=4)
s5.create_text(35,7,text='4')
s6=Canvas(area1,width=75,height=15,bg="white",highlightthickness=0)
s6.grid(row=0,column=5)
s6.create_text(35,7,text='5')
s7=Canvas(area1,width=75,height=15,bg="#E5BEED",highlightthickness=0)
s7.grid(row=0,column=6)
s7.create_text(35,7,text='6')
s8=Canvas(area1,width=75,height=15,bg="white",highlightthickness=0)
s8.grid(row=0,column=7)
s8.create_text(35,7,text='7')

st1=Canvas(area1,width=y,height=40,bg="white",highlightthickness=0)
st1.grid(row=1,column=0,columnspan=8)

st1.create_oval(y//2-60,5,y//2+60,30,fill="#83f28f")
st1.create_text(y//2,18,text= "START" )
st1.create_line(y//2,30,y//2,40)
st1.create_line(y//2,40,y//2-5,35)
st1.create_line(y//2,40,y//2+5,35)


# functions called while using tools buttons
def CREATE():

    global x
    global y
    global pop1
    global n


    pop1=Toplevel(main)
    pop1.title("Create")
    pop1.geometry("500x200")

    def go(a,b):

        if(x==y//b):
            a.append(create(Edtype.get(),Ename.get(),Evalue.get()))
            a[-1].draw(area1)
        else:
            if(n==1):
                r=source[-1].block
                go(r,2*b)
            else:
                r=source[-1].eblock
                go(r,2*b)
    
    def INSERT():

        if(x==y):
            source.append(create(Edtype.get(),Ename.get(),Evalue.get()))
            source[-1].draw(area1)
        else:
            if(n==1):
                k=source[-1].block
                go(k,2)
            else:
                k=source[-1].eblock
                go(k,2)
        pop1.destroy()


    
    Cframe=Frame(pop1,width=500,height=200)
    Cframe.pack(anchor='center')

    Clabel = Label(Cframe,text="Create a variable")
    Clabel.grid(row=0,column=6,padx=20,pady=20)

    Edtype= Entry(Cframe,width=20)
    Edtype.grid(row=3,column=3,padx=20,pady=20)
    Edtype.insert(0,"Enter data type")

    Ename= Entry(Cframe,width=20)
    Ename.grid(row=3,column=6,padx=20,pady=20)
    Ename.insert(0,"Enter name")

    Evalue= Entry(Cframe,width=20)
    Evalue.grid(row=3,column=9,padx=20,pady=20)
    Evalue.insert(0,"Enter value")

    Cbutton=Button(Cframe,text='ENTER',width=10,command=INSERT)
    Cbutton.grid(row=6,column=6,padx=20,pady=20)

def ASSIGN():

    global x
    global y
    global pop1
    global n

    global x
    global y
    global pop1

    pop1=Toplevel(main)
    pop1.title("Create")
    pop1.geometry("500x200")

    def go(a,b):
        if(x==y//b):
            a.append(assign(Ename.get(),Evalue.get()))
            a[-1].draw(area1)
        else:
            if(n==1):
                r=source[-1].block
                go(r,2*b)
            else:
                r=source[-1].eblock
                go(r,2*b)
    
    def INSERT():
        if(x==y):
            source.append(assign(Ename.get(),Evalue.get()))
            source[-1].draw(area1)
        else:
            if(n==1):
                k=source[-1].block
                go(k,2)
            else:
                k=source[-1].eblock
                go(k,2)
        pop1.destroy()

    
    Cframe=Frame(pop1,width=500,height=200)
    Cframe.pack(anchor='center')

    Clabel = Label(Cframe,text="Assign the variable a value")
    Clabel.grid(row=0,column=7,padx=20,pady=20)

    Ename= Entry(Cframe,width=20)
    Ename.grid(row=3,column=6,padx=20,pady=20)
    Ename.insert(0,"Enter name")

    Evalue= Entry(Cframe,width=20)
    Evalue.grid(row=3,column=8,padx=20,pady=20)
    Evalue.insert(0,"Enter value")

    Cbutton=Button(Cframe,text='ENTER',width=10,command=INSERT)
    Cbutton.grid(row=6,column=7,padx=20,pady=20)

def INPUT():

    global x
    global y
    global pop1
    global n

    pop1=Toplevel(main)
    pop1.title("Create")
    pop1.geometry("500x200")

    def go(a,b):
        if(x==y//b):
            a.append(input(Evalue.get()))
            a[-1].draw(area1)
        else:
            if(n==1):
                r=source[-1].block
                go(r,2*b)
            else:
                r=source[-1].eblock
                go(r,2*b)

    
    def INSERT():
        if(x==y):
            source.append(input(Evalue.get()))
            source[-1].draw(area1)
        else:
            if(n==1):
                k=source[-1].block
                go(k,2)
            else:
                k=source[-1].eblock
                go(k,2)
        pop1.destroy()
    
    Cframe=Frame(pop1,width=500,height=200)
    Cframe.pack(anchor='center')

    Clabel = Label(Cframe,text="Enter the variable where to be inserted")
    Clabel.grid(row=0,column=6,padx=20,pady=20)

    Evalue= Entry(Cframe,width=20)
    Evalue.grid(row=3,column=6,padx=20,pady=20)
    Evalue.insert(0,"Enter the variable")

    Cbutton=Button(Cframe,text='ENTER',width=10,command=INSERT)
    Cbutton.grid(row=6,column=6,padx=20,pady=20)

def OUTPUT():

    global x
    global y
    global pop1
    global n

    pop1=Toplevel(main)
    pop1.title("Create")
    pop1.geometry("500x200")

    def go(a,b):
        if(x==y//b):
            a.append(output(Evalue.get()))
            a[-1].draw(area1)
        else:
            if(n==1):
                r=source[-1].block
                go(r,2*b)
            else:
                r=source[-1].eblock
                go(r,2*b)

    
    def INSERT():
        if(x==y):
            source.append(output(Evalue.get()))
            source[-1].draw(area1)
        else:
            if(n==1):
                k=source[-1].block
                go(k,2)
            else:
                if(n==1):
                    k=source[-1].block
                    go(k,2)
                else:
                    k=source[-1].eblock
                    go(k,2)
        pop1.destroy()
    
    Cframe=Frame(pop1,width=500,height=200)
    Cframe.pack(anchor='center')

    Clabel = Label(Cframe,text="Enter the content to be displayed")
    Clabel.grid(row=0,column=6,padx=20,pady=20)

    Evalue= Entry(Cframe,width=20)
    Evalue.grid(row=3,column=6,padx=20,pady=20)
    Evalue.insert(0,"Enter message")

    Cbutton=Button(Cframe,text='ENTER',width=10,command=INSERT)
    Cbutton.grid(row=6,column=6,padx=20,pady=20)

def IF():

    global x
    global y
    global pop1
    global n

    pop1=Toplevel(main)
    pop1.title("Create")
    pop1.geometry("500x200")

    def go(a,b):
        if(x==y//b):
            a.append(_if(Evalue.get()))
            a[-1].draw(area1)
        else:
            if(n==1):
                r=source[-1].block
                go(r,2*b)
            else:
                r=source[-1].eblock
                go(r,2*b)

    
    def INSERT():
        if(x==y):
            source.append(_if(Evalue.get()))
            source[-1].draw(area1)
        else:
            if(n==1):
                k=source[-1].block
                go(k,2)
            else:
                k=source[-1].eblock
                go(k,2)
        pop1.destroy()
    
    Cframe=Frame(pop1,width=500,height=200)
    Cframe.pack(anchor='center')

    Clabel = Label(Cframe,text="Enter a if condition")
    Clabel.grid(row=0,column=6,padx=20,pady=20)

    Evalue= Entry(Cframe,width=20)
    Evalue.grid(row=3,column=6,padx=20,pady=20)
    Evalue.insert(0,"condition")

    Cbutton=Button(Cframe,text='ENTER',width=10,command=INSERT)
    Cbutton.grid(row=6,column=6,padx=20,pady=20)

def WHILE():

    global x
    global y
    global pop1
    global n

    pop1=Toplevel(main)
    pop1.title("Create")
    pop1.geometry("500x200")

    def go(a,b):
        if(x==y//b):
            a.append(_while(Evalue.get()))
            a[-1].draw(area1)
        else:
            if(n==1):
                r=source[-1].block
                go(r,2*b)
            else:
                r=source[-1].eblock
                go(r,2*b)
    
    def INSERT():
        if(x==y):
            source.append(_while(Evalue.get()))
            source[-1].draw(area1)
        else:
            if(n==1):
                k=source[-1].block
                go(k,2)
            else:
                k=source[-1].eblock
                go(k,2)
        pop1.destroy()
    
    Cframe=Frame(pop1,width=500,height=200)
    Cframe.pack(anchor='center')

    Clabel = Label(Cframe,text="Enter the while condition for while loop")
    Clabel.grid(row=0,column=6,padx=20,pady=20)

    Evalue= Entry(Cframe,width=20)
    Evalue.grid(row=3,column=6,padx=20,pady=20)
    Evalue.insert(0,"Enter condition")

    Cbutton=Button(Cframe,text='ENTER',width=10,command=INSERT)
    Cbutton.grid(row=6,column=6,padx=20,pady=20)

def FOR():
    
    global x
    global y
    global pop1
    global n


    pop1=Toplevel(main)
    pop1.title("For loop")
    pop1.geometry("500x200")

    def go(a,b):

        if(x==y//b):
            a.append(_for(Edtype.get(),Ename.get(),Evalue.get()))
            a[-1].draw(area1)
        else:
            if(n==1):
                r=source[-1].block
                go(r,2*b)
            else:
                r=source[-1].eblock
                go(r,2*b)
    
    def INSERT():

        if(x==y):
            source.append(_for(Edtype.get(),Ename.get(),Evalue.get()))
            source[-1].draw(area1)
        else:
            if(n==1):
                k=source[-1].block
                go(k,2)
            else:
                k=source[-1].eblock
                go(k,2)
        pop1.destroy()


    Cframe=Frame(pop1,width=500,height=200)
    Cframe.pack(anchor='center')

    Clabel = Label(Cframe,text="for loop")
    Clabel.grid(row=0,column=6,padx=20,pady=20)

    Edtype= Entry(Cframe,width=20)
    Edtype.grid(row=3,column=3,padx=20,pady=20)
    Edtype.insert(0,"begin")

    Ename= Entry(Cframe,width=20)
    Ename.grid(row=3,column=6,padx=20,pady=20)
    Ename.insert(0,"end")

    Evalue= Entry(Cframe,width=20)
    Evalue.grid(row=3,column=9,padx=20,pady=20)
    Evalue.insert(0,"increment")

    Cbutton=Button(Cframe,text='ENTER',width=10,command=INSERT)
    Cbutton.grid(row=6,column=6,padx=20,pady=20)

# various program operations as buttons
N=Button(top,text='NEW',width=10,height=1)
N.pack(side='left',anchor='nw')
OP=Button(top,text='OPEN',width=10,height=1)
OP.pack(side='left',anchor='nw')
S=Button(top,text='SAVE',width=10,height=1)
S.pack(side='left',anchor='nw')
R=Button(top,text='RUN',width=10,height=1,command=lambda:start(source))
R.pack(side='left',anchor='nw')
C=Button(top,text='CLEAR',width=10,height=1,command=CLEAR)
C.pack(side='left',anchor='nw')

# various tools as buttons
I=Button(tools,text='INPUT',width=10,command=INPUT)
I.grid(row=0,column=0)
O=Button(tools,text='OUTPUT',width=10,command=OUTPUT)
O.grid(row=1,column=0)
C=Button(tools,text='CREATE',width=10,command=CREATE)
C.grid(row=2,column=0)
A=Button(tools,text='ASSIGNMENT',width=10,command=ASSIGN)
A.grid(row=3,column=0)
IF=Button(tools,text='IF',width=10,command=IF)
IF.grid(row=6,column=0)
F=Button(tools,text='FOR',width=10,command=FOR)
F.grid(row=7,column=0)
W=Button(tools,text='WHILE',width=10,command=WHILE)
W.grid(row=8,column=0)
A1=Button(tools,text='UP',width=10,command=A1)
A1.grid(row=9,column=0)
A2=Button(tools,text='DOWN',width=10,command=A2)
A2.grid(row=10,column=0)

# frame to store buttons for getting depth : how much nested
dep=Frame(tools,bg="grey")
dep.grid(row=11,column=0,padx=3,pady=3)

# buttons to move in and out of nest change depth
m1=Button(dep,text='^',width=3,command=M1)
m1.grid(row=0,column=0)
inout=Label(dep,text='1',width=10,padx=2,pady=3)
inout.grid(row=1,column=0)
m2=Button(dep,text='v',width=3,command=M2)
m2.grid(row=2,column=0)
# label to display depth

# binding to key board arrow keys to find position
main.bind("<Up>",U1)
main.bind("<Down>",D1)
main.bind("<Right>",R1)
main.bind("<Left>",L1)

# binding mouse to get coordinates of each point
main.bind('<Motion>',move)

pos=Label(tools,text='(2:0)',width=10,padx=2,pady=3)
pos.grid(row=12,column=0)

# label to display the coordinates
co=Label(tools,text='coordinates',width=10)
co.grid(row=13,column=0)

forif=Label(tools,text='1',width=10)
forif.grid(row=14,column=0)

A3=Button(tools,text='O',width=10,command=A3)
A3.grid(row=15,column=0)

# g=open('C:/Users/91964/Desktop/GITHUB/sem2/DS/project/new_project/numbers.txt',"r")
# data2=g.read()

num=Label(area2,width=2,height=800,bg='white',text=data2)
num.pack(side='left',anchor='nw')

main.mainloop()

print(z)