#! /usr/bin/env python2

"""
Filename: characterSwap.py
Author: Emily Daniels
Date: November 2015
Purpose: Swaps the names and genders of characters in a novel.
"""

import re
import string
from collections import defaultdict


def read_text(filename):
    """
    Reads the text from a text file.
    """
    with open(filename, "rb") as f:
        text = f.read()
    return text


def split_into_sentences(text):
    """
    Split sentences on .?! "" and not on abbreviations of titles.
    """
    sentence_enders = re.compile(r"""
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
    return sentence_enders.split(text)


def replace_names(text, names_file):
    """
    Replaces the original character names with those from the file.
    """
    name_swapped_text = []
    names = [i.strip().split(',') for i in open(names_file)]
    for line in text:
        for old, new in names:
            line = line.replace(old, new)
        name_swapped_text.append(line)
    return name_swapped_text


def replace_pronouns(text, pronouns_file):
    """
    Replaces the original character pronouns with those from the file.
    """
    pronoun_swapped_text = []
    pronouns = [i.strip().split(',') for i in open(pronouns_file)]
    for line in text:
        words = line.split()
        new_words = []
        for word in words:
            for old, new in pronouns:
                word = check_word(word, old, new)
            new_words.append(word)
        new_line = ' '.join(new_words)
        pronoun_swapped_text.append(new_line)
    return pronoun_swapped_text


def check_word(word, old, new):
    """
    Checks and replaces words based on the word lists.
    """
    # remove word enders
    ender = False
    add_ender = ""
    for punc in set(string.punctuation):
        if word.endswith(punc):
            ender = True
            add_ender = punc
            word = word[:-1]
    # remove possession
    possessive = False
    if word.endswith("'s"):
        possessive = True
        word = word[:-2]
    # compare word to word lists
    word = replace_word(word, old, new)
    # add back word enders and possession
    if possessive:
        word += "'s"
    if ender:
        word += add_ender
    return word


def replace_word(word, old, new):
    """
    Compares words without punctuation or case and replaces
    the word if needed.
    """
    if word.lower() == old:
        if word[0].isupper():
            word = word.replace(word, new.title())
        else:
            word = word.replace(word, new)
    elif word.lower() == new:
        if word[0].isupper():
            word = word.replace(word, old.title())
        else:
            word = word.replace(word, old)
    return word


def write_text(text, modified_filename):
    """
    Writes the modified text to a text file.
    """
    with open(modified_filename, "wb") as f:
        for line in text:
            f.write(line + ' \n')


if __name__ == "__main__":
    filename = "The_Adventures_of_Sherlock_Holmes.txt"
    modified_filename = "The_Adventures_of_Charlotte_Holmes.txt"
    names_file = "holmes_names.csv"
    pronouns_file = "holmes_pronouns.csv"
    text = read_text(filename)
    split_text = split_into_sentences(text)
    name_swapped_text = replace_names(split_text, names_file)
    pronoun_swapped_text = replace_pronouns(name_swapped_text, pronouns_file)
    write_text(pronoun_swapped_text, modified_filename)
