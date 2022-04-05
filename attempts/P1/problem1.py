#!/usr/bin/env python3

__author__ = "Aidan Kelley"
__copyright__ = "Copyright 2021"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "3.8.7"
__maintainer__ = ""
__email__ = "akelley1@highpoint.edu"
__status__ = "Complete"

import matplotlib.pyplot as plt
import re

def main():
    data = open("antenna.txt", "r").read().split()
    # print(data)
    antennaCount = data[0]
    data.pop(0)
    # print(data)

    circleX = []
    circleY = []

    for i in range(0, len(data)):
        if i%2 == 0:
            circleX.append(float(data[i]))
        else:
            circleY.append(float(data[i]))
    # print(circleX)
    # print(circleY)

    radius = 20
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.xlim([0, 600])
    plt.ylim([0, 600])
    plt.title('Circle')
    for i in range(0, len(antennaCount)):
        draw_circle = plt.Circle((circleX[i], circleY[i]), radius,fill=False)
        axes.add_artist(draw_circle)

    plt.show()

if __name__ == "__main__":
    main()
