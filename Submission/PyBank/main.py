# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# Modules
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"

# Variables
month_count = 0
total_profit = 0
# asked Xpert
last_month_profit = None
changes = []

greatest_increase = 0
greatest_increase_date = ""
previous_profit1 = None

greatest_decrease = 0
greatest_decrease_date = ""
previous_profit2 = None

with open(csvpath, encoding= 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        # count months
        month_count += 1

        # total profit
        total_profit += int(row[1])
        
        # changes in profit
        if (month_count == 1):
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - (last_month_profit)
            changes.append(change)
            # reset
            last_month_profit = int(row[1])
            
            # greatest increase in profit
            current_profit1 = int(row[1])

            if previous_profit1 is not None:
                profit_change1 = current_profit1 - previous_profit1

                if profit_change1 > greatest_increase:
                    greatest_increase = profit_change1
                    greatest_increase_date = row[0]

            previous_profit1 = current_profit1

            # greatest decrease in profit
            current_profit2 = int(row[1])

            if previous_profit2 is not None:
                profit_change2 = current_profit2 - previous_profit2

                if profit_change2 < greatest_decrease:
                    greatest_decrease = profit_change2
                    greatest_decrease_date = row[0]

            previous_profit2 = current_profit2
    avg_change = sum(changes) / (len(changes))

    print("Month Count", month_count)
    print("Total Profit:", total_profit)
    print("Number of Changes:", len(changes))
    print("Average of Changes:", avg_change)
    print(f"The greatest increase in profits was {greatest_increase} on {greatest_increase_date}.")
    print(f"The greatest decrease in profits was {greatest_decrease} on {greatest_decrease_date}.")