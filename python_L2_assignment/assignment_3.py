import math
class Mymath: 

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
	  
	
		
a=input("enter the first number\n")
a1=int(a)
b=input("enter the second number\n")	
b1=int(b)

obj = Mymath() 
obj.sqroot(a1)
obj.addition(a1,b1)
obj.subtraction(a1,b1)
obj.multiplication(a1,b1)
obj.division(a1,b1)