import os

 # Target Directory

DIR = input('Enter a file path: ')

# create an empty dictionary
folderDict = {}

# Get list of entries in the directory
dirlist = os.listdir(DIR)

for eachEntry in dirlist:
    dirPath = os.path.join(DIR, eachEntry)
    folderDict[dirPath] = os.path.getsize(dirPath)

entryList = list(folderDict.items())

print('first five', entryList[:5])
print('last five', entryList[-5:])
# interate through each entry
# get the full path 

# Add entry to dictionary key = path, value = size

# Next convert the dictionary to a list

# Now slice the list