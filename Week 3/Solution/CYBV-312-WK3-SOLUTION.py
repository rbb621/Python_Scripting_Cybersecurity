'''
Week 3 Solution
CYBV 312
Professor Hosmer
June 2022
'''

# Python Standard Libaries 
import os
import hashlib
import time

# Python 3rd Party Libraries
from prettytable import PrettyTable     # pip install prettytable

print("\n\nWeek-3 Assignment Solution - Professor Hosmer \n")

while True:
    DIR = input("Please Enter Starting Directory: ")
    if not os.path.isdir(DIR):
        print("invalid directory...please enter a valid directory path")
        continue
    else:
        break

''' Create the pretty table '''
tbl = PrettyTable(['Path','Status','FileSize','LastModified', 'LastAccess', 'Created', 'SHA-256 HASH', 'Error Info'])  

# Start Walking the file system
print("Walking: ", DIR, "\n")

for currentRoot, dirList, fileList in os.walk(DIR):
    
    for nextFile in fileList:
        
        try:
            
            fullPath = os.path.join(currentRoot, nextFile)
            absPath = os.path.abspath(fullPath)
            
            stats = os.stat(absPath)
            
            fileSize = stats.st_size
            modEPOCH  = stats.st_mtime
            accEPOCH  = stats.st_atime
            creEPOCH  = stats.st_ctime
            
            modTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(modEPOCH))
            accTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(accEPOCH))               
            creTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(creEPOCH))
            
            with open(absPath, 'rb') as targetFile:
                fileContents = targetFile.read()
                hashObj = hashlib.sha256()
                hashObj.update(fileContents)
                hexDigest = hashObj.hexdigest()
            
            tbl.add_row( [ absPath, 'OK', fileSize, modTime, accTime, creTime, hexDigest, ''] ) 
            
        except Exception as err:
            tbl.add_row( [nextFile, 'ERR', 0, 'ERR', 'ERR', 'ERR', 'ERR', str(err)] ) 
            continue

tbl.align = "l" # align the columns left justified

# display the tables
print("RESULTS: Sorted by LastModified Date")
print (tbl.get_string(sortby="LastModified", reversesort=True))

print("\n\nRESULTS: Sorted by FileSize")
print (tbl.get_string(sortby="FileSize", reversesort=True))

print("\n\nRESULTS: Sorted by Path")
print (tbl.get_string(sortby="Path"))

''' Create CSV File Name based on date and time '''
now = time.time()
timeString = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime(now))
csvFileName = "WK-3-"+timeString+".csv"
print(csvFileName)

''' Open the CSV File and write the contents'''
with open(csvFileName, 'w') as outFile:
    csvOut = tbl.get_csv_string(sortby="Path")
    outFile.write(csvOut)
    

print("\nScript-End\n")