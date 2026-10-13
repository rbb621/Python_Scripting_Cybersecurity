'''
Python Logging Example
Professor Hosmer
August 2020
'''
import logging      # Python Standard Logging Library

# Turn on Logging

print("\nSample Python Logging\n")
logging.basicConfig(filename='ScriptLog.txt',level=logging.DEBUG,format='%(process)d-%(levelname)s-%(asctime)s %(message)s')


with open("test.txt", 'r') as test:
    data = test.read()
    logging.info("We successfully read the file")

logging.info('Script Started')
logging.warning('Osmanthis Wine tastes the same  ')
logging.error('Lonely Lonely Lost Soul    ')
logging.critical('Sample Critical Message ')

print("\nScript Complete")