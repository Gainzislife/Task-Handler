# This is a program that helps users view and manage their tasks at work

# Import modules
from datetime import date, datetime
from os import path

# Get current day's date
today = date.today()

# Read users from textfile
user_file = open("Task 25/user.txt", "r")

# Empty string to store the user file data in
info = ""

# Save everything in one line
for line in user_file:
    info += line.strip() + " "

# Close user.txt
user_file.close()

# Remove commas and split string at spaces
info = info.replace(",", "").split()

# Register user function
def reg_user():
    print("\n----- REGISTER NEW USER -----")

    # Loop continuously
    while True:
        # Boolean to check if a username exists
        correct_credentials = True # True = username does not exist
        
        new_user = input("Enter new username: ")

        # Get the length of the info list
        length = len(info)

        for i in range(0, length):
            # Compare the input only with usernames, not the passwords
            if i % 2 == 0 and new_user == info[i]:
                print("\nUsername already exists. Try a different one!")
                correct_credentials = False # False = username exists
                break # Break out of the for loop

        # If the username does not exist yet
        if correct_credentials:
            new_pass = input("Enter password for new user: ")
            compare = input("Confirm password: ")

            # Check if the password entered twice are the same
            if new_pass != compare:
                print("\n!!!!! Warning! Passwords don't match - New user NOT added. !!!!!")
                break # End while loop
            else:
                # Append entered data to the end of the user file
                user_file = open("Task 25/user.txt", "a")
                user_file.write("\n" + new_user + ", " + new_pass)
                user_file.close()
                print("\nNew user added.")
                break # End while loop

    return

# Add a task to a user
def add_task():
    print("\n----- ADD NEW TASK -----")
    to_user = input("Username of the person the task should be added to: ")
    task_title = input("Title of the task: ")
    task_description = input("Describe the task: ")
    due_date = input("Due date of the task: ")
    current_date = today.strftime("%d %b %Y") # Output is: day + month abreviation + year

    # Append the new task to the end of the tasks file
    task_file = open("Task 25/tasks.txt", "a")
    task_file.write("\n" + to_user + ", " + task_title + ", " + task_description + ", " + current_date + ", " + due_date + ", No")
    task_file.close()

    print("\nNew task added for " + to_user)
    return

# View all tasks is the file
def view_all():
    print("\n----- VIEW ALL TASKS -----")

    task_file = open("Task 25/tasks.txt", "r")

    # Run through file and save the data in variables
    for line in task_file:
        data = line.split(", ")
        to_user = data[0]
        task_title = data[1]
        task_description = data[2]
        add_date = data[3]
        due_date = data[4]
        completed = data[5]

        print("Task: \t\t\t" + task_title)
        print("Assigned to: \t\t" + to_user)
        print("Task description: \t" + task_description)
        print("Date assigned: \t\t" + add_date)
        print("Due date: \t\t" + due_date)
        print("Task complete? \t\t" + completed)

    task_file.close()
    return

# View logged in user's tasks
def view_mine():
    print("\n----- VIEW " + username.upper() + "'S TASKS -----")

    num = 0 # To track the number of tasks for a certain user

    # Empty dictionary to save tasks of current user in
    user_tasks = {}

    # Empty list to save usernames to
    users = []

    # Open tasks.txt
    f = open("Task 25/tasks.txt", "r")
    # Save tasks in a list
    task_file = f.readlines()
    # Close file
    f.close()

    # Open user.txt
    f = open("Task 25/user.txt", "r")
    # Save users in a list
    for line in f:
        user_data = line.split(", ")
        users.append(user_data[0])
    f.close()

    # Length of task_file
    task_file_length = len(task_file)

    # Loop through task_file
    for i in range(task_file_length):
        task_data = task_file[i].strip().split(", ")
        num += 1 # Count how many tasks there are
        user_tasks[num] = task_data # Assign task data to a number in the dictionary

    # Loop through and print dictionary
    for index in user_tasks:
        # Print only current user's tasks
        if user_tasks[index][0] == username:
            print("TASK #: " + str(index))
            print("Task Title: \t\t" + str(user_tasks[index][1]))
            print("Task Description: \t" + str(user_tasks[index][2]))
            print("Date Assigned: \t\t" + str(user_tasks[index][3]))
            print("Due Date: \t\t" + str(user_tasks[index][4]))
            print("Task Complete? \t\t" + str(user_tasks[index][5]))
            print("")

    # Ask user to choose a task
    select_task = int(input("Select a TASK # (-1 for Main Menu): "))

    # Exit if -1 is entered
    if select_task == -1:
        return

    # The current user can only edit his/her own tasks
    elif select_task in user_tasks and user_tasks[select_task][0] == username:
        print("TASK #" + str(select_task) + " SELECTED")

        # Continue asking input until something valid is entered
        while True:
            # Save user input is option variable
            option = input("Mark task as complete (C) or edit task (E)? ")

            # Mark the task as complete then exit the loop
            if option == "C" or option == "c":
                print("Task marked as complete.")
                user_tasks[select_task][5] = "Yes"
                break

            # Ask the user how to edit the task
            elif option == "E" or option == "e":

                # The task has to be incomplete to be editable
                if user_tasks[select_task][5] == "No":
                    # Save the user's input in the edit variable
                    edit = input("Change TASK TO DIFFERENT USER (T) or DUE DATE (D) of the task? ")

                    if edit == "T" or edit == "t":
                        
                        # Continue asking until a valid username is entered
                        while True:
                            change_user = input("Change task to which user? (-1 to abort) ")

                            # Change the user if the username exists
                            if change_user in users:
                                user_tasks[select_task][0] = change_user
                                break

                            # Break the loop
                            elif change_user == "-1":
                                break

                            # Error message when an invalid username is entered
                            else:
                                print("No such user.")

                    elif edit == "D" or edit == "d":
                        new_date = input("New DUE DATE(dd Mon year): ")
                        user_tasks[select_task][4] = new_date

                    else:
                        print("Unknown input.")
                else:
                    print("Can't edit completed tasks.")

                break
            # Break loop if this is entered
            elif option == "X" or option == "x":
                break
            else:
                # Error message for wrong input
                print("Wrong input!! Enter a 'C', 'E' or 'X' to abort.")

    else:
        # Error message
        print("Task not found!")

    # Open tasks file
    f = open("Task 25/tasks.txt", "w")

    # Combine each dictionary value into one long string
    for key in user_tasks:
        f.write(", ".join(user_tasks[key]) + "\n")

    # Close tasks file
    f.close()

    return

def generate_reports():

    # Open tasks.txt and save it in a list
    f = open("Task 25/tasks.txt", "r")
    task_list = f.readlines()
    f.close()

    # Read user.txt and save it in a list
    f = open("Task 25/user.txt", "r")
    user_list = f.readlines()
    f.close()

    # Total users
    total_users = len(user_list)

    # Empty user dictionary
    user_dict = {} # Count a user's total tasks
    user_tComplete_dict = {} # Count complete tasks
    user_tOverdue_dict = {} # Count overdue and incomplete tasks
    user_percent_dict = {} # Determine each user's % of tasks
    user_tComplete_percent_dict = {} # Determine % completed tasks
    user_tIncomplete_percent_dict = {} # Determine % incompleted tasks
    user_tOverdue_percent_dict = {} # Determine % incomplete and overdue tasks

    # Variable to track completed tasks
    completed_tasks = 0

    # Variable to track overdue tasks
    overdue_tasks = 0

    # Determine total tasks
    total_tasks = len(task_list)

    # Create dictionary with usernames as keys and assign 0 to each value
    for i in range(total_users):
        user_data = user_list[i].strip().split(", ")

        user_dict[user_data[0]] = 0
        user_tComplete_dict[user_data[0]] = 0
        user_tOverdue_dict[user_data[0]] = 0

    # Loop through each task
    for i in range(total_tasks):
        # Split each line up at comma
        task_data = task_list[i].strip().split(", ")

        # Add one to user's total tasks
        user_dict[task_data[0]] += 1

        # Count completed tasks
        if task_data[-1] == "Yes":
            completed_tasks += 1
            user_tComplete_dict[task_data[0]] += 1

        # Convert task_data[i] date(string) to date
        task_due_date = datetime.strptime(task_data[-2], "%d %b %Y")

        # Get report's date
        report_date = datetime.today()

        # Check if tasks are incomplete and overdue
        if task_data[-1] == "No" and task_due_date < report_date:
            overdue_tasks += 1

            # Add as overdue to specific user
            user_tOverdue_dict[task_data[0]] += 1

    # Incomplete tasks
    incomplete_tasks = total_tasks - completed_tasks

    # Percentage values
    incom_percent = round(incomplete_tasks / total_tasks * 100)
    overdue_percent = round(overdue_tasks / total_tasks * 100)

    # Create TASK_OVERVIEW.TXT
    f = open("Task 25/task_overview.txt", "w")
    f.write(
        "Total Tasks:       " + str(total_tasks) +
        "\nCompleted Tasks:   " + str(completed_tasks) +
        "\nIncompleted Tasks: " + str(incomplete_tasks) +
        "\nOverdue Tasks:     " + str(overdue_tasks) +
        "\nIncomplete (%):    " + str(incom_percent) +
        "\nOverdue (%):       " + str(overdue_percent)
    )

    # Percentage total to each user
    for key in user_dict:
        user_percent_dict[key] = round(user_dict[key] / total_tasks * 100)
        user_tComplete_percent_dict[key] = round(user_tComplete_dict[key] / user_dict[key] * 100)
        user_tIncomplete_percent_dict[key] = round((user_dict[key] - user_tComplete_dict[key]) / user_dict[key] * 100)
        user_tOverdue_percent_dict[key] = round(user_tOverdue_dict[key] / user_dict[key] * 100)

    # Create USER_OVERVIEW.TXT
    f = open("Task 25/user_overview.txt", "w")
    f.write(
        "Total Users: \t" + str(total_users) +
        "\nTotal Tasks: \t" + str(total_tasks) +
        "\nTasks Assigned To Each User (%): \t" + str(user_percent_dict) +
        "\nTasks Completed By Each User (%): \t" + str(user_tComplete_percent_dict) +
        "\nEach User's Incomplete Tasks (%): \t" + str(user_tIncomplete_percent_dict) +
        "\nIncomplete & Overdue Tasks (%): \t" + str(user_tOverdue_percent_dict)
    )

    return

def statistics():
    print("\n----- STATISTICS -----")
    print("TASK OVERVIEW")

    # Open task_overview and display to screen
    f = open("Task 25/task_overview.txt", "r")
    for line in f:
        print(line, end="")
    f.close()

    print("\n\nUSER OVERVIEW")

    # Open user_overview and display to screen
    f = open("Task 25/user_overview.txt", "r")
    for line in f:
        print(line, end="")
    f.close()

    print("")

    return

print("\n----- LOGIN -----")

# Continue asking for input details until it is correct
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the username exists
    if username in info:
        index = info.index(username) + 1
        usr_password = info[index]

        # Check if the password matches the username
        if usr_password == password:
            print("\nSuccessful login.")
            break
    else:
        print("!!!!! Incorrect username or password! Try again. !!!!!")

# Loop until 'e' is entered
while True:
    # Check if logged in as admin
    if username == "admin":
        print("\n----- LOGGED IN AS ADMIN -----")
        print("Please select one of the following options:")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("gr - generate reports")
        print("s - statistics")
        print("e - exit")

        # Save the user's option as menu_option
        menu_option = input("")

        # Register a new user
        if menu_option == "r":
            reg_user()
        # Exit the program
        elif menu_option == "e":
            print("\n----- GOODBYE -----")
            break
        # Add a task
        elif menu_option == "a":
            add_task()
        # View all tasks
        elif menu_option == "va":
            view_all()
        # View current user's tasks
        elif menu_option == "vm":
            view_mine()
        
        # View statistics
        elif menu_option == "s":
            # If files were generated otherwise generate them
            if path.exists("Task 25/task_overview.txt") and path.exists("Task 25/user_overview.txt"):
                statistics()
            else:
                generate_reports()
                statistics()

        # Generate reports
        elif menu_option == "gr":
            print("\nGenerating....")
            generate_reports()
            print("Done.")
        else:
            # If anything other than the given options are entered, show an error
            print("\n!!!!! UNKNOWN OPTION. TRY AGAIN !!!!!")

    else:
        # Show menu options
        print("\n----- LOGGED IN AS " + username.upper() + " -----")
        print("Please select one of the following options:")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit")

        menu_option = input("")

        # Register a new user
        if menu_option == "e":
            print("\n----- GOODBYE -----")
            break
        # Add a task
        elif menu_option == "a":
            add_task()
        # View all tasks
        elif menu_option == "va":
            view_all()
        # View current user's tasks
        elif menu_option == "vm":
            view_mine()
        else:
            # If anything other than the given options are entered, show an error
            print("\n!!!!! UNKNOWN OPTION. TRY AGAIN !!!!!")