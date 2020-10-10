'''
Triple quotes indicates a block comment!
Fill in the missing code so that the
following functions work as intended.

The functions are ordered by increasing difficulty.
Make sure you know the difference between
**print** and **return**!
'''

### Variables, Conditionals ###

# 1) Return the sum of the two parameters
def add(x, y):
  return x+y

# 2) Return the larger number
def larger(x, y):
    if x>y:
        return x
    else:
        return y

# 3) Return True only when _exactly_ one input is True
def xor(a, b):
    if (a==true and b==false) or (a==false and b==true):
        return True
    else:
        return False

### Loops ###

# 4) Print 'hello world' n times
def hello_n(n):
    for i in range (0,n+1):
        print("hello world")
 

# 5) Print the decimal representations of 1/2, 1/3, 1/4 ... 1/n
def fraction(n):
    for i in range (0,n+1):
        print(1/i)


# 6) Return the factorial of n (written as n!)
# ex: 4! = 4 * 3 * 2 * 1 = 24
def factorial(n):
    x=1
    for i in range (n+1,1,-1):
        x*=i
    return x

# 7) Print a triangle of stars according to n
# Hint: Use nested loops!
def stars(n):
  for i in range (0,n+1):
    for j in range (0,i):
        print ("*", end='')
    print("")

stars(4)
''' ex: stars(4) should print:
*
**
***
****
'''