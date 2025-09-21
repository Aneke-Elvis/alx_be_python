# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# --- Core Logic to Generate Reminder ---
# This is where the fix is applied.

# First, determine the base message based on priority using match...case
match priority:
    case "high":
        base_message = f"is a **high priority** task"
    case "medium":
        base_message = f"is a **medium priority** task"
    case "low":
        base_message = f"is a **low priority** task."
    case _:
        # Handles cases where priority is not one of the expected values
        base_message = "is a task with an unknown priority"

# Next, use an if statement to add time-bound information
if time_bound == "yes":
    # If it's time-bound, add the "immediate attention" phrase.
    final_message = f"'{task}' {base_message} that requires immediate attention today!"
elif priority == "low" and time_bound == "no":
    # Special message for low-priority, non-time-bound tasks.
    final_message = f"Note: '{task}' {base_message} Consider completing it when you have free time."
else:
    # Default case for other non-time-bound tasks.
    final_message = f"'{task}' {base_message}."

# Print the customized reminder
print("\Reminder:", final_message)