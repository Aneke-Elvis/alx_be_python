# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Get the current date and time, save it in `current_date`,
    print it in "YYYY-MM-DD HH:MM:SS" format and return the datetime object.
    """
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date

def calculate_future_date(days):
    """
    Calculate the date after `days` days from now.
    Saves the result in `future_date`, prints it as "YYYY-MM-DD",
    and returns the datetime object.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def get_integer_from_user(prompt="Enter the number of days to add to the current date: "):
    """
    Prompt the user until they enter a valid integer. Returns the integer.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("That's not a valid whole number. Please enter an integer (e.g., 10 or -3).")

if __name__ == "__main__":
    # Part 1: display the current date and time
    display_current_datetime()

    # Part 2: ask the user for number of days and calculate future date
    days_to_add = get_integer_from_user()
    calculate_future_date(days_to_add)
