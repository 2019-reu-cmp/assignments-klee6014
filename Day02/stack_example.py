"""stack_example.py -- example of basic python

Modified 2017-06-01
"""

def a(x, y):
  """(x+1)*y"""
  x += 1 #x = x + 1
  return x * y

def b(z):
  """((z+1)*z) and prints the answer"""
  prod = a(z, z)
  print(z, prod)
  return prod



def c(x, y, z):
  """adds x+y+z together as total, (total+1)*total**2"""
  total = x + y + z
  square = b(total)**2
  return square

x = 1
y = x + 1
print('c =', c(x, y + 3, x + y)) 
#file prints 'c = ((x + y + 3 + x + y +1)*(x + y + 3 + x + y))**2'

#Things We Could Do
# Added docstrings
# Easier to use variables
# Put functions in a better order

