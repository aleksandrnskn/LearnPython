# If ... Else

"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

# If statement:

a = 33
b = 200

if b > a:
  print("b is greater than a")

# Elif

a = 33
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
# Else

a = 200
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
