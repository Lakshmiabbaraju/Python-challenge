import os
import csv

# Set the path for the CSV file
PyPollcsv = r"C:\Users\adith\UTA-VIRT-DATA-PT-09-2024-U-LOLC\02-Homework\03-Python\Starter_Code\PyPoll\Resources\election_data.csv"


# Initialize variables
count = 0
candidatelist = []
vote_count = {}

# Open the CSV using the set path
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # Count the total number of votes and candidates
    for row in csvreader:
        count += 1
        candidate = row[2]
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1

# Calculate vote percentages and determine the winner
unique_candidate = list(vote_count.keys())
votes = list(vote_count.values())
vote_percent = [(votes[i] / count) * 100 for i in range(len(votes))]
winning_vote_count = max(votes)
winner = unique_candidate[votes.index(winning_vote_count)]

# Print results
print("-------------------------")
print(f"header: {csv_header}")
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes: " + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
    print(f"{unique_candidate[i]}: {vote_percent[i]:.3f}% ({votes[i]})")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Write results to a text file
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write(f"Header: {csv_header}\n")
    text.write("---------------------------------------\n")
    text.write("Total Votes: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(unique_candidate)):
        text.write(f"{unique_candidate[i]}: {vote_percent[i]:.3f}% ({votes[i]})\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("----------------------")