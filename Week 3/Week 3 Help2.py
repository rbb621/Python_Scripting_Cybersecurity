'''
Script:  Week 3 Scripting Assignment Starting Point
Author:  Cameron Covington
Date:    Nov 2020
Version: .50
Purpose: Directory Metadata and Hashing

ASSIGNMENT DETAILS
Create a new script with the following requirements:
Allow the user to specify a starting directory using the built-in Python input() function

Using os.walk()
Acquire the following information for each file (sub-directories included):
File Path (absolute path)
File Size
MAC Times (in human readable form)
SHA-256 Hash value

Store the results in a prettytable with the headings:
AbsPath, FileSize, LastModified, LastAccess, CreatedTime, HASH

Display the prettytable sorted by FileSize
Catch and report any errors

Submit:
1) Your final script
2) A screenshot from within WingIDE of a successful execution
    
'''

''' IMPORT STANDARD LIBRARIES '''
import os       # File System Methods
import sys      # System Methods
import time     # Time Conversion Methods
import hashlib  # Python standard library hashlib


''' IMPORT 3RD PARTY LIBRARIES '''
from prettytable import PrettyTable # pip install prettytable

''' DEFINE PSEUDO CONSTANTS '''
#Change to directory as required
DIR = "/Users/cameroncovington/Dropbox/Arizona/CYBV312/Week 3"

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
    
    try:
        # Perform the os.walk, starting at the target directory
        # TODO: Change this from a pseudo-constant to a user-specified directory using input()
        for root, dirs, fileList in os.walk(DIR):
            # Print current Root directory
            print('root: ', root)
            # Print current directory
            print('dirs: ', dirs)
            # Print file list
            print('files: ', fileList)
            
            # For each of the files in the file list, do the following:
            for nextFile in fileList: 
                # Get the absolute path of the file--to be used for reporting and getting the file hash
                path = os.path.join(root, nextFile)
                absPath = os.path.abspath(path)
                # Call the GetFileMetadata function (from week 2 solution)
                success, errInfo, fileSize, macList = GetFileMetaData(absPath)
                
                # Open each file in read binary mode
                with open(absPath, 'rb') as targetFile:
                    # Read the contents of the file and get the file hash
                    fileContents = targetFile.read()
                    sha256Obj = hashlib.sha256()
                    sha256Obj.update(fileContents)
                    hexDigest = sha256Obj.hexdigest()
                    
                    # Print stats for each file encountered
                    # TODO: Format this output into a PrettyTable
                    print("File name: ", absPath)
                    print("Hex digest: ", hexDigest)
                    print("Modified Time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(macList[0])))
                    print("Accessed Time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(macList[1])))
                    print("Created Time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(macList[2])))
                    print("File size: ", fileSize)
                    print("="*50)
       
    except Exception as err:
        print("\n\nScript Aborted     ", "Exception =     ", err)        
    
    print("Script end")