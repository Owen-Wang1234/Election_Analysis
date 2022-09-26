# Election_Analysis

## Project Overview
The Colorado Board of Elections has requested an election audit of a recent local congressional election with the following:

1. Calculation of the total number of votes cast.
2. A complete list of the candidates who received votes.
3. Calculation of the total number of votes each candidate received.
4. Calculation of the percentage of votes each candidate won.
5. Declaration of the winner of the election based on the popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.12, Visual Studio Code 1.71.2

## Summary
A Python program was written to analyze the election results, writing the output into a text file while printing it out onto the terminal. 

![The program output printed onto the Windows Command Prompt terminal.](https://github.com/Owen-Wang1234/Election_Analysis/blob/main/analysis/Election_Results_Printed_in_Command_Line.png)

As shown in the screenshot above, the results were:
1. The recent election accumulated a total of 369,711 votes.
2. The candidates who received any votes were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
3. The results for each candidate were:
    - Charles Casper Stockam received 23.0% of the vote (85,213 votes)
    - Diana DeGette received 73.8% of the vote (272,892 votes)
    - Raymon Anthony Doane received 3.1% of the vote (11,606 votes)
4. The winner of the election was Diana DeGette with 73.8% of the vote (272,892 votes)

## Challenge Overview
The Colorado Board of Elections has requested additional information in the election audit to include the following:

1. A complete list of the counties in the precinct.
2. Calculation of the total number of votes counted in each county.
3. Calculation of the percentage of votes counted in each county.
4. Identification of the county with the greatest voter turnout.

## Challenge Summary
Additional lines of code were added to the program, yielding these points of information:
1. The counties in the precinct for this election were:
    - Jefferson County
    - Denver County
    - Arapahoe County
2. The results for each county were:
    - Jefferson County received 10.5% of the vote (38,855)
    - Denver County received 82.8% of the vote (306,055)
    - Arapahoe County received 6.7% of the vote (24,801)
3. The county with the largest voter turnout was Denver County with 82.8% of the vote (306,055)

## General Program Summary
The Python program for election auditing calculates the votes cast in each county, the percentage of the vote as a result, the votes cast for each candidate, and the percentage of the vote as a result. With these, the program returns the list of counties and candidates with those values as well as the county with the greatest voter turnout and the winning candidate. This is all for one elected position in one precinct. Opportunities for changing or expanding this program can be addressed by modifying the script in different ways depending on what is desired.

### The Input File
The program requires a comma-separated value (csv) file containing all the ballots collected in the election. The csv file used in this program only contained three columns: The Ballot ID, the County where the vote was cast, and the Candidate selected in the vote (in that order). Using a csv file that differs from this will necessitate some adjustment of code to pull the right values like (for example) if a different csv file has more columns inserted to include even more demographic data including the city and even the ID of the voting location within the city. A more ambitious csv file may be comprehensive enough to include almost all the candidates selected for all the different positions up for election (if the ballot chose to vote for someone for some position at all).

### The Program Structure
The part of the program that reads the csv to tally up the votes looks like this:
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
The blocks of code that count the votes for the candidate and the votes in the county are very similar to each other, reflecting the modularity of the program. In fact, the other part of the program that sets up the results to be written into the output text file and to be printed onto the terminal is just as modular. These blocks can be added or removed depending on how complex or how simple the election will be with the variable names changed to reflect what is to be tracked (candidate for a certain position, county, city, voting site, even whether a proposition is voted "yes" or "no").

One thing of note is the line tracking the total votes. If the program is to be modified to track elections for more than one position, then a series of conditional statements should be set up to account for any ballots that voted for one position but ignored another.