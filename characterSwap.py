#! /usr/bin/env python2

"""
    Filename: characterSwap.py
    Author: Emily Daniels
    Date: November 2015
    Purpose: Swaps character gender in The Adventures of Sherlock Holmes.
    """

import re
from collections import defaultdict

def readText():
    """
    Reads the text from a text file.
    """
    with open("A_Scandal_In_Bohemia.txt", "rb") as f:
        text = f.read()
    return text

def splitIntoSentences(text):
    """
        Split sentences on .?! "" and not on abbreviations of titles.
        Used for reference: http://stackoverflow.com/a/8466725
        """
    sentenceEnders = re.compile(r"""
        # Split sentences on whitespace between them.
        (?:               # Group for two positive lookbehinds.
        (?<=[.!?])      # Either an end of sentence punct,
        | (?<=[.!?]['"])  # or end of sentence punct and quote.
        )                 # End group of two positive lookbehinds.
        (?<!  Mr\.   )    # Don't end sentence on "Mr."
        (?<!  Mrs\.  )    # Don't end sentence on "Mrs."
        (?<!  Ms\.   )    # Don't end sentence on "Ms."
        (?<!  Jr\.   )    # Don't end sentence on "Jr."
        (?<!  Dr\.   )    # Don't end sentence on "Dr."
        (?<!  Prof\. )    # Don't end sentence on "Prof."
        (?<!  Sr\.   )    # Don't end sentence on "Sr."
        \s+               # Split on whitespace between sentences.
        """, re.IGNORECASE | re.VERBOSE)
    return sentenceEnders.split(text)

def replaceNames(text):
    nameSwapText = []
    names = [i.strip().split(',') for i in open('names.csv')]
    for line in text:
        for oldname, newname in names:
            line = line.replace(oldname, newname)
        nameSwapText.append(line)
    return nameSwapText

def replaceSexes(text):
    sexSwapText = []
    sexes = [i.strip().split(',') for i in open('replacements.csv')]
    for line in text:
        for oldsex, newsex in sexes:
            line = line.replace(oldsex, newsex)
        sexSwapText.append(line)
    return sexSwapText
   
def writeText(text):
    """
    Writes the modified text to a text file.
    """
    with open("A_Scandal_In_Bohemia_CH.txt", "wb") as f:
        for line in text:
            f.write(line + ' ')


if __name__ == "__main__":
    text = readText()
    splitText = splitIntoSentences(text)
    #print splitText
    nameSwapText = replaceNames(splitText)
    #print nameSwapText
    sexSwapText = replaceSexes(nameSwapText)
    #print sexSwapText
    writeText(sexSwapText)
    print "done!"