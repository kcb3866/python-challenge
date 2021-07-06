import os
import csv

pypoll_csv = os.path.join("", 'Resources', 'election_data.csv')

max_vote = 0
tot_vote = 0
winner = ""

candidates_votes={}

candidate_opt = []

# print("Election Results")
# print("--------------")

with open(pypoll_csv, 'r') as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
            

    for row in csv_reader:

        tot_vote = tot_vote + 1

        name=row[2]
        if name in candidate_opt:
            
            candidates_votes[name] = candidates_votes[name] + 1
        else:
            candidate_opt.append(name)
            candidates_votes[name] = 0

    # print(f'Candidates: {candidates_dict}')
    # print('----------------------')

    
    # for k,v in candidates_dict.items():
    #   max_vote = v
    #   tot_vote += max_vote
    #   winner = k

    # print(f'Total Vote: {tot_vote}')
    # print("-----------------")
    # print(f'Winner: {winner}')






output_file = os.path.join("election_analysis.txt")

# #  Open the output file
with open(output_file, "w") as txt_file:

    election_results = (
        f"\n\nElection Results:\n"
        f"----------------------\n"
        f"Total Votes: {tot_vote}\n"
        f"-----------------------\n"
    )

    print(election_results, end="")

    txt_file.write(election_results)
    
    # determing the vote count and percentage   
    for candidate in candidates_votes:
        votes = candidates_votes.get(candidate)
        vote_pct = float(votes) / float(tot_vote) * 100

        # determine winning vote count and candidate
        if (votes > max_vote):
            max_vote = votes
            winner = candidate

        # Print each candidate's voter count and percentage
        voter_output = f"{candidate}: {vote_pct: .3f}% ({votes})\n"
        print(voter_output)

        txt_file.write(voter_output)
    
    candidate_summary = (
        f"--------------------\n"
        f"Winner: {winner}\n"
        f"---------------------\n"
    )

    txt_file.write(candidate_summary)