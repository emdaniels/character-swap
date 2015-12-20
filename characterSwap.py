#! /usr/bin/env python2

"""
Filename: characterSwap.py
Author: Emily Daniels
Date: November 2015
Purpose: Swaps the names and genders of characters in a novel.
"""

import re
import string
import os
import characterDict


class SwapText(object):

    def __init__(self, filename):
        self.filename = filename
        self.is_mixed = False
        self.text = ""
        self.split_text = []
        self.opposite_names = {}
        self.they_names = {}
        self.she_names = {}
        self.he_names = {}
        self.opposite_name_swapped_text = []
        self.they_name_swapped_text = []
        self.she_name_swapped_text = []
        self.he_name_swapped_text = []
        self.opposite_pronouns = {}
        self.they_pronouns = {}
        self.she_pronouns = {}
        self.he_pronouns = {}
        self.opposite_pronoun_swapped_text = []
        self.they_pronoun_swapped_text = []
        self.she_pronoun_swapped_text = []
        self.he_pronoun_swapped_text = []
        self.read_text()
        self.split_into_sentences()
        self.create_names()
        self.replace_names('opposite')
        self.replace_names('they')
        self.replace_names('she')
        self.replace_names('he')
        self.create_pronouns()
        self.replace_pronouns('opposite')
        self.replace_pronouns('they')
        self.replace_pronouns('she')
        self.replace_pronouns('he')
        self.write('opposite')
        self.write('they')
        self.write('she')
        self.write('he')

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

    def create_names(self):
        """
        Creates dictionaries of all name types, given created name csv files
        in a names folder.
        """
        self.opposite_names = characterDict.CreateDict(os.path.abspath(
            "names/opposite_names.csv"))
        self.they_names = characterDict.CreateDict(os.path.abspath(
            "names/they_names.csv"))
        self.she_names = characterDict.CreateDict(os.path.abspath(
            "names/she_names.csv"))
        self.he_names = characterDict.CreateDict(os.path.abspath(
            "names/he_names.csv"))

    def replace_names(self, type):
        """
        Replaces text with all name types.
        """
        if type == 'opposite':
            self.opposite_name_swapped_text = self.swap_names(
                self.opposite_names)
        if type == 'they':
            self.they_name_swapped_text = self.swap_names(
                self.they_names)
        if type == 'she':
            self.she_name_swapped_text = self.swap_names(
                self.she_names)
        if type == 'he':
            self.he_name_swapped_text = self.swap_names(
                self.he_names)

    def swap_names(self, names):
        """
        Replaces the original character names with the specified names.
        """
        name_swapped_text = []
        for line in self.split_text:
            for old, new in names:
                line = line.replace(old, new)
            name_swapped_text.append(line)
        return name_swapped_text

    def create_pronouns(self):
        """
        Creates dictionaries of all pronoun types, creating a path to where
        characterSwap is located.
        """
        self.opposite_pronouns = characterDict.CreateDict(
            os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         "opposite_pronouns.csv")))
        self.they_pronouns = characterDict.CreateDict(
            os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         "they_pronouns.csv")))
        self.she_pronouns = characterDict.CreateDict(
            os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         "she_pronouns.csv")))
        self.he_pronouns = characterDict.CreateDict(
            os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         "he_pronouns.csv")))

    def replace_pronouns(self, type):
        """
        Replaces text with all pronoun types.
        """
        if type == 'opposite':
            self.is_mixed = True
            self.opposite_pronoun_swapped_text = self.swap_pronouns(
                self.opposite_pronouns, self.opposite_name_swapped_text)
        if type == 'they':
            self.is_mixed = False
            self.they_pronoun_swapped_text = self.swap_pronouns(
                self.they_pronouns, self.they_name_swapped_text)
        if type == 'she':
            self.is_mixed = False
            self.she_pronoun_swapped_text = self.swap_pronouns(
                self.she_pronouns, self.she_name_swapped_text)
        if type == 'he':
            self.is_mixed = False
            self.he_pronoun_swapped_text = self.swap_pronouns(
                self.he_pronouns, self.he_name_swapped_text)

    def swap_pronouns(self, pronouns, name_swapped_text):
        """
        Replaces the original character pronouns with the specified pronouns.
        """
        pronoun_swapped_text = []
        for line in name_swapped_text:
            words = line.split()
            new_words = []
            for word in words:
                for old, new in pronouns:
                    word = self.check_word(word, old, new)
                new_words.append(word)
            new_line = ' '.join(new_words)
            pronoun_swapped_text.append(new_line)
        return pronoun_swapped_text

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
        elif self.is_mixed and word.lower() == new:
            if word[0].isupper():
                word = word.replace(word, old.title())
            else:
                word = word.replace(word, old)
        return word

    def write(self, type):
        """
        Writes each pronoun swapped text to a text file.
        """
        if type == 'opposite':
            self.write_text('Opposite_', self.opposite_pronoun_swapped_text)
        if type == 'they':
            self.write_text('They_', self.they_pronoun_swapped_text)
        if type == 'she':
            self.write_text('She_', self.she_pronoun_swapped_text)
        if type == 'he':
            self.write_text('He_', self.he_pronoun_swapped_text)

    def write_text(self, modifier, pronoun_swapped_text):
        """
        Writes the modified text to a text file.
        """
        regex = re.compile(r'.{1,80}(?:\s+|$)')
        with open(modifier + self.filename, "wb") as f:
            f.write('\n'.join(s.rstrip() for line in pronoun_swapped_text
                              for s in regex.findall(line)))
