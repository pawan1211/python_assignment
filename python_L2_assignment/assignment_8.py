"""
9.Write a class called Circle and write the methods to calculate the area and circumference of the circle by 
    initialing the radius of the circle. 
    """
class Circle:
    
 def area(self,a):
     c=3.14*a*a
     print "area of circle =",c 
 def circumference(self,a):
     c=2*3.14*a
     print "circumference of circle =",c      
     
a=input("enter the radius of circle \n")
a1=int(a)

obj = Circle() 
obj.area(a1)
obj.circumference(a1)
