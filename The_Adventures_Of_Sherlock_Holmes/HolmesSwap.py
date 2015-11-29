#! /usr/bin/env python2

"""
Filename: holmesSwap.py
Author: Emily Daniels
Date: November 2015
Purpose: Swaps the names and genders of characters in
The Adventures of Sherlock Holmes
"""

import characterSwap

if __name__ == "__main__":
    # swapped pronoun version
    characterSwap.SwapText(
        "Original_The_Adventures_of_Sherlock_Holmes.txt",
        "Opposite_The_Adventures_of_Charlotte_Holmes.txt",
        "opposite_holmes_names.csv",
        "opposite_holmes_pronouns.csv",
        True)
    # they pronoun version
    characterSwap.SwapText(
        "Original_The_Adventures_of_Sherlock_Holmes.txt",
        "They_The_Adventures_of_Hemlock_Holmes.txt",
        "they_holmes_names.csv",
        "they_holmes_pronouns.csv",
        False)
    # she pronoun version
    characterSwap.SwapText(
        "Original_The_Adventures_of_Sherlock_Holmes.txt",
        "She_The_Adventures_of_Charlotte_Holmes.txt",
        "she_holmes_names.csv",
        "she_holmes_pronouns.csv",
        False)
    # he pronoun version
    characterSwap.SwapText(
        "Original_The_Adventures_of_Sherlock_Holmes.txt",
        "He_The_Adventures_of_Sherlock_Holmes.txt",
        "he_holmes_names.csv",
        "he_holmes_pronouns.csv",
        False)
