'''
Ricky Berliant
CYBV 312
Cameron Covington
10/4/2026
Week #6 Scripting Assignment
'''

# Python Standard Libaries 
import os
import re
import logging
import platform
import socket
import uuid
import hashlib
import time
import datetime

import psutil  # pip install psutil

def getSystemInfo():
    try:
        info={}
        info['\tplatform']=platform.system()
        info['\tplatform-release']=platform.release()
        info['\tplatform-version']=platform.version()
        info['\tarchitecture']=platform.machine()
        info['\thostname']=socket.gethostname()
        info['\tip-address']=socket.gethostbyname(socket.gethostname())
        info['\tmac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['\tprocessor']=platform.processor()
        info['\tram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return info
    except Exception as e:
        logging.exception(e)
        return False


def main():
    
    # Remove any old logging script
    if os.path.isfile('Berliant-Ricky-WK-6.txt'):   # REPLACE YOURNAME with Your Name
        os.remove("Berliant-Ricky-WK-6.txt")
    
    # configure the python logger, Replace YOURNAME
    logging.basicConfig(filename='Berliant-Ricky-WK-6.txt', 
                        level=logging.DEBUG, 
                        format='%(process)d-%(levelname)s-%(asctime)s %(message)s')
    logging.info("Script Start\n")
    
    investigator = input("Investigator Name:  ")   # Enter Your Name at this prompt
    organization = input("Class Code  :       ")   # Enter the Class at this prompt i.e. CYBV-312 YOUR SECTION
    
    sysInfo = getSystemInfo()

    # If file exists
    if sysInfo:
        logging.info('Investigator: %s', investigator)
        logging.info('Organization: %s', organization)
        logging.info('Purpose     : Week #6 CYBV 312 Assignment')
        logging.info('='* 40 + "\n")

        logging.info('***** System Information *****')
        for key, values in sysInfo.items():
            logging.info('%s: %s', key, values)
        logging.info('='* 40 + "\n")

        dirPath = input('Enter a directory path: ')
        logging.info('User Specified Directory: %s', dirPath)

        fileCount = 0
        beginTime = time.time()
    
    for currentRoot, dirList, fileList in os.walk(dirPath):
        for nextFile in fileList:
            fileCount += 1
            fullPath = os.path.join(currentRoot, nextFile)
            absPath = os.path.abspath(fullPath)

            # Get Metadata
            try:
                metaData = os.stat(absPath)
                fileSize = metaData.st_size

                # Convert timestamps to make it readable string
                timeLastAccess = metaData.st_atime
                timeLastModified = metaData.st_mtime
                timeCreated = metaData.st_ctime

                # Convert timestamps to readable string format
                timeLastModified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(metaData.st_mtime))
                timeLastAccess = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(metaData.st_atime))
                timeCreated = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(metaData.st_ctime))


                # Create SHA-256 Hash    
                with open(absPath, 'rb') as target:
                    fileContents = target.read()
                    sha256Obj = hashlib.sha256()
                    sha256Obj.update(fileContents)
                    hexDigest = sha256Obj.hexdigest()

                    logging.info('File Processed:')
                    logging.info('\tPath: %s', absPath)
                    logging.info('\tFile Size: %s', fileSize)
                    logging.info('\tLast-Modified: %s', timeLastModified)
                    logging.info('\tLast-Accessed: %s', timeLastAccess)
                    logging.info('\tCreated: %s', timeCreated)
                    logging.info('\tSHA-256: %s', hexDigest)
                    logging.info("=" * 70 + "\n")


            except Exception as err:
                logging.info("Exception: %s", err)


    # Elapse Time (Optional)
    endTime = time.time()
    elapsedTime = int(endTime - beginTime)
    delta = datetime.timedelta(seconds=round(endTime - beginTime))


    #Displaying elapse time Results
    logging.info("=" * 40 + "\n")
    logging.info('Files Processed:       %d', fileCount)
    logging.info('Elapsed Time hh:mm:ss: %s \n', delta)
    logging.info('Status: Script Ended ')


# Run main()
if __name__ == '__main__':
    
    print("\n\nWeek-6 Logging Starter Script - Ricky Berliant \n")
    main()
    print("\nScript End")

