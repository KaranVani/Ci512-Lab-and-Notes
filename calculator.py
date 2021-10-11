from myfunctions import sum
from myfunctions import subtract
from myfunctions import multiply
from myfunctions import divide

userinput = input('Type a for add, s for subtract, m for multiply, d for divide: ')

if userinput == 'a':
  sum()
elif userinput == 's':
  subtract()
elif userinput == 'm':
  multiply()
elif userinput == 'd':
  divide()
