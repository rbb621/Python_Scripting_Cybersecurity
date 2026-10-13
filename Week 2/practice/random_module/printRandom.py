import random

for i in range(5):
    print(random.randint(1,10))

'''
When you save your Python scripts, take care not to give them a name that is used 
by one of Python’s modules,  such as random.py, sys.py, os.py, or math.py. 
If you accidentally name one of your programs, say, random.py, 
and use an import random statement in another program, your program would import
your random.py file instead of Python’s random module. This can lead to errors 
such as AttributeError: module 'random' has no attribute 'randint', since your 
random.py doesn’t have the functions that the real random module has. 
Don’t use the names of any built-in Python functions either, such as print() 
or input().
'''

