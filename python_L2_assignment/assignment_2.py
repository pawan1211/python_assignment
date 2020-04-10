"""
2.	 Given email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'
write a regular  expression to extract 
a. email id
b. domain name
c. time
"""


import re
email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'
s =re.findall('\S+@\S+',email)
s1=re.findall('@\S+',email)
s2=re.findall('[0-9]+:+[0-9]+:+[0-9]+',email)
email_id=""
domain_name=""
domain_name1=""
time=""
for i in s:
   email_id=email_id+i
for i in s1:
     domain_name1=domain_name1+i
for i in domain_name1:
    if(i not in '@'):
       domain_name=domain_name+i     
for i in s2:
   time=time+i   

print "the email_id is ",email_id
print "the domain_name is ",domain_name
print "the time is ",time
