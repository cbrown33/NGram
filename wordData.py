"""
wordData.py
Written by Conor Brown
"""

from rit_lib import *

class YearCount(struct):
    _slots = ((int, 'year'), (int, 'count'))

class WordTrend(struct):
    _slots = ((str, 'word'), (float, 'trend'))

def readWordFile(fileName):
    """
    reads a file and creates a dictionary of wordCount objects from the file
    :param fileName: the file
    :return: the created dictionary
    """
    dct = dict()
    clist = list()
    with open('data/' + fileName) as f:
        for line in f:
            line = line.strip()
            if len(line) <= 5:
                if not len(clist) == 0:
                    dct[key] = clist
                    clist = list()
                key = line
            elif line[4] != ',':
                if not len(clist) == 0:
                    dct[key] = clist
                    clist = list()
                key = line
            else:
                clist.append(YearCount(int(line[0:4]), int(line[5:])))
        dct[key] = clist
        f.close()
    return dct

def totalOccurrences(word, words):
    """
    finds the total occurrences of a word in a given dictionary
    :param word: the word
    :param words: the dict
    :return: the number of occurrences
    """
    ct = 0
    if word in words:
        lst = words[word]
        for i in range(len(lst)):
            ct += lst[i].count
    return ct

def main():
    """
    asks for a word input, then calculates the number of times it occurs in the file
    :return:
    """
    file = input("Enter the name of a file: ")
    wd = input('Enter a word: ')
    wdc = str(wd + ':')
    print('Total occurrences of', wdc, totalOccurrences(wd, readWordFile(file)))

if __name__ == '__main__':
    main()