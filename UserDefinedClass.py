from tkinter import *
import config

# class to create an object variable with particular data type,name & intial value
class create:
   def __init__(self,dtype,name,value=None):
        self.dtype = dtype
        self.name = name
        self.value = value
        self.canvas = None

   def draw(self,area):
        if(config.z==1):
            self.canvas = Canvas(area,width=config.x,height=40,bg="white",highlightthickness=0)
            self.canvas.grid(row=config.ROW1,column=config.COL1,columnspan=config.z)
            self.canvas.create_rectangle(config.x//2-30,0, config.x//2+30,30,fill="#7B9E89")
            self.canvas.create_text(config.x//2,15,text=str(self.name) +' = '+ str(self.value) )
            self.canvas.create_line(config.x//2,30,config.x//2,40)
            self.canvas.create_line(config.x//2,40,config.x//2-5,35)
            self.canvas.create_line(config.x//2,40,config.x//2+5,35)

        self.canvas = Canvas(area,width=config.x,height=40,bg="white",highlightthickness=0)
        self.canvas.grid(row=config.ROW1,column=config.COL1,columnspan=config.z)
        self.canvas.create_rectangle(config.x//2-60,0, config.x//2+60,30,fill="#7B9E89")
        self.canvas.create_text(config.x//2,15,text=str(self.name) +' = '+ str(self.value) )
        self.canvas.create_line(config.x//2,30,config.x//2,40)
        self.canvas.create_line(config.x//2,40,config.x//2-5,35)
        self.canvas.create_line(config.x//2,40,config.x//2+5,35)

   def parse(self,file):
        
        if self.value:
            file.write(f"{self.dtype} {self.name} = {self.value};\n")
        else:
            file.write(f"{self.dtype} {self.name};\n")
