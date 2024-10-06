import os
import csv

# Objective 2: Set the path for the CSV file in PyBankcsv
#PyBankcsv = os.path.join("Resources", "budget_data.csv")  # Update this path if necessary
PyBankcsv = r"C:\Users\adith\UTA-VIRT-DATA-PT-09-2024-U-LOLC\02-Homework\03-Python\Starter_Code\PyBank\Resources\budget_data.csv"

# Objective 3: Create the lists to store data. 
profit = []
monthly_changes = []
dates = []

# Initialize the variables as required.
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = None  # Set to None for first comparison

# Open the CSV using the set path PyBankcsv
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Conducting the analysis
    for row in csvreader:
        # Use count to count the number of months in this dataset
        count += 1

        # Append the date and profit information
        dates.append(row[0])
        current_profit = int(row[1])
        profit.append(current_profit)
        total_profit += current_profit

        # Calculate the monthly change in profits
        if initial_profit is not None:
            monthly_change_profits = current_profit - initial_profit
            monthly_changes.append(monthly_change_profits)
            total_change_profits += monthly_change_profits

        # Update initial_profit for next iteration
        initial_profit = current_profit

# Calculate the average change in profits
average_change_profits = total_change_profits / len(monthly_changes) if monthly_changes else 0

# Find the max and min change in profits and the corresponding dates
if monthly_changes:
    greatest_increase_profits = max(monthly_changes)
    greatest_decrease_profits = min(monthly_changes)
    
    increase_date = dates[monthly_changes.index(greatest_increase_profits) + 1]  # +1 to align with dates
    decrease_date = dates[monthly_changes.index(greatest_decrease_profits) + 1]  # +1 to align with dates
else:
    increase_date = ""
    decrease_date = ""

# Print results
print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: " + "$" + f"{average_change_profits:.2f}")
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")
print("----------------------------------------------------------")

# Write the results to a text file
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) + "\n")
    text.write("    Average Change: " + '$' + f"{average_change_profits:.2f}" + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
