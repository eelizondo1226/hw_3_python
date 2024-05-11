#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

#Importing data
import csv
csvpath = "Resources/budget_data.csv"

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the comic book
    for row in csvreader:
        if row[0] == comic:
            print(row[0] + " was published by " + row[8] + " in " + row[9])

            # Set variable to confirm we have found the comic book
            found = True

    # If the comic book is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")


