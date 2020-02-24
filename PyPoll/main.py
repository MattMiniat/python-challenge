import os
import csv

# path to csv file
csvpath = os.path.join("Resources","election_data.csv")

def voterCount(list)
vote_count + 1
    print(str(vote_count))


with open(csvpath) as csvfile:

    print("One moment please...")
    print(" ")

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first so that it's not counted with the following data in the for loops.
    csv_header = next(csvreader)

    VoterID = []
    Counties = []
    Candidates = []
    
    for row in csvreader
        
    






# 
# 
# Create csvreader and for loop to read through the poll data
# Create list and loop and return all unique candidates who recieved votes (votes = true)
# Create for loop adding up all of the votes
    #Create separate loops to add up how many votes each candidate recieved
    #divide and format the answers
#Create a dictionary using candidates as keys and their votes as values, returning the max value as the winner
#  
#
#
#
#
#