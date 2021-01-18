import csv
import os

pybank_csv = os.path.join("", "", 'budget_data.csv')
pl_dict=[]
months=[]
pl_chg = []

print("Financial Analysis")
print("--------------")

tot_months = 0
tot_profits = 0
inc_chg = 0
dec_chg = 0

with open(pybank_csv, 'r') as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    header = next(csv_reader) 

    for row in csvfile:
       tot_months += 1
       tot_profits = tot_profits + int(row[1])
       months.append(row[0])
       pl_dict.append(row[1])
    
    for x in range(len(pl_dict)):
        change = int(pl_dict[x]) - int(pl_dict[x - 1])
        pl_chg.append(change) 
        inc_chg = max(pl_chg)
        dec_chg = min(pl_chg)
    
    def average(datachange):
        sum_pl = 0
        length = len(datachange)
        print(length)
        for x in datachange:
            sum_pl = sum_pl + x
        print(sum_pl)
        return sum_pl / length


       
        
    print(f'Total Months: {months}') 

    print(f'Total Profits: {tot_profits}')    
    print(f'Average Change: {average(pl_chg)} ')    
    print(f'Greatest Increase in Profits: ')  
    print(f'Greatest Decrease in Profits: ')  




    
    
    

# output_file = os.path.join("Analysis")

# #  Open the output file
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     writer.writerow(["Election Results"])

#     # Write in zipped rows
#     writer.writerows()
