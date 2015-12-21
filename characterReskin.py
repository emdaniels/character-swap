#! /usr/bin/env python2

"""
Filename: characterReskin.py
Author: Emily Daniels
Date: December 2015
Purpose: Reskins characters in a novel.
"""

import re
import string
import characterDict
import os
import random


class Reskin(object):

    def __init__(self, filename):
        self.filename = filename
        self.split_text = []
        self.swapped_text = []
        self.augmented_text = []
        self.replacers = {}
        self.read_text()
        self.split_into_sentences()
        self.create_replacers()
        self.replace_words()
        self.augment_text()
        self.write_text()

    def read_text(self):
        """
        Reads the text from a text file.
        """
        with open(self.filename, "rb") as f:
            self.text = f.read()
        return self.text

    def split_into_sentences(self):
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
            (?<!  St\.   )    # Don't end sentence on "St."
            (?<!  M\.   )    # Don't end sentence on "M."
            \s+               # Split on whitespace between sentences.
            """, re.IGNORECASE | re.VERBOSE)
        self.split_text = sentence_enders.split(self.text)
        return self.split_text

    def create_replacers(self):
        """
        Creates dictionaries of replacer words, creating a path to where
        characterReskin is located.
        """
        self.replacers = characterDict.CreateDict(
            os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         "replacers.csv")))

    def replace_words(self):
        """
        Identifies phrases to be modified and replaces the words.
        """
        for line in self.split_text:
            words = line.split()
            new_words = []
            for word in words:
                for old, new in self.replacers:
                    word = self.check_word(word, old, new)
                new_words.append(word)
            new_line = ' '.join(new_words)
            self.swapped_text.append(new_line)
        return self.swapped_text

    def check_word(self, word, old, new):
        """
        Checks and replaces words based on the word lists.
        """
        # remove word starters
        starter = False
        add_starter = ""
        # remove word enders
        ender = False
        add_ender = ""
        for punc in set(string.punctuation):
            while word.startswith(punc):
                starter = True
                add_starter = punc + add_starter
                word = word[1:]
            while word.endswith(punc):
                ender = True
                add_ender = punc + add_ender
                word = word[:-1]
        # remove possession
        possessive = False
        if word.endswith("'s"):
            possessive = True
            word = word[:-2]
        # compare word to word lists
        word = self.replace_word(word, old, new)
        # add back word enders and possession
        if possessive:
            word += "'s"
        if ender:
            word += add_ender
        if starter:
            word = add_starter + word
        return word

    def replace_word(self, word, old, new):
        """
        Compares words without punctuation or case and replaces
        the word if needed.
        """
        if word.lower() == old:
            if word[0].isupper():
                word = word.replace(word, new.title())
            else:
                word = word.replace(word, new)
        return word

    def augment_text(self):
        """
        Augments the text with words to describe the body.
        """
        identifiers = [i.rstrip('\n') for i in open(
            os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         "identifiers.csv")))]
        for line in self.swapped_text:
            words = line.split()
            new_words = []
            for word in words:
                for id in identifiers:
                    word = self.add_word(word, id)
                new_words.append(word)
            new_line = ' '.join(new_words)
            self.augmented_text.append(new_line)
        return self.augmented_text

    def add_word(self, word, id):
        modifiers = ["dark", "caramel", "tawny", "bronzed"]
        if word == id:
            # choose a random modifier and add as an adjective
            word = random.choice(modifiers) + ' ' + word
        return word

    def write_text(self):
        """
        Writes the modified text to a text file.
        """
        regex = re.compile(r'.{1,80}(?:\s+|$)')
        with open("Reskinned_" + self.filename, "wb") as f:
            f.write('\n'.join(s.rstrip() for line in self.augmented_text
                              for s in regex.findall(line)))
