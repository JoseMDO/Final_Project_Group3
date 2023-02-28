# Final Project Wandering in the Woods Game
# File Name: final_project_Group3_final_version.py
# Jose Montes De Oca Morfin, Paige Dyer
# PaigeDyer@lewisu.edu
# joseamontesdeocamo@lewisu.edu
# CPSC-44000-LT1
# Finished and Submitted: TBA

import random

def print_intro():
    print("Hello! Welcome to the wandering in the woods game. This game is designed for three sets of students.")
    print("The first is for students between the grades Kindergarden through Second grade. The second set is for")
    print("students between Third grade and Fifth grade, and the last set of students is for Sixth grade through")
    print("Eight grade. Each level of this game gets progressivley more complex the higher in grade level you go.")

def grade_choice():
    print("A. Kindegarden - 2nd ")
    print("B. 3rd - 5th ")
    print("C. 6th - 8th")
    grade_choice = input("Enter the letter of choice for your grade level: ")
    grade_choice = grade_choice.lower()
    while grade_choice not in ["a", "b", "c"]:
        print("You must select a letter option of the three provided. Please try again.")
        grade_choice = input("Enter the letter of choice for your grade level: ")
    return grade_choice.lower()

def run_experiment(grid_width, grid_height, num_people, people_positions):
    # Set up the grid
    grid = [[0 for j in range(grid_width)] for i in range(grid_height)]
    # Set up the counters for each person
    moves_counters = [0 for i in range(num_people)]
    # Loop until all people meet
    while len(set(people_positions)) > 1:
        for i in range(num_people):
            # Move each person
            x, y = people_positions[i]
            x += random.choice([-1, 0, 1])
            y += random.choice([-1, 0, 1])
            x = max(0, min(x, grid_width-1))
            y = max(0, min(y, grid_height-1))
            people_positions[i] = (x, y)
            moves_counters[i] += 1  
    # Return the moves_counters list
    return moves_counters

# Function to run multiple experiments
def run_experiments(num_experiments, grid_width, grid_height, num_people):
    # Initialize a list to hold the results of each experiment
    results = []
    # Loop through each experiment
    for i in range(num_experiments):
        # Generate random starting positions for the people
        people_positions = [(random.randint(0, grid_width-1), random.randint(0, grid_height-1)) for j in range(num_people)]
        # Run the experiment and add the results to the list
        results.append(run_experiment(grid_width, grid_height, num_people, people_positions))

    # Return the results list
    return results

# Function to calculate statistics from the results
def calculate_statistics(results):
    # Calculate the total moves for each person across all experiments
    total_moves = [sum([result[i] for result in results]) for i in range(len(results[0]))]
    # Calculate the longest and shortest runs for each person
    longest_runs = [max([result[i] for result in results]) for i in range(len(results[0]))]
    shortest_runs = [min([result[i] for result in results]) for i in range(len(results[0]))]
    # Calculate the average run for each person
    average_runs = [total_moves[i]/len(results) for i in range(len(total_moves))]
    # Return the statistics as a dictionary
    return {"total_moves": total_moves, "longest_runs": longest_runs, "shortest_runs": shortest_runs, "average_runs": average_runs}


    
print_intro()
grade_choice = grade_choice()


if grade_choice == "a":
    player_1_name = input("Enter the name of the first player: ")
    player_2_name = input("Enter the name of the second player: ")
    
     # Set up the grid
    grid_size = 5
    grid = [[0 for j in range(grid_size)] for i in range(grid_size)]

    # Place the two people in opposite corners
    player1_x, player1_y = 0, 0
    player2_x, player2_y = grid_size-1, grid_size-1

    # Set up the counters for each person
    player1_moves = 0
    player2_moves = 0

    # Loop until the two people meet
    while (player1_x, player1_y) != (player2_x, player2_y):
        # Move person 1
        player1_x += random.choice([-1, 0, 1])
        player1_y += random.choice([-1, 0, 1])
        player1_moves += 1
        
        # Move person 2
        player2_x += random.choice([-1, 0, 1])
        player2_y += random.choice([-1, 0, 1])
        player2_moves += 1

    # Display the happy graphics and statistics
    print("Woohoo! You guys have found each other!")
    print(player_1_name, "took", player1_moves, "moves")
    print(player_2_name, "took", player2_moves, "moves")
    
elif grade_choice == "b":
    # Set up the grid
    grid_width = 7
    grid_height = 5
    grid = [[0 for j in range(grid_width)] for i in range(grid_height)]

    # Get the number of people and their starting positions
    num_people = int(input("Enter the number of people: "))
    people_positions = []
    for i in range(num_people):
        x = int(input("Enter starting x position for person " + str(i+1) + ": "))
        y = int(input("Enter starting y position for person " + str(i+1) + ": "))
        people_positions.append((x, y))

    # Set up the counters for each person
    moves_counters = [0 for i in range(num_people)]

    # Loop until all people meet
    while len(set(people_positions)) > 1:
        for i in range(num_people):
            # Move each person
            x, y = people_positions[i]
            x += random.choice([-1, 0, 1])
            y += random.choice([-1, 0, 1])
            x = max(0, min(x, grid_width-1))
            y = max(0, min(y, grid_height-1))
            people_positions[i] = (x, y)
            moves_counters[i] += 1

    # Display the happy graphics and statistics
    print("They found each other!")
    for i in range(num_people):
        print("Person", i+1, "took", moves_counters[i], "moves")
        
elif grade_choice == "c":
    # Get user input for the grid size and number of people
    grid_width = int(input("Enter the grid width: "))
    grid_height = int(input("Enter the grid height: "))
    num_people = int(input("Enter the number of people: "))

    # Get user input for the number of experiments to run
    num_experiments = int(input("Enter the number of experiments to run: "))

    # Run the experiments
    results = run_experiments(num_experiments, grid_width, grid_height, num_people)

    # Calculate and display the statistics
    statistics = calculate_statistics(results)
    print("Total moves:", statistics["total_moves"])
    print("Longest runs:", statistics["longest_runs"])
    print("Shortest runs:", statistics["shortest_runs"])
    print("Average runs:", statistics["average_runs"])