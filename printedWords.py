"""
printedWords.py
Written by Conor Brown
"""

from wordData import *
import simplePlot as s

def printedWords(words):
    """
    Takes a dict of words and totals the amount of words printed for each year as a list of YearCount objects
    :param words: the dict of words
    :return: The list of YearCount objects
    """
    lst = list()
    for i in range(1900, 2009):
        ct = 0
        for node in words:
            for item in words[node]:
                if i == item.year:
                    ct += item.count
        lst.append(YearCount(i, ct))
    return lst

def wordsForYear(year, yearList):
    """
    Takes a yearList from printedWords and a year and returns the amount of words printed in that year
    :param year: the inputted year
    :param yearList: from printedWords
    :return: 0 if the year does not exist, else the num of words printed
    """
    for node in yearList:
        if node.year == year:
            return node.count
        elif node.year > year:
            return 0
    return 0

def main():
    """
    Takes inputs for the previous two functions then calls them and displays a chart of the printed words
    :return: None
    """
    year = input("Enter a year: ")
    yearc = str(year + ':')
    wordsByYearList = printedWords(readWordFile(input('Enter the name of a file: ')))
    print("The amount of words printed in", yearc, wordsForYear(int(year), wordsByYearList))
    labels = 'Year', 'Total Words'
    plot = s.plot2D('Number of Printed Words over Time', labels)
    for yc in wordsByYearList:
        point = yc.year, yc.count
        plot.addPoint(point)
    plot.display()

if __name__ == '__main__':
    main()