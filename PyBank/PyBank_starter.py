import os
import csv

# Set the path for the CSV file
budget_data = os.path.join("Resources", "budget_data.csv")

# Create lists to store data
profits = []
monthly_changes = []
date = []

# Initialize variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = None

# Open the CSV using the set path
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:    
        # Count the number of months
        count += 1 

        # Append the date and profit information
        date.append(row[0])
        profit_value = int(row[1])
        profits.append(profit_value)

        # Calculate total profit
        total_profit += profit_value

        # Calculate monthly change in profits
        if initial_profit is not None:
            monthly_change_profits = profit_value - initial_profit
            monthly_changes.append(monthly_change_profits)
            total_change_profits += monthly_change_profits

        # Update initial profit for next iteration
        initial_profit = profit_value

# Calculate average change in profits
average_change_profits = total_change_profits / (count - 1) if count > 1 else 0

# Find the greatest increase and decrease in profits
if monthly_changes:
    greatest_increase_profits = max(monthly_changes)
    greatest_decrease_profits = min(monthly_changes)

    increase_date = date[monthly_changes.index(greatest_increase_profits) + 1]  # Offset by +1 due to indexing
    decrease_date = date[monthly_changes.index(greatest_decrease_profits) + 1]

# Print results
print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")
print("----------------------------------------------------------")

# Write results to a text file
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) + "\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")