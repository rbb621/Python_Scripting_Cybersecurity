'''
Introducing itertools
Professor Hosmer
August 2020
'''

import itertools   # Python standard library

print("Generate Combinations")
cnt = 0
for combinations in itertools.combinations("xyza", 2):
    print(combinations)

print("Generate Permuations")
for permutations in itertools.permutations("abc", 3):
    print(permutations)
    cnt+=1

print(cnt)    
print("Generate Product")
cnt = 0
for variations in range(4,8):
    for products in itertools.product("xyza", repeat=variations):
        print(products)    
        cnt+=1
print("Product Count: ", cnt)


# name = 'Rick'
# print(name[:5])

pw = ""

for eachChr in ('x', 'y', 'z'):
    pw = pw + "".join(eachChr)

print(pw)

d = {
    "file1.txt": 100,
    "file2.txt": 200,
    "file3.txt": 300
}

emptyList = list(d.items())
print(emptyList)