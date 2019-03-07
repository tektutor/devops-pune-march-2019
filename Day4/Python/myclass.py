#!/usr/bin/python


class MyClass:
   def __init__(self):
       print ("This is a constructor")   

   def sayHello(self,msg):
      print (msg)
      print ('This is second print')

obj = MyClass()
obj.sayHello('Hello Python!')
