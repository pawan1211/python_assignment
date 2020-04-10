class Second(): 
   def __gt__(self,a,b):
       c=len(a)
       d=len(b)
       l=0
       if(c>d or d>c ):
          print("String is not equal")
       else:
         for i in range(len(a)):
            if(a[i] not in b[i]):
                l=1
                break
         if l==1:
           print("String is not equal")
         else:
           print("String is  equal")     
         
      
  
a=raw_input("enter the first string\n")
b=raw_input("enter the second string\n")	
obj=Second()
  
obj.__gt__(a,b)
