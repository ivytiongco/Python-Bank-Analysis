# import the os module to allow us to create file paths across operating systems
import os

# module for reading CSV files
import csv

# set path for file
budgetdata = os.path.join('Desktop/PythonResources', 'budget_data.csv')

# open the CSV
with open(budgetdata) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # read the header row first
    csv_header = next(csvreader)
    
    # variables
    date = []
    amount = []
    amount_change = []

    # read each row of data after the header
    for row in csvreader:
        date.append(row[0])
        amount.append(int(row[1]))

# print first lines of results
    print("Financial Analysis")
    print("------------------------------")

# total number of months included in the dataset
    print(f"Total Months: {len(date)}")

# net total amount of Profit/Losses
    print(f"Total: ${sum(amount)}")

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
    print(f"Average Change: ${round(avg_amount_change,2)}")
    print(f"Greatest Increase in Profits: {max_amount_change_date} (${max_amount_change})")
    print(f"Greatest Decrease in Losses: {min_amount_change_date} (${min_amount_change})")

# set path for text file of results
output_path = os.path.join('Desktop/Python-Bank-Poll-Analyses/PyBank', "pybank.txt")

# create text file and print results to it
f = open(output_path, 'w')
print("Financial Analysis", file = f)
print("------------------------------", file = f)
print(f"Total Months: {len(date)}", file = f)
print(f"Total: ${sum(amount)}", file = f)
print(f"Average Change: ${round(avg_amount_change,2)}", file = f)
print(f"Greatest Increase in Profits: {max_amount_change_date} (${max_amount_change})", file = f)
print(f"Greatest Decrease in Losses: {min_amount_change_date} (${min_amount_change})", file = f)