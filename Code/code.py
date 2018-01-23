from tkinter import *
import urllib3
from bs4 import BeautifulSoup
import string
import random


class TheCode:
    mystery_word = ""
    letters_found = []
    component_counter = -1

    def __init__(self, filename):
        self.mystery_word = self.create_word(filename.rstrip('\n'))
        for letter in self.mystery_word:
            self.letters_found.append("_")          #Create spaces equal to the word
                                                    #Make it a list so its mutable for
                                                    #-letter fill function

    def get_word(self):
        return self.mystery_word

    def create_word(self, filename):
        with open(filename) as f:
            word_list = []
            split = f.read().split()
            for word in split:
                cap_word = word.upper()
                word_list.append(cap_word)
        randomNum = random.randrange(0, len(word_list)-1)
        return word_list[randomNum]

    def encrypt_word(self):
        counter = 0
        word = self.mystery_word
        while counter < len(word):
           word =  word.replace(word[counter], "_")
           counter = counter + 1
        word_with_space = " ".join(word)
        return word_with_space

    def word_check(self, letter):
       found_letters = [i for i, ltr in enumerate(self.mystery_word) if ltr == letter]
       if len(found_letters) == 0:
           self.component_counter = self.component_counter + 1
           return self.component_counter
       else:
            self.letter_fill(found_letters, letter)
            return ""
    def letter_fill(self, letters, letter):
       for index in letters:
            self.letters_found[index] = letter

    def file_len(self):
        with open("Topics") as f:
            for i, l in enumerate(f):
                pass
        return i + 1