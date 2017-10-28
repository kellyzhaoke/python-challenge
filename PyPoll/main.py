# import os and csv
import csv

#input file 
file_to_load = "election_data_2.csv"
file_to_output = "election_data_2.txt"

Candidates=[]

with open(file_to_load, newline="") as election_data:
    csv_reader = csv.reader(election_data, delimiter=",")

    # Skip csv header
    next(csv_reader, None)

    # Loop 
    for row in csv_reader:
        Candidates.append(row[2]) # Update candidate list


#print total
total_votes=len(Candidates)
c_list=set(Candidates)
c_list=[i for i in c_list]
vote_counts=[Candidates.count(i) for i in c_list]
vote_percent= [((Candidates.count(i)/total_votes)*100) for i in c_list]
vote_percent= [round(i,3) for i in vote_percent]

max_vote=max(vote_counts)

mx,idx = max( (vote_counts[i],i) for i in range(len(vote_counts)) )

wins=c_list[idx]
        
# printing summary  
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes) )
print('-------------------------')

c_num=0
for i in c_list:
    print(i + ': ' + str(vote_percent[c_num])+'% '+ '(' + str(vote_counts[c_num]) + ')' )
    c_num+=1

print('-------------------------')

print('Winner: ' + str(wins)) 

print('-------------------------')
