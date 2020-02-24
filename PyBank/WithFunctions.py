import os
import csv

# path to csv file
csvpath = os.path.join("Resources","budget_data.csv")

Dates = []
Totals = []
Changes = []

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


def FinancialLists(budget_data):
    getDates(budget_data)
    getTotals(budget_data)


def getDates(budget_data):
    date = str(budget_data[0])
    Dates.append(date)


def getTotals(budget_data):
    monthly_amount = int(budget_data[1])
    Totals.append(monthly_amount)


def getChanges():
    for i in range(1, len(Totals)):
        revenue_change = Totals[i] - Totals[i - 1]
        Changes.append(revenue_change)


def Total_Months():
    Months_Num = (len(Dates))
    print(f"Total Months :" + str(Months_Num))


def netTotal():
    netTotal = sum(Totals)
    print(f"Net Total: $" + str(netTotal))


def Avg_Change():
    avg_change = sum(Changes)/len(Changes)
    print(f"Average Change: $" + str(round(avg_change, 2)))


def greatestIncrease():
    greatest_Profit = max(Changes)
    return greatest_Profit


def greatestDecrease():
    greatest_Loss = min(Changes)
    return greatest_Loss


def get_I_date():
    for i in range(len(Totals)):
        if Totals[i] - Totals[i - 1] == greatestIncrease():
            greatest_increase_date = Dates[i]
    print(f"Greatest increase in revenue: " + greatest_increase_date + " ($" + str(greatestIncrease()) + ")" )


def get_D_date():
    for i in range(len(Totals)):
        if Totals[i] - Totals[i - 1] == greatestDecrease():
            greatest_decrease_date = Dates[i]
    print(f"Greatest decrease in revenue: " + greatest_decrease_date + " ($" + str(greatestDecrease()) + ")" )




with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first so that it's not counted with the following data in the for loops.
    csv_header = next(csvreader)
    
    for row in csvreader:
        FinancialLists(row)
    Financial_Analysis()
