from pathlib import Path
import os

print(Path.cwd()) #Current Directory

# How to properly create a new directory
rickyPath = '/Users/rickyberliant/Documents'
newPath = '/Fire Emblem'
fall2026 = 'Fall 2026/CYBV 312/Week 2/chapter_9'

os.chdir(rickyPath) #Changes directory, as long as it exists
print(Path.cwd()) #/Users/rickyberliant/Documents/...
print(Path.home()) # /Users/rickyberliant
# Python will display an error if you try to change to a directory 
# that does not exist.

#Creates a new directory

'''
Absolute - Root
Relative - CWD (Curren Working Directory)
'''

#Abolute Example:
print(Path(rickyPath).is_absolute())

#Relative Example
print(Path(fall2026).is_absolute())

print(os.path.abspath('.//Scripts'))
print(os.path.abspath('.'))
os.path.abspath('.')