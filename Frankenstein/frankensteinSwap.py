#! /usr/bin/env python2

"""
Filename: frankensteinSwap.py
Author: Emily Daniels
Date: November 2015
Purpose: Swaps the names and genders of characters in Frankenstein
"""

import characterSwap
import characterReskin

if __name__ == "__main__":
    characterSwap.SwapText("Frankenstein.txt")
    characterReskin.Reskin("Opposite_Frankenstein.txt")
    characterReskin.Reskin("They_Frankenstein.txt")
    characterReskin.Reskin("She_Frankenstein.txt")
    characterReskin.Reskin("He_Frankenstein.txt")
