from fileinput import filename
from hashlib import new
from tkinter.ttk import Separator
from player import Player
from pathlib import Path
import csv

playerList = []

print("Welcome to the baseball stats app\nEnter year to continue")

def run():
    year = input("What year: ")

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