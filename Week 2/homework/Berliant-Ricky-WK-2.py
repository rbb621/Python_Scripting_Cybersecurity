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
from prettytable import PrettyTable


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
        
        macTimeList = [timeLastModified, timeCreated, timeLastAccess] # Group the MAC Times in a List
        return True, None, fileSize, macTimeList
    except Exception as err:
        return False, str(err), None, None

''' LOCAL CLASSES '''
# NONE

''' MAIN ENTRY POINT '''

def main():

    print("First Script: Obtain File Meta Data\n")

    targetDir = input('Enter a directory: ') # Input
    print()

    resultTable = PrettyTable(['Path','Type', 'Size', 'UTC-Modified', 'UTC-Accessed', 'UTC-Created'])
    
    resultList = []


    try:
        fileList = os.listdir(targetDir) # Directory
        for eachFile in fileList:
            print(eachFile)
            path = os.path.join(targetDir, eachFile)
            path = os.path.abspath(path)

            success, errInfo, fileSize, macList = GetFileMetaData(path)
                   

    except Exception as err:
        print("\n\nScript Aborted     ", "Exception =     ", err)

        
    if success:
        print("Success:   ", targetDir)
        print("File Size: ", fileSize)
        print("MAC Times: ", macList)

        metaData         = os.stat(targetDir)       # Use the stat method to obtain meta data
        fileSize         = metaData.st_size          # Extract fileSize and MAC Times

        # Targeting the Elements to convert them to readable times
        timeLastAccess   = macList[0]
        timeLastModified = macList[1]
        timeCreated      = macList[2]
        
        print("MetaData:           ", metaData)

        
        # Convert it to utcTime
        modEpoch = timeLastModified 
        readableAccess = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeLastAccess))
        readableModified = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeLastModified))
        readableCreated = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeCreated))

        # Human Readable Times
        print("\nEpoch time converted to human-readable form:")
        print("Last Access Time:   ", readableAccess)
        print("Last Modified Time: ", readableModified)
        print("Creation Time:      ", readableCreated)
        
    else:
        print("Fail:    ", TARGET, "Exception =     ", errInfo)



if __name__ == '__main__':
    main()
    print("\nScript End")