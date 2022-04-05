# Team 15

#!/usr/bin/env python3

__author__ = "Aidan Kelley, Ryan Hirscher, Conor Rybacki"
__copyright__ = "Copyright 2021"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "3.8.7"
__maintainer__ = ""
__email__ = "akelley1@highpoint.edu, rhirsche@highpoint.edu, crybacki@highpoint.edu"
__status__ = "Complete"


def main():

    data = open("ballot.txt", "r")
    votes = data.read().splitlines()
    # print(votes)
    # print("")

    first = []
    second = []
    third = []

    for i in range(0, len(votes)):
        first.append(votes[i][0])
        second.append(votes[i][2])
        third.append(votes[i][4])
    voters = len(first)

    # print(first)
    # print(second)
    # print(third)

    firstVote = percentage(count(first), voters)
    # print(firstVote)

    # percentSecond = percentage(count(second), voters)
    # print(percentSecond)
    #
    # percentThird = percentage(count(third), voters)
    # print(percentThird)

    print("")

    secondVote = percentage(addCount(count(first), count(second)), voters*2)
    thirdVote = percentage( addCount(addCount(count(first), count(second)), count(third) ), voters*3)

    for d in firstVote:
        if firstVote[d] >.5:
            winner = d
            break
        else:
            if secondVote[d] >.5:
                winner = d
                break
            else:
                if thirdVote[d] >.5:
                    winner = d
                    break
                else:
                    winner = "tie"

    if winner == "tie":
        print("tie")
    else:
        print(winner, "wins")


def addCount(vote1, vote2):
    results = {}
    for d in vote1:
        results[d] = vote1[d] + vote2[d]
    return results

def count(data):
    results = {'A': 0,
                'B': 0,
                'C': 0,
                'D': 0,
                'E': 0,
                'F': 0,
                'G': 0,
                'H': 0,
                'I': 0,
                'J': 0
                }
    for vote in data:
        for key in results:
            if vote == key:
                results[key] = results[key] + 1
    return results

def percentage(data, voters):
    # print(data)
    for d in data:
        # print(d)
        # print(data[d])
        data[d] = float(format(data[d]/voters, '.4f'))
    return data

if __name__ == "__main__":
  main()
