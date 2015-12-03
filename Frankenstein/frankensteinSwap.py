#! /usr/bin/env python2

"""
Filename: frankensteinSwap.py
Author: Emily Daniels
Date: November 2015
Purpose: Swaps the names and genders of characters in
Frankenstein
"""

import characterSwap

if __name__ == "__main__":
    # swapped pronoun version
    characterSwap.SwapText(
        "Original_Frankenstein.txt",
        "Opposite_Frankenstein.txt",
        "opposite_frankenstein_names.csv",
        "opposite_frankenstein_pronouns.csv",
        True)
    # they pronoun version
    characterSwap.SwapText(
        "Original_Frankenstein.txt",
        "They_Frankenstein.txt",
        "they_frankenstein_names.csv",
        "they_frankenstein_pronouns.csv",
        False)
    # she pronoun version
    characterSwap.SwapText(
        "Original_Frankenstein.txt",
        "She_Frankenstein.txt",
        "she_frankenstein_names.csv",
        "she_frankenstein_pronouns.csv",
        False)
    # he pronoun version
    characterSwap.SwapText(
        "Original_Frankenstein.txt",
        "He_Frankenstein.txt",
        "he_frankenstein_names.csv",
        "he_frankenstein_pronouns.csv",
        False)
