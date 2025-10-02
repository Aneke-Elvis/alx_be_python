# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Ask user for temperature
        temp_input = input("Enter the temperature to convert: ")

        # Validate that it's numeric (allows one decimal point and an optional leading minus)
        if not temp_input.replace(".", "", 1).isdigit() and not (temp_input.startswith("-") and temp_input[1:].replace(".", "", 1).isdigit()):
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_input)

        # Ask user for unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        else:
            raise ValueError("Invalid unit. Please enter C or F.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
