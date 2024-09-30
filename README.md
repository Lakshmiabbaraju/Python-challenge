Explanation for PYBANK: 
Reading the CSV File: The script uses the csv module to read the budget_data.csv file and skips the header.
Calculating Metrics:
It calculates the total number of months and the net total of "Profit/Losses".
It keeps track of changes in profits/losses to calculate the average change.
It also tracks the greatest increase and decrease in profits.
Output: The results are formatted into a string and printed to the console. They are also written to a text file called financial_analysis.txt.

Explanation for PYPOLL: 
Reading the CSV File: The script uses the csv module to read the election_data.csv file and skips the header.
Calculating Metrics:
It counts the total number of votes and tallies the votes for each candidate using a defaultdict.
It calculates the percentage of votes for each candidate and identifies the winner based on the highest vote count.
Output: The results are formatted into a string and printed to the console. They are also saved to a text file called election_results.txt.
