import os
import csv

# path to csv file
csvpath = os.path.join("Resources","budget_data.csv")

# with loop used when accessing csv
with open(csvpath) as csvfile:

    print("One moment please...")
    print(" ")

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first so that it's not counted with the following data in the for loops.
    csv_header = next(csvreader)

    # Create empty lists for 'Dates', 'Totals', and 'Changes' in revenue.
    # Also create variables for the dates of the greatest profit and the greatest loss
    Dates = []
    Totals = []
    Changes = []
    greatest_increase_date = ""
    greatest_decrease_date = ""

    # For loop to read each row of data in the csv after the header to populate the Dates list and Totals list
    for row in csvreader:
        Dates.append(row[0])
        monthly_amount = int(row[1])
        Totals.append(monthly_amount)

    #For loop to populate Changes list by using the items in the totals list
    for i in range(1, len(Totals)):
        revenue_change = Totals[i] - Totals[i - 1]
        Changes.append(revenue_change)

    # Create variables for the greatest profit and greatest loss by using the min and max functions
    greatest_Profit = max(Changes)
    greatest_Loss = min(Changes)

    # Create variables for the average change, the net Total, and the total amount of months.
    avg_Change = sum(Changes)/len(Changes)
    netTotal = sum(Totals)
    Total_Months = len(Dates)

    # for loop with conditionals to filter out and return the dates of 
    # the greatest increase and the greatest decrease
    for i in range(len(Totals)):
        if Totals[i] - Totals[i - 1] == greatest_Profit:
            greatest_increase_date = Dates[i]
        if Totals[i] - Totals[i - 1] == greatest_Loss:
            greatest_decrease_date = Dates[i]

    #Print out the results
    print("Financial Analysis")
    print("-----------------------------------------")
    print("Total Months: " + str(Total_Months))
    print("Net Total: $" + str(netTotal))
    print("Average Change in revenue: $" + str(round(avg_Change,2)))
    print("Greatest increase in revenue: " + str(greatest_increase_date) + " ($" + str(greatest_Profit) + ")" )
    print("Greatest decrease in revenue: " + str(greatest_decrease_date) + " ($" + str(greatest_Loss) + ")")
    

    # export and print out to newly created text file in PyBank folder
    f = open("file.txt", "w")
    print("Financial Analysis", file = f)
    print("-----------------------------------------", file = f)
    print("Total Months: " + str(Total_Months), file = f)
    print("Net Total: $" + str(netTotal), file = f)
    print("Average Change in revenue: $" + str(round(avg_Change,2)), file = f)
    print("Greatest increase in revenue: " + str(greatest_increase_date) + " ($" + str(greatest_Profit) + ")", file = f )
    print("Greatest decrease in revenue: " + str(greatest_decrease_date) + " ($" + str(greatest_Loss) + ")", file = f)














# def numberOfMonths(budget_data):
#     Dates = []
#     Total_Months = int
#     for row in csvreader:
#         Dates.append(row[0]))
#     Total_Months = len(Dates)
#     print(f"Total Months" + Total_Months)

# def getTotals(csvreader):
#     Totals = []
#     for row in csvreader:
#         monthly_amount = int(row[1])
#         Totals.append(monthly_amount)
#     return Totals

# def NetTotal(list):
#     netTotal = sum(Totals)
#     return netTotal

# def getChanges(list):
#     for i in range(1, len(list)):
#         revenue_change = list[i] - list[i - 1]
#         Changes.append(revenue_change)
#     return Changes
    
# def getAvgChanges(list):
#     avg_Change = sum(list)/len(list)
#     return avg_Change

# def getMaxChange(list):
#     greatest_Profit = max(list)
#     return greatest_Profit

# def getMinChange(list):
#     greatest_Loss = min(list)
#     return greatest_Loss

# def get_Greatest_Increase_Date(list1, list2, int):
#     for i in range(len(list1)):
#         if list1[i] - list1[i - 1] == int:
#             greatest_increase_date = list2[i]
#     return greatest_increase_date

# def get_Greatest_Decrease_Date(list1, list2, int):
#     for i in range(len(list1)):
#         if list1[i] - list1[i - 1] == int:
#             greatest_decrease_date = list2[i]
#     return greatest_decrease_date


# with open(budget_csv) as csvfile:
#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvreader)

#     Dates = getDates(csvreader)
#     Totals = getTotals(csvreader)
#     Changes = getChanges(Totals)

#     Greatest_Increase = getMaxChange(Changes)
#     Greatest_Decrease = getMinChange(Changes)
#     Increase_Date = get_Greatest_Increase_Date(Totals, Dates, Greatest_Increase)
#     Decrease_Date = get_Greatest_Decrease_Date(Totals, Dates, Greatest_Decrease)

#     print(Total_Months(Dates))
#     print(NetTotal(Totals))
#     print(getAvgChanges(Changes))
#     print(Increase_Date + Greatest_Increase)
#     print(Greatest_Decrease + Decrease_Date)