#add our dependencies.
import csv
import os
#assing a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
#assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. intialize a total vote counter.
total_votes = 0
#candidates option.
candidate_options = []
#Declare the empty dictionary.
candidate_votes = {}


list_of_counties = []
county_votes = {'Jefferson': 0, 'Denver': 0, 'Arapahoe':0 }
#create a dictionary County-key and votes-values

#largest_count
largest_county = () 
largest_county = 0
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print the header row.
    headers = next(file_reader)
    print(headers)
    #print each row in the CSV file.
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        county_name = row[1]
        
        if county_name not in list_of_counties:
            list_of_counties.append(county_name)
        if county_name == 'Jefferson':
            county_votes['Jefferson'] += 1
        if county_name == 'Denver':
            county_votes['Denver'] += 1
        if county_name == 'Arapahoe':
            county_votes['Arapahoe'] += 1   
    

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1
    
    print(county_votes)
    if county_votes['Jefferson'] > county_votes['Denver']:
        largest_vote_a = county_votes['Jefferson']
    else:
        largest_vote_a = county_votes['Denver']
    if largest_vote_a > county_votes['Arapahoe']:
        largest_vote = largest_vote_a
    else:
        largest_vote = county_votes['Arapahoe']
    Largest_County_Turnout = list(county_votes.keys())[list(county_votes.values()).index(largest_vote)]
    print(Largest_County_Turnout)
    print ("Largest County Turnout:",list(county_votes.keys())[list(county_votes.values()).index(largest_vote)])

with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    
   # Print the candidate vote dictionary..
    print(candidate_votes)
    

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        print(f"{candidate}: received {vote_percentage}% of the vote.") 
    
    

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in county_votes:
        # Retrieve vote count of a candidate.
        votes = county_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        county_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(county_results)
              
        #  Save the candidate results to our text file.
        
        txt_file.write(county_results)

        
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
              
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        #largest_county
        
    
    
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    Largest_County_Turnout_txt = (
        f"-------------------------\n"
        f"Largest County Turnout: {Largest_County_Turnout}\n"
        
        f"-------------------------\n")
    txt_file.write(Largest_County_Turnout_txt)
    txt_file.write(winning_candidate_summary)