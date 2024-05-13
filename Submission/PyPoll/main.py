#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

# Modules
import csv

# Set path for file
csvpath = "Resources/election_data.csv"

# Variables
vote_count = 0
candi_dict = {}
percentages = {}
winner_candi = ""
winner_votes = 0

with open(csvpath, encoding= 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # total number of votes
    for row in csvreader:
        vote_count += 1
        
        # list of canidates
        row_candi = row[2]
        if row_candi in candi_dict.keys():
            candi_dict[row_candi] += 1
        else:
            candi_dict[row_candi] = 1
        
print("Total number of votes cast: ", vote_count)
print("List of candidates: ", candi_dict)

# percentage of votes (asked Xpert)
for candidate in candi_dict.keys():
    votes = candi_dict[candidate]
    percentage = (votes / vote_count) * 100
    percentages[candidate] = percentage
    print("Percentage the candidate won: ", f"{candidate}: {percentage:.3f}% ({votes})")
    
for candidate, percentage in percentages.items():
    if percentage > winner_votes:
        winner_votes = percentage
        winner_candi = candidate
print(f"Winner: {winner_candi} with {winner_votes:.3f}% of the votes")




