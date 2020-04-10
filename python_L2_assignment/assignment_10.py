"""
10.	Create a class called First and two classes called Second  and Third which inherit from First. 
Create class called Fourth which inherits from Second and Third. Create a common method called method1 in 
all the classes and provide the Method Resolution Order.
"""

import math
class First: 
 def method1(self):
     print"this class is first"
     
class Second(First): 
    def method1(self):
       print"this class is second"  
       First.method1(self)
       
class Third(First): 
   def method1(self):
       print"this class is third" 
       First.method1(self)
        
class Fourth(Second,Third): 
  def method1(self):
      print"this class is fourth" 
      Second.method1(self)
      Third.method1(self)
     

obj = Fourth()
obj.method1()
