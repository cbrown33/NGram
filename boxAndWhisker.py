"""
boxAndWhisker.py
Written by Conor Brown
"""

import turtle as t
from math import  *


def boxAndWhisker(small, q1, med, q3, large):
    """
    Draws a box and whisker plot from the given 5 number summary after normalizing the data
    :param small: the min of the data
    :param q1: the first quartile of the data
    :param med: the median of the data
    :param q3: the third quartile of the data
    :param large: the max of the data
    :return: None
    """
    lst = normalize(small, q1, med, q3, large)
    t.setup(width = ceil((lst[4]-lst[0])*2), height = 200)
    leftd = (lst[4]-lst[0])/2
    d1 = lst[1]-lst[0]
    d2 = lst[2]-lst[1]
    d3 = lst[3]-lst[2]
    d4 = lst[4]-lst[3]
    t.ht()
    t.seth(180)
    t.up()
    t.fd(leftd)
    t.down()
    drawEnd()
    t.fd(d1)
    drawBox(d2)
    drawBox(d3)
    t.fd(d4)
    drawEnd()
    t.done()

def drawEnd():
    """
    Draws an end for the min and max
    Start: facing towards the end
    End: facing away from the end
    :return: None
    """
    t.rt(90)
    t.fd(10)
    t.bk(20)
    t.fd(10)
    t.rt(90)

def drawBox(length):
    """
    Draws a box for the q1-med or med-q3 distance
    :param length: the length from q1-med or med-q3
    :return:
    """
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(50)
    t.up()
    t.lt(90)
    t.fd(length)
    t.down()

def normalize(q0, q1, q2, q3, q4):
    """
    Normalizes the data by halfing data that is all over 1000 and doubling data that is all under 400
    :param q0: the 0th distance
    :param q1: the first distance
    :param q2: the second distance
    :param q3: the third distance
    :param q4: the fourth distance
    :return: the five distances in a list
    """
    lst = [q0, q1, q2, q3, q4]
    while all(i >= 1000 for i in lst):
        lst[:] = [x / 2 for x in lst]
    while all(i <= 400 for i in lst):
        lst[:] = [x * 2 for x in lst]
    return lst

def main():
    """
    Draws a box and whisker plot from the 5 given inputs
    :return: None
    """
    boxAndWhisker(float(input("Enter the minimum: ")),
                  float(input("Enter the first quartile: ")),
                  float(input("Enter the median: ")),
                  float(input('Enter the third quartile: ')),
                  float(input("Enter the maximum: ")))

if __name__ == '__main__':
    main()