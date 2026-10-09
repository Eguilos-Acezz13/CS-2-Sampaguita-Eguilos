
# Functions for basic arithmetic operations
def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero."
    return num1 / num2


# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter choice: ")

# Call the selected function
if choice == "1":
    result = add_numbers(num1, num2)
elif choice == "2":
    result = subtract_numbers(num1, num2)
elif choice == "3":
    result = multiply_numbers(num1, num2)
elif choice == "4":
    result = divide_numbers(num1, num2)
else:
    result = "Invalid operation."

# Display the result
print("Result:", result)

#Short Reflection

#1. What functions did you create?
#I created functions for addition, subtraction, multiplication, and division.

#2. What parameters did your functions use?
#Each function used num1 and num2.

#3. What arguments were passed when the functions were called?
#The two numbers entered by the user were passed as arguments.

#4. How did your program use the returned value?
#It stored the returned value in the result variable and displayed it.

#5. Why is it better to divide the program into functions?
#Functions make the code more organized, reusable, and easier to understand and fix.
