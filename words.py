# !/usr/bin/env python3

"""Docstring test dor this module
     this madule si almos useless its porpuse is only to test python
"""



import sys
from urllib.request import urlopen

def fetch_words(url):
    """ read text in a rul and save every word into a list"""
    story=urlopen(url)
    story_words=[]
    """    for byte in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)"""
    for byte in story:
        story_words.append(byte)
    story.close()
    return(story_words)


""" !!!!!!!!!!!!!!!!!! THIS DOCSTRING IS IN THE MIDDLE OF NOTHING"""


def print_items(items):
    """prints items from a iterable objcet to sreen"""
    for item in  items:
        print(item)

def main(url):
    """this is the main function"""
    words=fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    #http://sixty-north.com/c/t.txt
    print("Enter url: ")
    url=input()
    main(url)
