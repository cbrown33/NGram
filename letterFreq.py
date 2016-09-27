"""
letterFreq.py
Written by Conor Brown
"""

from wordData import *
from operator import *

def letterFreq(words):
    """
    Determines the frequency of the letters in all of the words in the dict words
    :param words: a dict full of YearCount objects
    :return: the string of letters from most to least frequent
    """
    lst = list(words.keys())
    counts = creAlphDict()
    for key in lst:
        num = 0
        for node in range(len(words[key])):
            num += words[key][node].count
        for ch in key:
            counts[ch] += num
    output = str()
    sorteddict = sorted(counts.items(), key=itemgetter(1))
    sorteddict.reverse()
    for i in range(len(sorteddict)):
        output = output + sorteddict[i][0]
    return output

def creAlphDict():
    """
    Creates a dictionary with all of the letters in the alphabet with values of 0
    :return: the dict
    """
    x = {}
    for ch in 'qwertyuiopasdfghjklzxcvbnm':
        x[ch] = 0
    return x

def main():
    letterFreq(readWordFile(input("Enter the name of a file: ")))

if __name__ == '__main__':
    main()