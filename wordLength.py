"""
wordLength.py
Written by Conor Brown
"""

from wordData import *
from boxAndWhisker import *
from math import *

def summaryFromWords(words, year):
    """
    computes the distribution of word lengths and finds the five number summary of the lengths
    :param words: a dict of yearCount objects
    :param year: the given year to calculate at
    :return: the 5 num summary
    """
    numdict = dict()
    num = 0
    keys = words.keys()
    for key in keys:
        for x in range(len(words[key])):
            if words[key][x].year == year:
                if len(key) in numdict:
                    numdict[len(key)] += words[key][x].count
                elif not len(key) in numdict:
                    numdict[len(key)] = words[key][x].count
                break
            elif words[key][x].year > year:
                break
    numkeys = sorted(list(numdict.keys()))
    for j in range(100):
        if j in numdict:
            num += numdict[j]
    if len(numkeys) == 0:
        raise Exception("No words for this year.")
    min = numkeys[0]
    max = numkeys[-1]
    counter = 0
    var = 0
    for i in range(len(numkeys)):
        counter += numdict[numkeys[i]]
        if counter >= num/4 and var == 0:
            if counter == num/4:
                if i == 0:
                    q1 = numkeys[0]
                else:
                    q1 = (numkeys[i] + numkeys[i-1]) / 2
            else:
                q1 = numkeys[i]
                var = 1
        if counter >= num/2 and var == 1:
            if counter == num/2:
                if i == 0:
                    med = numkeys[0]
                else:
                    med = (numkeys[i] + numkeys[i-1]) / 2
            else:
                med = numkeys[i]
                var = 2
        if counter >= 3*num/4 and var == 2:
            if counter == num/2:
                if i == 0:
                    q3 = numkeys[0]
                else:
                    q3 = (numkeys[i] + numkeys[i-1]) / 2
            else:
                q3 = numkeys[i]
                break
    return min, q1, med, q3, max

def main():
    """
    asks for inputs of file, year, then draws the 5 number summary as a box and whisker plot
    :return: None
    """
    file = input("Enter a file name: ")
    yr = int(input("Enter a year: "))
    dct = readWordFile(file)
    lst = list(summaryFromWords(dct, yr))
    print("Minimum:", lst[0])
    print("1st quartile:", lst[1])
    print("Median:", lst[2])
    print("3rd quartile:", lst[3])
    print("Maximum:", lst[4])
    boxAndWhisker(lst[0], lst[1], lst[2], lst[3], lst[4])

if __name__ == '__main__':
     main()