#! /usr/bin/python3

import re

def makeUpper(word):
    return word if len(word) == 0 else (word if word[0].isupper() else word[0].upper() + word[1:])
    
def addPeriod(word):
    return word if len(word) == 0 else (word if word[-1] == '.' else word + '.')
# I wrote the above functions to beautify the output.

contents = input("Enter the name of the file you want to read: ")

try: # Try and catch in case the file entered doesn't exist or can't be read.
    with open(contents) as thisFile: 
        num = 1 # Line numbering. 

        p1 = re.compile(r'(?:,\s+(?:for|and|nor|but|or|yet|so)\s+|[.]\s+)', re.IGNORECASE) # Using syntax and usage info from the 're' package's
        p2 = re.compile(r'\s*\n')                                                          # documentation page.
        print(f"\"{thisFile.name}\" Thoughts:\n")
        for line in thisFile:                   # Iterating through each line of the text file.
            subline = p1.split(p2.sub('',line)) # Removing newline characters. CHOMP! Then splitting along p1's regex.
            for phrases in subline:             # Iterating through each phrase/clause in subline. 
                print(f"{num}: {addPeriod(makeUpper(phrases))}\n") # Printing desired output.
                num += 1                        # Increment line numbering.
                
except IOError:
    print("That file doesn't exist or can't be read. Please try again with another file.") # Letting the user know that something went wrong.
