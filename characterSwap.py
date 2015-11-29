#! /usr/bin/env python2

"""
Filename: characterSwap.py
Author: Emily Daniels
Date: November 2015
Purpose: Swaps the names and genders of characters in a novel.
"""

import re
import string


class SwapText(object):

    def __init__(self, filename, modified_filename, names_file, pronouns_file,
                 is_mixed):
        self.text = ""
        self.split_text = []
        self.name_swapped_text = []
        self.pronoun_swapped_text = []
        self.filename = filename
        self.modified_filename = modified_filename
        self.names_file = names_file
        self.pronouns_file = pronouns_file
        self.is_mixed = is_mixed
        self.read_text()
        self.split_into_sentences()
        self.replace_names()
        self.replace_pronouns()
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
            \s+               # Split on whitespace between sentences.
            """, re.IGNORECASE | re.VERBOSE)
        self.split_text = sentence_enders.split(self.text)
        return self.split_text

    def replace_names(self):
        """
        Replaces the original character names with those from the file.
        """
        names = [i.strip().split(',') for i in open(self.names_file)]
        for line in self.split_text:
            for old, new in names:
                line = line.replace(old, new)
            self.name_swapped_text.append(line)
        return self.name_swapped_text

    def replace_pronouns(self):
        """
        Replaces the original character pronouns with those from the file.
        """
        pronouns = [i.strip().split(',') for i in open(self.pronouns_file)]
        for line in self.name_swapped_text:
            words = line.split()
            new_words = []
            for word in words:
                for old, new in pronouns:
                    word = self.check_word(word, old, new)
                new_words.append(word)
            new_line = ' '.join(new_words)
            self.pronoun_swapped_text.append(new_line)
        return self.pronoun_swapped_text

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

    def write_text(self):
        """
        Writes the modified text to a text file.
        """
        regex = re.compile(r'.{1,80}(?:\s+|$)')
        with open(self.modified_filename, "wb") as f:
            f.write('\n'.join(s.rstrip() for line in self.pronoun_swapped_text
                              for s in regex.findall(line)))
