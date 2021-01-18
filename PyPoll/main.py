import os
import csv

pypoll_csv = os.path.join("", 'Resources', 'election_data.csv')

candidates_dict={}

print("Election Results")
print("--------------")

with open(pypoll_csv, 'r') as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
            

    for row in csvfile:
        na=row[2]
        if na in candidates_dict:
            candidates_dict[na] = candidates_dict[na] + 1
        else:
            candidates_dict[na] = 1
    print(f'Candidates: {candidates_dict}')
    print('----------------------')

    max_vote = 0
    tot_vote = 0
    winner = ""
    for k,v in candidates_dict.items():
      max_vote = v
      tot_vote += max_vote
      winner = k

    print(f'Total Vote: {tot_vote}')
    print("-----------------")
    print(f'Winner: {winner}')





    
    
    
# I accidentally overrode this file with an incomplete file last minute.
# I did have the correct print out before

output_file = os.path.join("analysis.txt")

# #  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
 
#     # Write the header row
    writer.writerows("Election Results")
    writer.writerows("------------")
    writer.writerows(f'Total Vote: {tot_vote}')
    writer.writerows("------------")
    writer.writerows(f'Winner: {winner}')