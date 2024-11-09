# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# File paths
filepath = "Resources/election_data.csv"
output_file = "analysis/election_data_EWimmer.txt"

# Variables
total_votes = 0
vote_dict = {}

# Read in csv after headers
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        # print row to tally total votes
        total_votes += 1

        # Track votes per candidate
        candidate = row[2]
        if candidate in vote_dict.keys():
            vote_dict[candidate] += 1 # Add 1 vote for existing candidate
        else: # Add new candidate to dict with 1 vote count
            vote_dict[candidate] = 1

# Generate the output summary
def w_to_file(vote_dict, total_votes, output_file):
    with open(output_file, 'w') as f:
        f.write(f"Election Results\n")
        f.write("\n")
        f.write("-------------------------\n")
        f.write("\n")
        f.write(f"Total Votes: {total_votes}\n")
        f.write("\n")
        f.write("-------------------------\n")
        f.write("\n")
        for name, number in vote_dict.items():
            percent = (number / total_votes) * 100
            f.write(f"{name}: {percent:.3f}% ({number})\n")
            f.write("\n")
        f.write("-------------------------\n")
        f.write("\n")
        # Find winner and write
        winner = max(vote_dict, key=vote_dict.get)
        winner_votes = vote_dict[winner]
        f.write(f"Winner: {winner}\n")
        f.write("\n")
        f.write("-------------------------\n")
print(f"Write results to {output_file}")

# Write summary to output file
w_to_file(vote_dict, total_votes, output_file)



