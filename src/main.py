from fileinput import filename
from hashlib import new
from tkinter.ttk import Separator
from player import*
from pathlib import Path
import csv

#initial setup
print("Welcome to the baseball stats app\nEnter year to continue")
playerList = []

def run():
    """Function which runs the program"""
    year = (int(input("What year: ")))

    sortedPlayerList = []
    for player in playerList:
        if player.returnYear() == year:
            sortedPlayerList.append(player)



#read the csv file
seperator = "\n"
filename = "BaseballStats.csv"
filepath = Path(__file__).resolve().parent/filename
with open(filepath) as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    
    for row in csvReader:

        lastName = row[0]
        firstName = row[1]
        year = row[3]
        baDiff = row[4]
        slgDiff = row[5]
        avgEv = row[6]

        player1 = Player(firstName, lastName, year, baDiff, slgDiff, avgEv)
        playerList.append(player1)

        


run()