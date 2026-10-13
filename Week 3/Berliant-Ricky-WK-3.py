'''
WK-3 STARTER SCRIPT
Ricky Berliant
9/13/2026
CYBR 312
Instructor: Cameron Covington
'''

# Python Standard Libaries 
import os
import hashlib
import time

# Python 3rd Party Libraries
from prettytable import PrettyTable     # pip install prettytable

# Psuedo Constants

targetFolder = input("Enter Target Folder: ")
# Start of the Script
print("Walking: ", targetFolder, "\n")

# Table Design - Listed in categories sorted by columns
tbl = PrettyTable(['AbsPath', 
                   'FileSize', 
                   'LastModified', 
                   'LastAccess', 
                   'CreatedTime', 
                   'SHA-256 HASH'])  


def GetFileMetaData(fileName):
    ''' 
        obtain filesystem metadata
        from the specified file
        specifically, fileSize and MAC Times
        
        return True, None, fileSize and MacTimeList
    '''
    try:
        metaData         = os.stat(fileName)       # Use the stat method to obtain meta data
        fileSize         = metaData.st_size         # Extract fileSize and MAC Times
        lastModified     = metaData.st_mtime
        lastAccess       = metaData.st_atime
        createdTime      = metaData.st_ctime
        
        macTimeList = [lastModified, lastAccess, createdTime] # Group the MAC Times in a List
        return True, None, fileSize, macTimeList
    
    except Exception as err:
        return False, str(err), None, None

# Retrieving Hexadecimals Through Hashlib
def GetSHA256(absPath):
    try:
        # Open each file in read binary mode
        with open(absPath, 'rb') as targetFile:
            # Read the contents of the file and get the file hash
            fileContents = targetFile.read()
            sha256Obj = hashlib.sha256()
            sha256Obj.update(fileContents)
            hexDigest = sha256Obj.hexdigest()
            return hexDigest
            
    except Exception as err:
        print("\n\nScript Aborted     ", "Exception =     ", err) 

'''
Note:
currentRoot = directory currently being examined
dirList     = subdirectories found
fileList    = files found
'''

for currentRoot, dirList, fileList in os.walk(targetFolder):

    for nextFile in fileList:
        
        fullPath        = os.path.join(currentRoot, nextFile)
        absPath         = os.path.abspath(fullPath)
        fileSize        = os.path.getsize(absPath)
        metaData        = os.stat(absPath)
        lastModified    = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(metaData.st_mtime))
        lastAccess      = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(metaData.st_atime))
        createdTime     = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(metaData.st_ctime))
        fileHash        = GetSHA256(absPath)
        
        tbl.add_row( [ absPath, fileSize, lastModified, lastAccess, createdTime, fileHash] ) 


tbl.align = "l" # align the columns left justified
# display the table
print (tbl.get_string(sortby="FileSize", reversesort=True))


print("\nScript-End\n")

