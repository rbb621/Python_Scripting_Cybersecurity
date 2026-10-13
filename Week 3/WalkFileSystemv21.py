'''
os.walk() example
Cameron Covington
Version 0.50
October 2020
'''

# Import filesystem library
import os

# Define pseudo-constant directory
DIR = "/Users/cameroncovington/Library/Mobile Documents/com~apple~CloudDocs/Arizona/CYBV312/Week 3"

print("Walking: ",DIR, "\n")

# Begin walking at the DIR 
for root, dirs, fileList in os.walk(DIR):
    # Print out the root directory we are currently at
    print("root:    ", root)
    # Print out the subdirectories contained within the current directory
    print("dirs:    ", dirs)
    # Print out the files contained within the current directory
    print("files:   ", fileList)
    
    # For each of the files, join the path with the filename to get the complete path
    for nextFile in fileList:
        fullPath = os.path.join(root, nextFile)
        print(fullPath)
    
    # Formatting
    print("="*50)
    
    # When we get to this point, we will do it all over again, recursively iterating through the directory structure    

# Exiting the for loop, printing end of script    
print("\nScript End")