import os
import csv

budgetdata = os.path.join('Desktop/PythonResources', 'budget_data.csv')

total = 0

with open(budgetdata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)
    csv_header = next(csvreader)

# print headers for analysis
    print(" ")
    print("Financial Analysis")
    print("------------------------------")

# total number of months included in the dataset
    print("Total Months: " + str(len(list(csvreader))))
# start over reading the rows
    csvfile.seek(0)
    next(csvreader)

# net total amount of Profit/Losses
    for row in csvreader:
        total += int(row[1])
    print("Total: $" + str(total))
# start over reading the rows
    csvfile.seek(0)
    next(csvreader)

# average of the changes in Profit/Losses over the entire period
    for row in csvreader:
        total += int(row[1])
        count = len(list(csvreader))
        avg = total/count
    print("Average Change: $" + str(round(avg,2)))