"""

6.	Write a code to overload __add__ method to perform  2 x 2 matrix addition
"""
class Second(): 
   def __add__(self,a,b):
       rows, cols = (2,2) 
       c= [[0]*cols]*rows 
       for i in range(len(a)):
          for j in range(len(a)):
             c[i][j]=a[i][j]+b[i][j]
             print c[i][j]
    
print "adding first matrix\n"
a=[[1,2],[4,5]]
b=[[1,8],[9,5]]
obj = Second()
obj.__add__(a,b)
print "adding second matrix\n"
a=[[1,4],[6,7]]
b=[[1,8],[9,5]]
obj.__add__(a,b)
