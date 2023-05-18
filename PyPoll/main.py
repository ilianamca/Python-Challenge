#Mod 3 Challenge-PyPoll
# count how many votes were casted
# how many condidates were there
# show what % of votes for each candidates
# show number of votes for each candidates
# and then the winner-candidate with the most votes!



import csv
import os

#set file
file_path = os.path.join("Resources", "election_data.csv")

with open(file_path) as file:
    reader = csv.reader(file) 
    next(reader) #skipping header row

    #varliable
    totalvotes = 0
    candidates = {}
    winner = ""


    #counting votes
    #counting candidates
    for row in reader: #processing each row
        totalvotes = totalvotes + 1
        currentcan = row[2]

        if currentcan not in candidates: 
            candidates[currentcan] = 1
        else: candidates[currentcan] += 1
        # if/else statement = if we havent seen the candidate give them a vote, if we have seen them give them another vote

winner = max(candidates, key = candidates.get) 
#key tells max to look up by vote..max gives the name of candidate with the most votes


#printing "Election Results" in format

report= f'''
Election Results

------------------

Total Votes:{totalvotes}

--------------------

'''
#calc the % of votes for each candidate  and # of votes for each
for currentcan, votes in candidates.items():
    percentvotes = votes / totalvotes * 100
    report += f'{currentcan}: {percentvotes:.3f}% ({votes}) \n'
     
report += f'--------------------\nWinner: {winner}\n----------------------'
print(report)


#creating an output file
output_path = os.path.join("analysis","Election_Analysis.txt")
with open(output_path, "w") as outfile:
    outfile.write(report)