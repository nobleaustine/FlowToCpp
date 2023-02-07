from tkinter import *


class create:

	def __init__(self,dtype,name,value=None):
		self.dtype = dtype
		self.name = name
		self.value = value
		

	def parse(self,file):

		if self.value: 
			file.write(f"{self.dtype} {self.name} = {self.value};\n")
		else:
			file.write(f"{self.dtype} {self.name};\n")


class assign:

	def __init__(self,name,value):
		self.name = name
		self.value = value

	def parse(self,file):
		file.write(f"{self.name} = {self.value};\n")


class output:

	def __init__(self,value):
		self.value = value

	def parse(self,file):
		file.write(f"cout << {self.value};\n")


class input:

	def __init__(self,name):
		self.name = name

	def parse(self,file):
		file.write(f"cin >> {self.name};\n")


class _if:

	def __init__(self,condition,if_block,else_block=None):
		self.condition = condition
		self.if_block = if_block
		self.else_block = else_block

	def parse(self,file):

		file.write(f"if ({self.condition}){{\n")
		for i in self.if_block: 
			i.parse(file)
		file.write("}\n")

		if self.else_block:
			file.write(f"else {{\n")
			for i in self.else_block: 
				i.parse(file)
			file.write("}\n")


class _while:

	def __init__(self,condition,block):
		self.condition = condition
		self.block = block

	def parse(self,file):
		file.write(f"while ({self.condition}){{\n")
		for i in self.block: 
			i.parse(file)
		file.write("}\n")


class _for:

	def __init__(self,beg,end,step,block):
		self.beg = beg
		self.end = end
		self.step = step
		self.block = block

	def parse(self,file):
		file.write(f"for (int i={self.beg}; i<={self.end}; i=i+{self.step}){{\n")
		for i in self.block: 
			i.parse(file)
		file.write("}\n")


def start(data):

	file = open("main.cpp","w")
	file.write("#include <iostream>\n#include <stdlib.h>\nusing namespace std;\n\nint main() {\n\n")

	for i in data:
		i.parse(file)

	file.write('\nsystem("pause");\nreturn 0;\n\n}')
	file.close()

	os.system("g++ -o main main.cpp")
	os.system("main")


if __name__ == "__main__":

	import os
	start([create('int','m','9+4'),create('char','letter'),assign('letter',"'g'"),output('"rfhrufh"'),input('m'),_for(0,9,1,[output('"hi"')]),_if('m<10',[output('"yes"')],[output('"no"'),_if("letter=='g'",[_while('m<=20',[output('m'),assign('m','m+1')])])])])