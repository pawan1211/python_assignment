
import math
class Mymath:
 
 def __init__(self,a,b):
       self.a=a
       self.b=b

 def sqroot(self):
     c=math.sqrt(self.a)
     print "square-root of number is =",c 
 def addition(self):
    
	 c=self.a+self.b
	 print "addion of two number is =",c
 def subtraction(self):
    
	 c=self.a-self.b
	 print "subtraction of two number is =",c	 
 def multiplication(self):
	  c=self.a*self.b
	  print "multiplication of two number is =",c
 def division(self):
	  c=self.a/self.b
	  print "division of two number is =",c	  
	  
	
		
		
a=input("enter the first number\n")
a1=int(a)
b=input("enter the second number\n")	
b1=int(b)

obj = Mymath(a1,b1) 
obj.sqroot()
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()
