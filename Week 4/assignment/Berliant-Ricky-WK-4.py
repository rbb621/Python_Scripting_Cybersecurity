'''
Name: Ricky Berliant
Instructor: Cameron Covington
Date: 9/20/2026
Class: CYBV 312
Assignment: Week #4 Scripting Assignment
'''

# Import modules
import re 
import sys
import os
from prettytable import PrettyTable

# Create URL regular expoession 
urlPattern = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w\.?=%&=\-@/$,]*')

# Create an empty dictionary
chunkSize = 65535

# Create an empty dictionary
binaryDict = {}


try:

    assignmentFile = input('Enter the name of a large File: ')

    count = 0

    if os.path.isfile(assignmentFile): 
        with open(assignmentFile, 'rb') as fileBinary:
            while True:
                fileChunk = fileBinary.read(chunkSize)

                if not fileChunk:
                    break

                urlMatches = urlPattern.findall(fileChunk)
                
                for eachURL in urlMatches:
                    if eachURL in binaryDict:
                        count = binaryDict[eachURL]
                        count += 1
                        binaryDict[eachURL] = count
                    else:
                        binaryDict[eachURL] = 1

    else:
        sys.exit("File does not exist")

                        

    print('Generating Sorted Result Table')
    table = PrettyTable(['Occurs', 'URL'])

    # Creating a Pretty Table
    for url, occurs in binaryDict.items():
        table.add_row([occurs, url])
    table.align = 'l'
    print(table.get_string(sortby="Occurs", reversesort=True))


except Exception as err:
    sys.exit("\nException: "+str(err)+ "Script Aborted")