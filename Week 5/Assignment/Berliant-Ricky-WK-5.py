'''
Name: Ricky Berliant
Instructor: Cameron Covington
Date: 9/27/2026
Class: CYBV 312
'''


import itertools
import hashlib
import pickle

# Open the destination File (write binary)
pickleFileWrite = open('./rainbow.db', 'wb') 

#Create any python object
rainbowTable = {}


# Create a "dynamic" rainbow table of all password 4-7 characters in length
password = 'abc123&'

for variations in range(4,8):
    for products in itertools.product(password, repeat=variations):
        pw = ""
        md5Hash = hashlib.md5()
        for eachChr in products:
            pw = pw+"".join(eachChr)
        pw = bytes(pw, 'ascii')
        md5Hash.update(pw)
        md5Digest = md5Hash.hexdigest()
        rainbowTable[md5Digest] = pw

pickle.dump(rainbowTable, pickleFileWrite)                      
pickleFileWrite.close() 

pickleFileRead = open('./rainbow.db', 'rb')

retrievedList = pickle.load(pickleFileRead)

entryList = list(retrievedList.items())

print("Dictionary Length:", len(retrievedList))
print("First-Five:",entryList[:5])
print("Last-Five: ",entryList[-5:])

pickleFileRead.close()
