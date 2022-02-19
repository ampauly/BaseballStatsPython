from fileinput import filename
from hashlib import new
import string
from tkinter.ttk import Separator
from player import*
from pathlib import Path
import csv

#initial setup
print("Welcome to the baseball stats app\nEnter year to continue")
playerList = []
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

def run():
    """Function which runs the program"""
    year = (int(input("What year: ")))
    print("Enter 1 for batting average above expected")
    print("Enter 2 for slugging above expected")
    print("Enter 3 for average exit velocity")
    stat = (int(input("Which stat: ")))

    #filter players based on year
    filteredPlayerList = []
    for player1 in playerList:
        playerYear = player1.return_year()
        if int(playerYear) == int(year):
            filteredPlayerList.append(player1)

    #sort list based on stat
    def playerBaDiff_sort(emp):
        return emp.baDiff
    
    def playerSlgDiff_sort(emp):
        return emp.slgDiff

    def playerAvgEv_sort(emp):
        return emp.avgEv

    sortedPlayerList = []
    if int(stat) == 1:
        sortedPlayerList = sorted(filteredPlayerList, key=playerBaDiff_sort, reverse=True)
    elif int(stat) == 2:
        sortedPlayerList = sorted(filteredPlayerList, key=playerSlgDiff_sort, reverse=True)
    elif int(stat) == 3:
        sortedPlayerList = sorted(filteredPlayerList, key=playerAvgEv_sort, reverse=True)
    else:
        print("Enter valid number")
    
    print("The top 3 in " + str(year) + ":")
    for x in range(3):
        s = sortedPlayerList[x].return_firstName() + " " +sortedPlayerList[x].return_lastName()
        print(s)

    if input("Run again?(yes/no): ") == "yes":
        run()
    

run()