#! /usr/bin/env python2

"""
Filename: characterSwap.py
Author: Emily Daniels
Date: November 2015
Purpose: Swaps the gender of characters in The Adventures of Sherlock Holmes.
"""

import re
import string
from collections import defaultdict

def readText():
    """
    Reads the text from a text file.
    """
    with open("The_Adventures_of_Sherlock_Holmes.txt", "rb") as f:
        text = f.read()
    return text

def splitIntoSentences(text):
    """
    Split sentences on .?! "" and not on abbreviations of titles.
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
    """
    Replaces the original character names with those from the file.
    """
    nameSwapText = []
    names = [i.strip().split(',') for i in open('names.csv')]
    for line in text:
        for old, new in names:
            line = line.replace(old, new)
        nameSwapText.append(line)
    return nameSwapText

def replacePronouns(text):
    """
    Replaces the original character pronouns with those from the file.
    """
    pronounSwapText = []
    pronouns = [i.strip().split(',') for i in open('replacements.csv')]
    exclude = set(string.punctuation)
    for line in text:
        words = line.split()
        newWords = []
        for word in words:
            for old, new in pronouns:
                word = checkWord(word, old, new, exclude)
            newWords.append(word)
        newLine = ' '.join(newWords)
        pronounSwapText.append(newLine)
    return pronounSwapText

def checkWord(word, old, new, exclude):
    """
    Compares words without punctuation or case to those specified and replaces
    the word if needed.
    """
    strippedWord = ''.join(ch for ch in word if ch not in exclude)
    if strippedWord.lower() == old:
        if word[0].isupper():
            word = word.replace(word, new.title())
        else:
            word = word.replace(word, new)
    elif strippedWord.lower() == new:
        if word[0].isupper():
            word = word.replace(word, old.title())
        else:
            word = word.replace(word, old)
    return word


def writeText(text):
    """
    Writes the modified text to a text file.
    """
    with open("The_Adventures_of_Charlotte_Holmes.txt", "wb") as f:
        for line in text:
            f.write(line + ' ')


if __name__ == "__main__":
    text = readText()
    splitText = splitIntoSentences(text)
    nameSwapText = replaceNames(splitText)
    pronounSwapText = replacePronouns(nameSwapText)
    writeText(pronounSwapText)