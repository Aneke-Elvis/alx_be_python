# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the message variable
message = ""
time_message = ""

# Use a match...case statement to set the reminder based on priority
match priority:
    case "high":
        message = f"'{task}' is a **high priority** task"
    case "medium":
        message = f"'{task}' is a **medium priority** task"
    case "low":
        message = f"Note: '{task}' is a **low priority** task. Consider completing it when you have free time."
    case _:
        message = f"'{task}' is a task" # Default case for invalid priority

# Use an if statement to modify the message if the task is time-bound
if time_bound == "yes":
    time_message = " that requires immediate attention today!"
elif time_bound == "no" and priority != "low":
    # For non-time-bound tasks that are not low priority, a simple message is best
    time_message = ". You can complete it at your convenience."
else:
    # No additional message for low-priority, non-time-bound tasks
    time_message = ""

# Combine and print the final reminder
print("\nReminder:", message + time_message)