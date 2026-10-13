'''
For this assignment you will be using your preferred Integrated Development Environment and the Python Shell.

Step 1:

Execute the following statement (copy and paste into the WingIDE Python Shell) then press enter.
'''

#2) What is the length of the textStr? 
def lenghtOfTextStr(text):

    countCharacters = 0

    for ch in range(len(text)):
        countCharacters += 1

    print("Number of characters: ")

    return countCharacters

# 3) Create a list of wordsFound in textStr. (hint: use the method .split() )
def listOfWords(words):

    updatedStr = words.split()

    return updatedStr

#4) Sort the wordsFound list.

def sortWords(words):
    wordsSplit = words.split()
    wordsSplit.sort()

    return wordsSplit


# #5) How many individual words (i.e., strings) were created?

def individualWords(words):
    countWords = 0

    updatedStr = words.split()

    for words in updatedStr:
        countWords += 1

    print("Number of words: ")
    return countWords


# #6) How many words in the wordsFound list are in Title case?

def titleCaseWords(words):
    count = 0

    for word in words:
        if word.istitle():
            count += 1

    print('Number of Title Cased Words: ')

    return count


def main():

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
upon for such trips.
'''

    print(lenghtOfTextStr(textStr))
    print(listOfWords(textStr))
    print(sortWords(textStr))
    print(titleCaseWords(textStr))
    print(individualWords(textStr))

if __name__ == '__main__':
    main()


'''
Step 2:

Using the Python shell within WingIDE determine the following characteristics that are associated with variable textStr:

1) What is the type of the variable/object is textStr?

textStr is a string data type. As long as there are any text, numbers, special characters inside the quotes will always be considered to be a string

2) What is the length of the textStr?


3) Create a list of wordsFound in textStr. (hint: use the method .split() )
4) Sort the wordsFound list.
5) How many individual words (i.e., strings) were created?
6) How many words in the wordsFound list are in Title case? (hint: use the method .istitle() )

Once completed Copy and Paste your results from your WingIDE Session into a 
text file with the naming convention: LastName-Firstname-WK1.txt




'''