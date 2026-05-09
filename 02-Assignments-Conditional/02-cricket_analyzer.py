# 2. Task: Cricket Stats Analyzer 
# Objective: Write a script to analyze cricket stats for a team. 
# Hints: 
# Prompt the user to input the runs scored by each of the five players in a 
# cricket match. 
# For each player (Player 1 to Player 5) ask the user to input the runs they 
# scored. 
# Calculate the total runs scored by all players and the average runs. 
# Display the total runs and average runs to the user. 

player1 = int(input("Enter Player1 Runs they Scored : "))
player2 = int(input("Enter Player2 Runs they Scored : "))
player3 = int(input("Enter Player3 Runs they Scored : "))
player4 = int(input("Enter Player4 Runs they Scored : "))
player5 = int(input("Enter Player5 Runs they Scored : "))
print("="*40) #Used for alignment

total_runs = player1 + player2 + player3 + player4 + player5
print(f"Total Runs Scored by all Players: {total_runs}")
print() #Used for making space Ups and Below

# Average= total all numbers / Total subjects (formula)
average = total_runs / 5
print(f"Average Runs of the User: {average}")