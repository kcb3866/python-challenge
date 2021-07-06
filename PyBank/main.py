import csv
import os

pybank_csv = os.path.join("Resources", 'budget_data.csv')

months_change = []
net_change_list = []

tot_months = 0
tot_profits = 0
inc_chg = ["", 0]
dec_chg = ["", 9999999999999]

with open(pybank_csv, "r") as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    header = next(csv_reader) 

    # Extract the first row to avoid appending to net_change
    first_row = next(csv_reader)
    tot_months += 1
    tot_profits += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csv_reader:
       # track  the total 
       tot_months += 1
       tot_profits += int(row[1])
    
    #    track the net change
       net_change = int(row[1]) - prev_net
       prev_net = int(row[1])
       net_change_list += [net_change] 
       months_change += [row[0]]
    
    # Calculate the greatest increase
    if net_change > inc_chg[1]:
        inc_chg[0] = row[0]
        inc_chg[1] = net_change

    # Calculate the greatest decrease
    if net_change < dec_chg[1]:
        dec_chg[0] = row[0]
        dec_chg[1] = net_change
    # Calculate the average net change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate output Summary
output_summary = (
    f"Financial Analysis\n"
    f"--------------\n"
    f"Total Months: {tot_months}\n"
    f"Total Profits: {tot_profits}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {inc_chg[0]} (${inc_chg[1]})\n"
    f"Greatest Decrease in Profits: {dec_chg[0]} (${dec_chg[1]}\n"
)

print(output_summary)
       
        
 
    

output_file = os.path.join("budget_analysis.txt")

#  Open the output file
with open(output_file, "w") as txt_file:
    txt_file.write(output_summary)