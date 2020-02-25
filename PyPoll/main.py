import os
import csv

# path to csv file
csvpath = os.path.join("Resources","election_data.csv")

# lists to be called by functions
total_votes = []
assignedVotes = []
Candidates = []
electionDict = {}

# Main function used to organize and print results 
def Results():
    print("Election Results")
    print("----------------------------------------")
    getTotalVotes()
    print("----------------------------------------")
    getCandidates()
    print("----------------------------------------")
    # getWinner()

# Function used to populate the 'total_votes' list 
def getVotes(election_data):
    total_votes.append(election_data[2])

# After 'getVotes()' is used in the with loop, 
# This function counts the number of votes in the list and prints out the total number of votes
def getTotalVotes():
    total = len(total_votes)
    print("Total Votes: " + str(total))


# Unfortunately, I could not figure out how to split this next function into separate functions as they rely on each other,
# and for some reason would only return empty. 
# Each part of the function is as follows:
# 1) Filters out the names of each unique candidate in 'total_votes' and add them to the 'Candidates' list, 

# 2) Convert the list into a dictionary: electionDict

# 3) Iterates through 'total_votes', comparing the keys in electionDict to the items in total_votes
#       for each time an item equals the dictionary's key, the value of that key is incremented by 1

# 4) Prints out the keys of electionDict, calls votePercent() for each entry in electionDict, and prints out the value of each key.

# 5) uses max() to detemine the maximum value in electionDict and then prints the key as the winner to the terminal.

def getCandidates():
# 1)
    candidatesSet = set(total_votes)
    NewList = list(candidatesSet)
    Candidates = NewList

# 2)
    electionDict = {i : 0 for i in Candidates}

# 3)
    for key in electionDict:
        for j in range(len(total_votes)):
            if key == total_votes[j]:
                electionDict[key] += 1
# 4)
        print(f" " + key, electionDict[key], votePercent(electionDict[key], len(total_votes)))
    
# 5)
    print("----------------------------------------")
    Winner = max(electionDict, key=electionDict.get)
    print("Winner!: "+ Winner)
        

# function used to find the percent of the total_votes and print it out as a string.
def votePercent(votesAssigned, totalVotes):
    PercentOfVote = str(round((votesAssigned / totalVotes * 100)))
    output = str("(" + PercentOfVote + "%)")
    return output


with open(csvpath) as csvfile:

    print("One moment please...")
    print(" ")

    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first so that it's not counted with the following data in the for loop.
    csv_header = next(csvreader)
    

    #Loop through the data and find the total number of votes in the csv
    for row in csvreader:
        getVotes(row)
    #print out the results of the election and determine the winner.
    Results()






