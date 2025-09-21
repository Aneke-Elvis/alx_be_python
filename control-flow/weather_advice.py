# weather_advice.py
# Simple program that recommends clothing based on the weather.

def main():
    # Ask the user for the weather. The prompt matches the assignment.
    # .strip() removes extra spaces; .lower() makes the input case-insensitive.
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    # Branching with if / elif / else to choose the recommendation
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        # Handles any unexpected input (e.g., "windy", "cloudy", typos)
        print("Sorry, I don't have recommendations for this weather.")

# Standard Python idiom so the program runs when executed as a script
if __name__ == "__main__":
    main()
