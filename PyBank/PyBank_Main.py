import os
import csv
import sys

csvpath = os.path.join("Resources", "budget_data.csv")


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    csv_header = next(csvreader)



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    row_count = 0

    for row in csvreader:
        row_count += 1
    

total_months = row_count - 1


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    next(csvreader)
    
    pybank_total = 0
    

    #Iterate through csv and add each month's profit/loss to the total
    
    for row in csvreader:
        profit_loss = int(row[1])
        
        pybank_total += profit_loss



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    

    next(csvreader)
    
    prev_p_l = None
    total_change = 0
    num_changes = 0
    
    list_changes = []
    

    #Iterate through csv and find the months with greatest increase and decrease
    for row in csvreader:
        current_p_l = int(row[1])
        
        if prev_p_l is not None:
            change = current_p_l - prev_p_l
            total_change += change
            num_changes += 1
            list_changes.append(change)
            
        prev_p_l = current_p_l
    
    average_change = total_change / num_changes

    greatest_increase = max(list_changes)
    greatest_decrease = min(list_changes)



print("Financial Analysis")

print("----------------")

print(f'Total Months: {total_months}')
print(f'Total: ${pybank_total}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: (${greatest_increase})')
print(f'Greatest Decrease in Profits: (${greatest_decrease})')

# Save output to a text file
with open("PyBank.txt", "w") as f:
    # Redirect standard output to the file
    sys.stdout = f
    # Print the same message as before
    print("Financial Analysis")

    print("----------------")

    print(f'Total Months: {total_months}')
    print(f'Total: ${pybank_total}')
    print(f'Average Change: ${round(average_change,2)}')
    print(f'Greatest Increase in Profits: (${greatest_increase})')
    print(f'Greatest Decrease in Profits: (${greatest_decrease})')

