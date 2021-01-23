import os 
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
print(budget_data)

months = 0
net_profit_loss = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

with open(budget_data) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    for row in csv_reader: 
        month = row[0]
        profit_loss = int(row[1])
        months = months + 1  
        net_profit_loss = net_profit_loss + profit_loss

        if (profit_loss > greatest_increase): 
            greatest_increase = profit_loss
            greatest_increase_month = month 

        if (profit_loss < greatest_decrease): 
            greatest_decrease = profit_loss
            greatest_decrease_month = month 
    
def resultsString(): 
    results = ""
    results = results + "Financial Analysis\n"
    results = results + "-------------------------\n"
    results = results + f"Total Months: {months}\n"
    results = results + f"Total: {net_profit_loss}\n"
    results = results + f"Average Change: {net_profit_loss/months}\n"
    results = results + f"Greatest Increase in Profit: {greatest_increase_month} ${greatest_increase}\n"
    results = results + f"Greatest Decrease in Profit: {greatest_decrease_month} ${greatest_decrease}\n"
    return results 

results = resultsString()
print(results)
with open(os.path.join("analysis", "analysis.txt"),"w") as analysis_file:
    analysis_file.write(results)