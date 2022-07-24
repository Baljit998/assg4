try:
 print("outer try block")
 n = int(input("enter a number"))
 print(10/n)
 try:
  print("inner try")
  print("anu"+"preet")
 except TypeError:
  print("Hello")
 else:
  print("inner no exception")
 except ArithmeticError:
  print(10/5)
 else:
  print("outer no excepiton")
 finally:
  print("finally block")

"""output
outer try block
enter a number50
0.2222222222222222
inner try
anupreet
inner no exception
outer no excepiton
finally block
"""
 
