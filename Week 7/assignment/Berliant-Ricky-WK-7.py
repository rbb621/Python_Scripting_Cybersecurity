'''
Searching for Images with PIL

Name: Ricky Berliant
Date: 10/11/2026
Instructor: Cameron Covington
Class: CYBV 312
Assignment: Scripting Assignment #7

'''

import sys
import os
from PIL import Image
from prettytable import PrettyTable

# User enters a folder directory
directPath = input("Enter a folder: ")


# Table Design - Listed in categories sorted by columns
tbl = PrettyTable(['File', 
                   'Ext', 
                   'Format', 
                   'Width', 
                   'Height', 
                   'Mode'])  

print("\nWeek 7 Starter Script\n")

for currentRoot, dirList, fileList in os.walk(directPath):
    for nextFile in fileList:
        fullPath = os.path.join(currentRoot, nextFile)

        if os.path.isfile(fullPath):
            ext = os.path.splitext(fullPath)[1]

            # Opening the images inside the directory
            try:
                with Image.open(fullPath) as im:
                    imageFormat = im.format
                    width = im.width
                    height = im.height
                    mode = im.mode
                    tbl.add_row([fullPath, ext, imageFormat, width, height, mode])

                
            except Exception as err:
                tbl.add_row([fullPath, ext, '[NA]', '[NA]', '[NA]', '[NA]'])

tbl.align = "l"
print (tbl.get_string(sortby="Ext"))



print("Script Done")
        