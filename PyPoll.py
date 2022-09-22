# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a vairable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize a list of candidates.
candidate_options = []

# Initialize a dictionary pairing the candidate with votes.
candidate_votes = {}

# Initialize the winner's parameters.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Then add it to the list of candidates.
            candidate_options.append(candidate_name)

            # And start tracking the vote count for that candidate.
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1

# Calculate the percentage of votes each candidate won.
# Iterate through the candidate list.
for candidate_name in candidate_votes:

    # Get the vote count of the candidate.
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print the candidate name and the percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine the winner of the election based on popular vote.
    # See if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If true, then set the winning candidate, count, and percentage.
        winning_candidate = candidate_name
        winning_count = votes
        winning_percentage = vote_percentage

# Print the winning summary.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Use the open statement to open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
#    txt_file.write("Counties in the Election\n")
#    txt_file.write("-------------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")