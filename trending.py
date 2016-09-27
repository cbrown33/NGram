"""
trending.py
Written by Conor Brown
"""

from wordData import *
from operator import *

def trending(words, startYr, endYr):
    """
    takes a dict of words and two year endpoints then calculates the trend of all eligible words
    :param words: the dict of words
    :param startYr: the year to start calculating trends
    :param endYr:  the year to end calculating trends
    :return: a sorted list of WordTrend objects by dec trend value
    """
    keys = list(words.keys())
    trendlist = list()
    for i in range(len(keys)):
        n = calctrend(words[keys[i]], startYr, endYr)
        if n is not None:
            trendlist.append(WordTrend(keys[i], n))
    return sorted(trendlist, key=attrgetter('trend'), reverse=True)

def calctrend(wlist, st, end):
    """
    calculates the trend value of a list with a given start and end year, if there is a value
    :param wlist: the list to be calculated
    :param st: the start year
    :param end: the end year
    :return: the value or None
    """
    endval = ''
    stval = ''
    for i in range(len(wlist)):
        if end >= wlist[i].year:
            if wlist[i].year == st:
                if wlist[i].count < 1000:
                    return None
                else:
                    stval = wlist[i].count
            elif wlist[i].year == end:
                if wlist[i].count < 1000:
                    return None
                else:
                    endval = wlist[i].count
    if isinstance(endval, int) and  isinstance(stval, int):
        return endval/stval
    return None

def main():
    """
    asks for inputs for the file, st, and end yr, then calculates the trend values
    for all applicable words and prints the top ten and bottom ten trending words
    :return:
    """
    file = input("Enter the name of a file: ")
    startYr = int(input("Enter starting year: "))
    endYr = int(input("Enter ending year: "))
    trendlist = trending(readWordFile(file), startYr, endYr)
    print("The top 10 trending words from", startYr, "to", str(str(endYr) + ':'))
    if len(trendlist) >= 10:
        for x in range(10):
            print(trendlist[x].word)
    elif len(trendlist) < 10:
        for x in range(len(trendlist)):
            print(trendlist[x].word)
    print("\n" + "The bottom 10 trending words from", startYr, "to", str(str(endYr) + ':'))
    if len(trendlist) >= 10:
        for x in range(1, 11):
            print(trendlist[-x].word)
    elif len(trendlist) < 10:
        for x in range(1, len(trendlist)+1):
            print(trendlist[-x].word)

if __name__ == '__main__':
    main()