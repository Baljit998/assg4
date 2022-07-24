class Vehicle:
 	def __del__(self):
 		print("Vehicle object destroyed")
 		print(10/0)
v = Vehicle()
del v

"""output
Vehicle object destroyed
Exception ignored in: <function Vehicle.__del__ at 0x000002917B392440>
Traceback (most recent call last):
  File "C:/Users/User/Desktop/assig4/vehicle.py", line 4, in __del__
    print(10/0)
ZeroDivisionError: division by zero
"""
