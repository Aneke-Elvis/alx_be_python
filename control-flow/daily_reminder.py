# daily_reminder.py

# 1. Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# 2. Process the Task Based on Priority and Time Sensitivity
# Use a match...case statement for priority and build the core message.
match priority:
    case "high":
        priority_message = f"is a **high priority** task"
    case "medium":
        priority_message = f"is a **medium priority** task"
    case "low":
        priority_message = f"is a **low priority** task."
    case _:
        # Default case for invalid priority
        priority_message = f"is a task with an unknown priority"

# Use an if statement to modify the message if the task is time-bound.
if time_bound == "yes":
    # This combines the task, the priority message, and the time-bound message.
    final_reminder = f"'{task}' {priority_message} that requires immediate attention today!"
elif priority == "low" and time_bound == "no":
    # This handles the specific "low priority, non-time-bound" case.
    final_reminder = f"Note: '{task}' {priority_message} Consider completing it when you have free time."
else:
    # This handles all other non-time-bound cases (medium, high, or unknown priority).
    final_reminder = f"'{task}' {priority_message}."

# 3. Provide a Customized Reminder
# The fix is here: Ensure the print statement has the exact "Reminder: " prefix.
print(f"Reminder: {final_reminder}")