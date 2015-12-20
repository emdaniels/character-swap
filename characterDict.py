#! /usr/bin/env python2

"""
Filename: characterDict.py
Author: Emily Daniels
Date: December 2015
Purpose: Creates a dictionary from a file of paired words separated by commas.
"""


class CreateDict(object):

    def __init__(self, file):
        self.file = file
        self.characterDict = {}
        self.create()

    def create(self):
        self.characterDict = [i.strip().split(',') for i in open(self.file)]
        return self.characterDict

    def __iter__(self):
        return iter(self.characterDict)
