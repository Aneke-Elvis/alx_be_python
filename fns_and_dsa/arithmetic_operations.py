#create a function
def perform_operation( numb1: float, numb2: float, operation: str):
    if operation == "add":
        return numb1 + numb2
    elif operation == "subtract":
        return numb1 - numb2
    elif operation == "multiply":
        return numb1 * numb2
    elif operation == "division":
        if numb2 == 0:
            return "Error: Division by zero is not allowed"
        return numb1 / numb2
    else:
        return "Error: Invalid operation"
print(perform_operation(2, 0.1, "division"))
     
