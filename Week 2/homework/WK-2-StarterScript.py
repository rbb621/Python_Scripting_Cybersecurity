'''
Script:  WK-2 Starter Script
Author:  Ricky Berliant
Date:    9/6/2026
Version: 3.14.7
Purpose: Understanding the File System better
'''

''' IMPORT STANDARD LIBRARIES '''
import os       # File System Methods
import time     # Time Conversion Methods

''' IMPORT 3RD PARTY LIBRARIES '''
# NONE

''' DEFINE PSEUDO CONSTANTS '''

TARGET = "TESTFILE.JPG"   # Get the local name of this script

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
    
    print("First Script: Obtain File Meta Data\n")

    print("Accessing Metadata for : ", TARGET)
    fullPath = os.path.abspath(TARGET)
    success, errInfo, fileSize, macList = GetFileMetaData(TARGET)
    
    if success:
        print("Success:   ", TARGET)
        print("File Size: ", fileSize)
        print("MAC Times: ", macList)
    else:
        print("Fail:    ", TARGET, "Exception =     ", errInfo)

print("\nScript End")
