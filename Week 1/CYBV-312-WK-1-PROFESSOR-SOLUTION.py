'''
Week One Solution
Professor Hosmer

Assignment
Using the Python shell within WingIDE determine the following characteristics associated with textStr:
Copy and then Paste the results from WingIDE into a text file and submit this as your assignment 
(showing all the work)

1) What is the type of textStr? 
2) What is the length of the textStr? 
3) Create a list named wordsFound in textStr hint using the  method .split()
4) Sort the wordsFound list
5) How many individual words (i.e. strings) were created? 
6) How many words in the wordsFound list are in Title case, hint use the method .istitle()

'''

textStr = ''' Between ten and eleven o’clock that morning two messengers were sent in
a taxicab from the East River National Bank, at Broadway and Third
street, to draw $25,000 in currency from the Produce Exchange National
Bank, at Broadway and Beaver street, in the downtown financial district,
and bring it uptown. This transfer of money had been made several times
a week for so long a period without danger or loss that the messengers
were unarmed. One of them, Wilbur F. Smith, was an old man who had been
in the service of the bank thirty-five years, and the other was a mere
boy, named Wardle, seventeen years old. The taxicab man, an Italian
named Geno Montani, seemed almost a trusted employee, too, for he
operated two cabs from a stand near the bank, and was frequently called
upon for such trips.'''

print(textStr)
print("textStr Type:       ", type(textStr))
print("textStr Len:        ",len(textStr))
wordList = textStr.split()
wordList.sort()
print("wordsFound All Words Len:       ",len(wordList))
uniqueWordSet = set(wordList)
uniqueWordList = list(uniqueWordSet)
uniqueWordList.sort()
print("wordsFound Unique Words Len:    ",len(uniqueWordList))

# Simple is better than complex
titleCount = 0
for eachWord in wordList:
    if eachWord.istitle():
        print(eachWord)
        titleCount += 1

print("Title Case Words Readable Method: ",titleCount)

# Complex, cool but unreadable   
# Don't do this, this is counter to making Python readable as english
titleCount = len([x for x in wordList if x.istitle()])
print("Title Case Words Complex Method:  ",titleCount)

print("\nUnique Words")
for eachWord in uniqueWordList:
    print(eachWord)

        
