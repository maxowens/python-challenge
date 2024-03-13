import os
import csv
import sys

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Save header
    csv_header = next(csvreader)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    #skip header
    next(csvreader)
    
    candidates = []
    
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    #skip header
    next(csvreader)
    
    ccs = 0
    dd = 0
    rad = 0
    
#iterate through csv file adding a vote to the correct candidate when they are mentioned
    
    for row in csvreader:
        if row[2] == 'Charles Casper Stockham':
            ccs += 1
        elif row[2] == 'Diana DeGette':
            dd += 1
        elif row[2] == 'Raymon Anthony Doane':
            rad += 1
            
total_votes = ccs + dd + rad

#Calculate the percentage of votes received

ccs_pct = round((ccs / (total_votes)) * 100, 3)
dd_pct = round((dd / (total_votes)) * 100, 3)
rad_pct = round((rad / (total_votes)) * 100, 3)

#Return the candidate with the most votes as the winner

if max(ccs,dd,rad) == ccs:
    winner = 'Charles Casper Stockham'
elif max(ccs,dd,rad) == dd:
    winner = 'Diane DeGette'
elif max(ccs,dd,rad) == rad:
    winner = 'Raymon Anthony Doane'
            
print('Election Results')
print('----------------')

print(f'Total Votes: {total_votes}')
print('----------------')

print(f'Charles Casper Stockham: {ccs_pct}% ({ccs})')
print(f'Diana DeGette: {dd_pct}% ({dd})')
print(f'Raymon Anthony Doane: {rad_pct}% ({rad})')
print('----------------')

print(f'Winner: {winner}')


# Save output to a text file
with open("PyPoll.txt", "w") as f:
    # Redirect standard output to the file
    sys.stdout = f
    # Print the same message as before
    print('Election Results')
    print('----------------')

    print(f'Total Votes: {total_votes}')
    print('----------------')

    print(f'Charles Casper Stockham: {ccs_pct}% ({ccs})')
    print(f'Diana DeGette: {dd_pct}% ({dd})')
    print(f'Raymon Anthony Doane: {rad_pct}% ({rad})')
    print('----------------')

    print(f'Winner: {winner}')