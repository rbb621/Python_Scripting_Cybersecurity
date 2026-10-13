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

print("\nWeek 7 Starter Script\n")
while True:
    path = input("\nFileName to Examine Q to Quit: ")
    if path.lower() == 'q':
        break
    if os.path.isfile(path):
        ext = os.path.splitext(path)[1]
        try:
            with Image.open(path) as im:
                print("File Details")
                print("Extension:    ", ext)
                print("Image Format: ", im.format)
                print("Image Width:  ", im.width,  "Pixels")
                print("Image.Height: ", im.height, "Pixels")
                print("Image.Mode:   ", im.mode) 
        except Exception as err:
            print("File is not a known Image Type: ", path)
    else:
        print("Path Provide is Not a File")



print("Script Done")
        