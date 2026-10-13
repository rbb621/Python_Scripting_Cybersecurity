'''
Name: Ricky Berliant
Date: 10/14/2026
Class: CYBV312
Instructor: Cameron Covington
Assignment: Final
'''
import re

print("Final Script")
with open("mem.raw", 'rb') as target:  # assumes that mem.raw is in the same folder as script
    
    contents = target.read() # read the entire contents of the file
    
    txt = re.sub(b"[^A-Za-z']", b' ', contents)  # strip all non alpha characters
    txt = txt.lower()                            # convert all to lower case
    txt = txt.decode("utf-8")                    # convert to simple ASCII
    
    wordList = txt.split()  # Create a list of possible words
    print(len(wordList))


    kernelCount = 0
    encryptCount = 0
    fairwitnessCount = 0
    
    '''
    you will add your code here, that determines the number of occurrences
    of the following possible words found in the wordList
    
    kernel   encrypt  fairwitness  
    
    Note: You are NOT allowed to modify any other lines in the script, except
          to add your name in the comment block at the top
    Note: Your code will create the variables:  kernelCount, encryptCount, and fairwitnessCount
          so the print statements below will print out the correct number of occurrences
    '''
    
    print("kernelCount: ",      kernelCount)
    print("encryptCount:",      encryptCount)
    print("fairwitnessCount: ", fairwitnessCount)
    
