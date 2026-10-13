'''
Script:  First Script
Author:  Chet Hosmer
Date:    July 2020
Version: .50
Purpose: script Description
'''

''' IMPORT STANDARD LIBRARIES '''
import os       # File System Methods
import sys      # System Methods
import time     # Time Conversion Methods

''' IMPORT 3RD PARTY LIBRARIES '''
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
        
        macTimeList = [timeLastModified, timeCreated, timeLastAccess]   # Group the MAC Times in a List
        return True, None, fileSize, macTimeList
    
    except Exception as err:
        return False, str(err), None, None

''' LOCAL CLASSES '''
# NONE

''' MAIN ENTRY POINT '''

def main():
    
    print("\nWK-2 Final Solution: Professor Hosmer\n")

    targetDIR = input('Enter a Directory Path i.e. c:/ >>> ')
    print()
    
    resultTable = PrettyTable(['Path','Type', 'Size', 'UTC-Modified', 'UTC-Accessed', 'UTC-Created'])
    
    resultList = []
    
    try:
        fileList = os.listdir(targetDIR)
        for eachFile in fileList:

            path = os.path.join(targetDIR, eachFile)
            path = os.path.abspath(path)

            success, errInfo, fileSize, macList = GetFileMetaData(path)     
            
            if success:
                
                modTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(macList[0]))
                accTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(macList[1]))               
                creTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(macList[2]))  
                
                if os.path.isfile(path):
                    fileType = "File"
                elif os.path.isdir(path):
                    fileType = "Directory"
                elif os.path.islink(path):
                    fileType = "Link"
                else:
                    fileType = "Unknown"

                resultTable.add_row( [ path, fileType, fileSize, modTime, accTime, creTime] )                    
                
            else:
                print("Fail:      ", path, "Exception =     ", errInfo)

        resultTable.align = "l" 
        print(resultTable.get_string(sortby="Size", reversesort=True))        
              
    except Exception as err:
        print("\n\nScript Aborted     ", "Exception =     ", err)        
        
        
if __name__ == '__main__':
    
    main()
    print("Script End")
    
