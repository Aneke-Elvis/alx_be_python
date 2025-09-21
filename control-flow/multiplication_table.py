# Prompt the user for a number and convert the input to an integer
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate from 1 to 10
for i in range(1, 11):
    # Calculate the product of the number and the current iteration
    product = number * i
    
    # Print the multiplication line in the specified format
    print(f"{number} * {i} = {product}")