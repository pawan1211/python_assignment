"""
 5.Write a code to implement a child class called mathnew and parent classes as sqroot,   addition,subtraction, multiplication 
  and division. Use the super() function to inherit the parent methods.
  """

import math
class Mymath(object): 
 
     
 def sqroot(self,a):
    
	 c=math.sqrt(a)
	 print "square-root of  number is =",c 
 def addition(self,a,b):
    
	 c=a+b
	 print "addion of two number is =",c
 def subtraction(self,a,b):
    
	 c=a-b
	 print "subtraction of two number is =",c	 
 def multiplication(self,a,b):
	  c=a*b
	  print "multiplication of two number is =",c
 def division(self,a,b):
	  c=a/b
	  print "division of two number is =",c	  
	  
class My(Mymath):
    def __init__(self,a,b):
       self.a=a
       self.b=b
       super(My, self).sqroot(a)
       super(My, self).addition(a,b)
       super(My, self).subtraction(a,b)
       super(My, self).multiplication(a,b)
       super(My, self).division(a,b)
       
       
a=input("enter the first number\n")
a1=int(a)
b=input("enter the second number\n")	
b1=int(b)
obj = My(a1,b1)
