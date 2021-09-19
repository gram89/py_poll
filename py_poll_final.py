#import necessary packages
import csv
import os
#Get the current working directory to understand the file path
print (os.getcwd())
#Get the filepath to the csv file
file_open_path = os.path.join("Week 3","Asynchronous","py_poll","Resources","election_results.csv")
#initialise the counter
total_votes=0
#create a list to store candidate names
candidate_options=[]
#create a dicotionary to store candidate votes
candidate_votes={}
#winning candidate an winning vote count tracker
winning_candidate=""
winning_vote_count=0
winning_vote_percentage=float(0)
#open the csv file
with open(file_open_path) as election_data:
    # print(election_data)
    #to do: read and analyse the data here
    file_reader=csv.reader(election_data)
    #get the header row
    headers=next(file_reader)
    # print(headers)
    #get the data rows
    for row in file_reader:
        total_votes+=1
        candidate_name=row[2]
        #check in candidate name is present in the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin counting votes
            candidate_votes[candidate_name]=0
        #add a vote to the candidate's count
        candidate_votes[candidate_name]+=1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage=(votes/total_votes)*100
    #print all candidate names, vote count and vote percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})" )
    #find the winning candidate and vote count by checking if winning votes is greater than zero
    if (votes>winning_vote_count) and (vote_percentage>winning_vote_percentage):
        winning_vote_percentage=vote_percentage
        winning_vote_count=votes
        winning_candidate=candidate_name
winning_candidate_summary=(
        f"-----------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning vote count: {winning_vote_count:,}\n"
        f"Winning Percentage: {winning_vote_percentage:.1f}%\n"
        f"-------------------------------"
    )
print(winning_candidate_summary)
# print (total_votes)
# print(candidate_options)
# print (candidate_votes)

# file_write_path = os.path.join("Week 3","Asynchronous","py_poll","Analysis","election_analysis.txt")
# outfile = open(file_write_path, "w")
# outfile.write("Hello World")
# with open(file_write_path,"w") as outfile:
#         outfile.write("Counties in the election\n---------------------------------\nArapahoe\nDenver\nJefferson")
    