#import necessary packages
import csv
import os
#Get the current working directory to understand the file path
#print (os.getcwd())
#Get the filepath to the csv file
file_open_path = os.path.join("Week 3","Asynchronous","py_poll","Resources","election_results.csv")
#initialise the counter
total_votes=0
#create a list to store candidate names
candidate_options=[]
#Create a list to store county names
county_options=[]
#create a dicotionary to store candidate votes
candidate_votes={}
#create a dictionary to store county turnout
county_turnout={}
#winning candidate an winning vote count tracker
winning_candidate=""
winning_vote_count=0
winning_vote_percentage=float(0)
#county turnout tracker
highest_county_name=""
highest_county_count=0
highest_county_percentage=float(0)
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
        county_name=row[1]
        #check for duplicates in county names
        if county_name not in county_options:
            county_options.append(county_name)
            #begin tabulating turnout
            county_turnout[county_name]=0
        #add a vote to the county turnout
        county_turnout[county_name]+=1
##sanity check print(county_turnout)
#getting ready for the text file
file_write_path = os.path.join("Week 3","Asynchronous","py_poll","Analysis","election_analysis.txt")
with open(file_write_path,"w") as outfile:
    county_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(county_results, end="")
    # Save the final vote count to the text file.
    outfile.write(county_results)
    for county_name in county_turnout:
        county_votes = county_turnout[county_name]
        county_vote_percentage=(county_votes/total_votes)*100
        #print all county names, vote count and vote percentage
        county_results=(f"{county_name}: {county_vote_percentage:.1f}% ({county_votes:,})\n")
        print(county_results)
        outfile.write(county_results)
        # print(f"{county_name}: {county_vote_percentage:.1f}% ({county_votes:,})" )
        #find the winning candidate and vote count by checking if winning votes is greater than zero
        if (county_votes>highest_county_count) and (county_vote_percentage>highest_county_percentage):
            highest_county_percentage=county_vote_percentage
            highest_county_count=county_votes
            highest_county_name=county_name
    winning_county_summary=(
            f"\n-----------------------------\n"
            f"Largest County Turnout: {highest_county_name}\n"
            # f"Winning vote count: {highest_county_count:,}\n"
            # f"Winning Percentage: {highest_county_percentage:.1f}%\n"
            f"-------------------------------\n"
        )
    print(winning_county_summary)
    outfile.write(winning_county_summary)
    # election_results = (
    #     f"Candidate Results\n"
    #     f"-------------------------\n")
    #     # f"Total Votes: {total_votes:,}\n"
    #     # f"-------------------------\n")
    # print(election_results, end="")
    # # Save the final vote count to the text file.
    # outfile.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage=(votes/total_votes)*100
        #print all candidate names, vote count and vote percentage
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        outfile.write(candidate_results)
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})" )
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
            f"-------------------------------\n"
        )
    print(winning_candidate_summary)
    outfile.write(winning_candidate_summary)

    # print (total_votes)
    # print(candidate_options)
    # print (candidate_votes)

    # 
        