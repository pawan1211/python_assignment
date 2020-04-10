
class Circle:
    
 def __init__(self,a):
       self.a=a
         
 def area(self):
     c=3.14*a*a
     print "area of circle =",c 
     
 def circumference(self):
     c=2*3.14*a
     print "circumference of circle =",c      
     
a=input("enter the radius of circle \n")
a1=int(a)

obj = Circle(a1) 
obj.area()
obj.circumference()
