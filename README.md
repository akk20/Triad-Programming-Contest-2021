# Triad Programming Contest 2021

## Problem 1 - Locating an Antenna
Imagine you need to erect an antenna to communicate with a number of fixed wireless stations.  You want to position the antenna to get the best possible reception given the location of the wireless stations.  The strength of the radio signal decreases proportionally to the cube of the distance of the transmission.  Therefore, you want to position the antenna so that the sum of the cubes of the straight line distance from the antenna to each wireless station is a minimum.  The location should be determined to within 0.1 meters.

Write a program that reads in a list of X Y station locations and then displays the optimal X,Y location of the antenna such that the sum of the cubes of the straight line distance to each station is a minimum.  Input must be read from the file antenna.txt

The first line of input will contain an integer (referred to as N) that indicates the number of stations.

The following N lines will each contain two positive floating point numbers giving the X Y coordinates of a wireless station in meters.  There will be no more than 25 stations. 

The output must be `Optimal antenna location is xxx.x yyy.y` where xxx.x and yyy.y is the optimal location.  The numbers can be displayed with any number of digits to the right of the decimal point.

Example input
```
5
100 100
500 150
300 190.5
300 250
150 450
```

Output for the Example Input:
`Optimal antenna location is 264.1 235.3`
