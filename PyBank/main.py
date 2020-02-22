import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:


    print("One moment please...")
    print(" ")

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first so that it's not counted with the following data in the for loops.
    csv_header = next(csvreader)


    # Create empty lists for Dates, Totals, Changes in revenue.
    # Also create variables for the dates of the greatest profit and the greatest loss
    Dates = []
    Totals = []
    Changes = []
    greatest_increase_date = ""
    greatest_decrease_date = ""



    # For loop to read each row of data after the header to populate the Dates list and Totals list
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

    # Create variables for the average change, the netTotal, and the total amount of months.
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
    print("Total: $" + str(netTotal))
    print("Average Change: $" + str(round(avg_Change,2)))
    print("Greatest increase in Proftis: " + str(greatest_increase_date) + " ($" + str(greatest_Profit) + ")" )
    print("Greatest decrease in Proftis: " + str(greatest_decrease_date) + " ($" + str(greatest_Loss) + ")")
    
