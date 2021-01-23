import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

with open(election_data) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file) 
    for row in csv_reader: 
        voterID = int(row[0])
        county = row[1]
        candidate = row[2]

        #count all votes
        total_votes = total_votes + 1
        
        if candidates.get(candidate):
            candidates[candidate] = candidates[candidate] + 1
        else: 
            candidates[candidate] = 1
    
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates: 
    votes = candidates[candidate]
    print(f"{candidate}: {(votes / total_votes) * 100}% ({votes})")
    if votes > winner_votes:
        winner = candidate 
        winner_votes = votes 

print("-------------------------")
print(f"Winner: {winner}")

