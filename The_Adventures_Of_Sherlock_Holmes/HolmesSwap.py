#! /usr/bin/env python2

"""
Filename: holmesSwap.py
Author: Emily Daniels
Date: November 2015
Purpose: Swaps the names and genders of characters in
The Adventures of Sherlock Holmes
"""

import characterSwap
import characterReskin

if __name__ == "__main__":
    characterSwap.SwapText("The_Adventures_of_Sherlock_Holmes.txt")
    characterReskin.Reskin("Opposite_The_Adventures_of_Sherlock_Holmes.txt")
    characterReskin.Reskin("They_The_Adventures_of_Sherlock_Holmes.txt")
    characterReskin.Reskin("She_The_Adventures_of_Sherlock_Holmes.txt")
    characterReskin.Reskin("He_The_Adventures_of_Sherlock_Holmes.txt")
