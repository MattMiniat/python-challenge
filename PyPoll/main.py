import os
import csv

# path to csv file
csvpath = os.path.join("Resources","election_data.csv")

total_votes = []
assignedVotes = []
Candidates = []
electionDict = {}

def Results():
    print("Election Results")
    print("----------------------------------------")
    getTotalVotes()
    print("----------------------------------------")
    getCandidates()
    print("----------------------------------------")
    # getWinner()


def getVotes(election_data):
    total_votes.append(election_data[2])


def getTotalVotes():
    total = len(total_votes)
    print("Total Votes: " + str(total))



def getCandidates():
    
    candidatesSet = set(total_votes)
    NewList = list(candidatesSet)
    Candidates = NewList
    electionDict = {i : 0 for i in Candidates}
    for key in electionDict:
        for j in range(len(total_votes)):
            if key == total_votes[j]:
                electionDict[key] += 1
        print(f" " + key, electionDict[key], votePercent(electionDict[key], len(total_votes)))
    

    print("----------------------------------------")
    Winner = max(electionDict, key=electionDict.get)
    print("Winner!: "+ Winner)
        


def votePercent(votesAssigned, totalVotes):
    PercentOfVote = str(round((votesAssigned / totalVotes * 100)))
    output = str("(" + PercentOfVote + "%)")
    return output


with open(csvpath) as csvfile:

    print("One moment please...")
    print(" ")

    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first so that it's not counted with the following data in the for loops.
    csv_header = next(csvreader)
    


    for row in csvreader:
        getVotes(row)
    Results()






