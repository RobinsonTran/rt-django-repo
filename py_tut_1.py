# for line breaks and partitions; organization purposes
def lbreak():
    print ''
    print '-' * 45
    print ''

#  def fib2(n):
#      result=[]
#      a,b=0,1
#      while a < n:
#          result.append(a)
#          a,b=b,b+a
#      return result
#  f100=fib2(18)

#  print f100

# lbreak()

# def f(a, L=[]):
#     L.append(a)
#     return L

# print f(1)
# print f(2)
# print f(3)


# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# lbreak()


#  Default Argument Values
#  ------------------------------

#  def ask_ok(prompt, retries =4, complaint ='Yes or No, dude!'):
#      while True:
#          ok = raw_input(prompt)
#          if ok in ('y','ye','yes'):
#              return True
#          if ok in ('n','no','nop','nope'):
#              return False
#          retires = retries -1
#          if retries < 0:
#              raise IOError ('refusenik user')
#          print complaint
#  ask_ok('Do you really want to quit?')

#  ask_ok('OK to overwrite the file?',2)

#  ask_ok('OK to overwrite the file',2,'Come on, only yes or no!')

#  # Keyword Arguments
#  #---------------------------

#  def parrot(voltage, state='a stiff',action='voom',type='Norwegian Blue'):
#      print "--This parrot wouldn't",action,
#      print "if you put", voltage, "volts throught it."
#      print "--Lovely plumage, the",type
#      print "--It's",state,"!"


#  parrot (1000)
#  # print ''
#  print '### 1 positional argument ###'
#  # print ''
#  parrot (voltage=1000)
#  # print ''
#  print '# 1 keyword argument'
#  # print ''
#  parrot (voltage=1000000,action='VOOOOOM')
#  # print ''
#  print '### 2 keyword arguments ###'
#  # print ''
#  parrot (action='VOOOOOOOM',voltage=2000000)
#  # print ''
#  print '### 2 keyword arguments ###'
#  # print ''
#  parrot ('a million','bereft of life','jump')
#  # print ''
#  print '### 3 positional arguments ###'
#  # print ''
#  parrot ('a thousand',state='pushing up the daisies')
#  # print ''
#  print '### 1 positional, 1 keyword ###'

#  def cheeseshop(kind, *arguments, **keywords):
#      print "--Do you have any",kind,"?"
#      print "--I'm sorry, we're all out of",kind,"."
#      for arg in arguments:
#          print arg
#      print "-" * 69
#      keys = sorted (keywords.keys())
#      for kw in keys:
#          print kw, ":",keywords[kw]
#  cheeseshop("Limburger","It's very runny, sir.",
#          "It's really very, VERY runny, sir.",
#          shopkeeper='Michael Palin',
#          client="John Clease",
#          sketch="Cheese Shop Sketch")

#  #Arbitrary Argument Lists
#  #--------------------------------------

#  def write_multiple_items(file, separator, *args):
#      file.write(separator.join(args))

#  print '-' * 69

#  # Unpacking Argument Lists
#  #-----------------------------


#  def parrot(voltage, state='a stiff', action='voom'):
#      print "-- This parrot wouldn't", action ,
#      print "if you put", voltage, "volts through it.",
#      print "E's", state, "!"

#  d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOOM"}
#  parrot(**d)


#  print '-' *69

#  def make_incrementor(n):
#      return lambda x: x + n

#  f = make_incrementor(42)


#  print f(0)
#  print f(11)


#  print '-' *69

#  pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
#  pairs.sort(key=lambda pair:pair[1])
#  print pairs



#  print '-' *69

# #-----------------Data Structures-----------------------------
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print fruits.count('apple')
# print fruits.count('tangerine')
# print fruits.index('banana')
# print fruits.index('banana', 4) # Find next banana starting a position 4
# print fruits.reverse()
# print fruits
# fruits.append('grape')
# print fruits
# fruits.sort()
# print fruits
# print fruits.pop()

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print stack
# stack.pop()
# print stack
# stack.pop()
# stack.pop()
# print stack




# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# queue.popleft()
# queue.popleft()
# print queue

# squares = []
# for x in range(10):
#     squares.append(x**2)
# print squares

# list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x !=y]
# print list

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# print combs

# print '-' * 69

# vec = [-4, -2, 0, 2, 4]
# # create a new list with the values doubled
# print [x*2 for x in vec]


# print '-' * 69


# # filter the list to exlcude negative numbers

# print [x for x in vec if x >= 0]


# print '-' * 69

# # apply a function to all the elements
# print [abs(x) for x in vec]

# print '-' * 69

# # call a method on each element
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print [weapon.strip() for weapon in freshfruit]

# lbreak()

# # create a list of 2-tuples like (number, square)
# print [(x, x**2) for x in range(6)]

# lbreak()

# # the tuple must be parenthesized, otherwise an error is raised
# # print [x, x**2 for x in range(6)]

# # flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print [num for elem in vec for num in elem]

# lbreak()

# from math import pi
# print [str(round(pi, i)) for i in range(1, 6)]
# lbreak()
# print [str(round(pi, i)) for i in range(0, 20)]

# lbreak()

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# print [[row[i] for row in matrix ] for i in range(4)]

# lbreak()

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print transposed

# lbreak()

# transposed = []
# for i in range(4):
#     # the following 3 lines implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# print transposed

# lbreak()

# print list(zip(*matrix))

# lbreak()

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print a

# lbreak()

# del a [2:4]
# print a

# lbreak()

# del a[:]
# print a

# lbreak()

# t = 12345, 54321, 'hello'
# print t[0]
# lbreak()
# print t
# lbreak()
# # Tuples may be nested:
# u = t, (1, 2, 3, 4, 5)
# print u

# # Tuples are immutable:
# # t[0] = 88888

# lbreak()

# # but they can contain mutable objects:
# v = ([1, 2, 3], [3, 2, 1])
# print v

# lbreak()

# empty = ()
# singleton = 'hello', # <---- note trailing comma
# print len(empty)

# lbreak()

# print len(singleton)

# lbreak()

# print singleton

# lbreak()

# v, w, z = t
# print t
# print w
# print v
# # print x
# # print y
# print z

# lbreak()

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print (basket)      # show that duplicates have benn removed

# print 'orange' in basket    # fast membership testing

# print 'crabgrass' in basket

# # Demonstrate set operations on unique letters from two words

# a = set('abracadabra')
# b = set('alacazam')
# print a
# lbreak()
# print a - b
# lbreak()
# print a | b
# lbreak()
# print a & b
# lbreak()
# print a ^ b
# lbreak()

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print a

# lbreak()

# -------------------Dictionary-----------------------


