Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='Python is a case sensitive language'   #question1
... print("length of string=",len(a))
... print(a[::-1])
... b=a[10:26:1]
... print(b)
... replaced=a.replace("a case sensitive","object oriented")
... print(replaced)
... print(a.index("a"))
... print(a.replace(" ",""))
... 
... 
... name="abc"         #question 2
... SID="2210XXXX"
... department="XYZ"
... CGPA=9.9
... print("Hey,",name,"here!\nMy SID is",SID,"\nI am from",department,"department and my cgpa is",CGPA)
... 
... 
... a=56                                   #question 3
... b=10
... print("a & b=", a&b)
... print("a | b=", a|b)
... print("a ^ b=", a^b)
... print("left shifting both a and b with 2 bits=",a<<2,"=",b<<2)
... print("right shifting a with 2 bits and b with 4 bits=",a>>2,"=",b<<4)
... 
... 
... 
... num1=float(input("enter first number:"))          #question4
... num2=float(input("enter second number:"))
... num3=float(input("enter third number:"))
... print(" The greatest of the three number is:", max(num1,num2,num3))
... 
... 
... 
... str=input(" enter the string:")                    #question 5
if "name" in str:
    print("Yes")
else:
    print("No")



len1=float(input("Enter length of side 1:"))       #question 6
len2=float(input("Enter length of side 2:"))
len3=float(input("Enter length of side 3:"))
if len1+len2>len3 and len2+len3>len1 and len1+len3>len2:
    print("Yes")
else:
    print("No")






