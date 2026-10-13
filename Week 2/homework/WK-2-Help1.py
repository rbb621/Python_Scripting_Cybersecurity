'''
Script:  First Script
Author:  YOUR NAME
Date:    July 2020
Version: .50
Purpose: ENTER PURPOSE

ASSIGNMENT DETAILS
After experimenting with the First.py script and attending this weeks lecture, you are to modify/extend the First.py script as follows:

1) Allow the user to specify a directory to process using the built-in Python input() function
2) Process each entry in that directory and report:
    Full-Filepath, FileSize, MAC Times for each directory entry
    Converting each MAC epoch value into human readable form
3) Catch any errors when attempting to process files and report them

LECTURE HINTS

    PROMPT USER FOR ENTRY
        directory = input("Enter a Directory to Process: ")
    
    CONVERT EPOCH VALUES TO HUMAN READABLE UTC TIME
        Epoch= macTimes[0]
        utcTime= time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(modEpoch))
        print(utcTime)
    
'''

''' IMPORT STANDARD LIBRARIES '''
import os       # File System Methods
import sys      # System Methods
import time     # Time Conversion Methods

''' IMPORT 3RD PARTY LIBRARIES '''
# NONE

''' DEFINE PSEUDO CONSTANTS '''

# NONE

''' LOCAL FUNCTIONS '''

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
        timeLastAccess   = metaData.st_atime
        timeLastModified = metaData.st_mtime
        timeCreated      = metaData.st_ctime
        
        macTimeList = [timeLastModified, timeLastAccess, timeCreated] # Group the MAC Times in a List
        return True, None, fileSize, macTimeList
    
    except Exception as err:
        return False, str(err), None, None

''' LOCAL CLASSES '''
# NONE

''' MAIN ENTRY POINT '''

if __name__ == '__main__':
    
    print("\nWK-2 Solution: YOUR NAME - Version One\n")

    targetDIR = input('Enter a Directory Path i.e. c:/ >>> ')
    print()
    
    try:
        fileList = os.listdir(targetDIR)
        for eachFile in fileList:
            print(eachFile)
            path = os.path.join(targetDIR, eachFile)
            print(path)

            success, errInfo, fileSize, macList = GetFileMetaData(path)
            
            print(success)
            print(errInfo)
            print(fileSize)
            print(macList)
            
            print("="*50)
            
            # Your additional script code here
            
    except Exception as err:
        print("\n\nScript Aborted     ", "Exception =     ", err)        