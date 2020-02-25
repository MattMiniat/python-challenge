import os
import csv

# path to csv file
csvpath = os.path.join("Resources","budget_data.csv")

Dates = []
Totals = []
Changes = []

# main function used to print out the results
def Financial_Analysis():
    print(" ")
    print("Financial Analysis")
    print("-----------------------------------------")
    Total_Months()
    getChanges()
    netTotal()
    Avg_Change()
    get_I_date()
    get_D_date()

# functions that calls other functions to populate lists
def FinancialLists(budget_data):
    getDates(budget_data)
    getTotals(budget_data)

#function used to populate 'Dates' list
def getDates(budget_data):
    date = str(budget_data[0])
    Dates.append(date)

#function used to populate 'Totals' list
def getTotals(budget_data):
    monthly_amount = int(budget_data[1])
    Totals.append(monthly_amount)

#function used to populate 'Changes' list
def getChanges():
    for i in range(1, len(Totals)):
        revenue_change = Totals[i] - Totals[i - 1]
        Changes.append(revenue_change)

#function used to print out the total amounnt of months by counting the number of items in 'Dates'
def Total_Months():
    Months_Num = (len(Dates))
    print(f"Total Months :" + str(Months_Num))

#function used to print out the net total of the csv
def netTotal():
    netTotal = sum(Totals)
    print(f"Net Total: $" + str(netTotal))

#function used to find the avergage change in the 'Changes' list
def Avg_Change():
    avg_change = sum(Changes)/len(Changes)
    print(f"Average Change: $" + str(round(avg_change, 2)))

#function used to find the max in Changes
def greatestIncrease():
    greatest_Profit = max(Changes)
    return greatest_Profit

#function used to find the min in Changes
def greatestDecrease():
    greatest_Loss = min(Changes)
    return greatest_Loss

#function used to find the date of the max in Changes and print it.
def get_I_date():
    for i in range(len(Totals)):
        if Totals[i] - Totals[i - 1] == greatestIncrease():
            greatest_increase_date = Dates[i]
    print(f"Greatest increase in revenue: " + greatest_increase_date + " ($" + str(greatestIncrease()) + ")" )

#function used to find the date of the min in Changes and print it
def get_D_date():
    for i in range(len(Totals)):
        if Totals[i] - Totals[i - 1] == greatestDecrease():
            greatest_decrease_date = Dates[i]
    print(f"Greatest decrease in revenue: " + greatest_decrease_date + " ($" + str(greatestDecrease()) + ")" )



# Read in the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first so that it's not counted with the following data in the for loop.
    csv_header = next(csvreader)
    
    # Loop through the data and populate the lists first
    for row in csvreader:
        FinancialLists(row)
    #print the results of the analysis
    Financial_Analysis()
