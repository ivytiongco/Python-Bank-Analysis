import os
import csv

budgetdata = os.path.join('Desktop/PythonResources', 'budget_data.csv')

with open(budgetdata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)
    csv_header = next(csvreader)
    date = []
    amount = []
    amount_change = []
    total = 0

    for row in csvreader:
        date.append(row[0])
        amount.append(int(row[1]))

# print headers for analysis
    print(" ")
    print("Financial Analysis")
    print("------------------------------")

# total number of months included in the dataset
#    print("Total Months: " + str(len(list(csvreader))))
    print("Total Months: " + str(len(date)))

# net total amount of Profit/Losses
    print("Total: $" + str(sum(amount)))

# find difference between rows
    for i in range(1, len(amount)):
        amount_change.append(amount[i] - amount[i-1])

# average of difference between rows
        avg_amount_change = sum(amount_change)/len(amount_change)

# maximum of amount change is greatest increase in profits
        max_amount_change = max(amount_change)

# greatest decrease in losses (date and amount)
        min_amount_change = min(amount_change)

#find dates
        max_amount_change_date = str(date[amount_change.index(max(amount_change))+ 1])
        min_amount_change_date = str(date[amount_change.index(min(amount_change))+ 1])

# print avg, greatest inc, greatest dec
    print("Average Change: $" + str(round(avg_amount_change,2)))        
    print("Greatest Increase in Profits: " + max_amount_change_date + " ($" + str(max_amount_change) + ")")
    print("Greatest Decrease in Losses: " + min_amount_change_date + " ($" + str(min_amount_change) + ")")

# create text file of results ?????