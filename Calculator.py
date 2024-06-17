# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

# Function to calculate percentage
def percentage(x, y):
    return (x * y) / 100

# Function to display the menu and get user choice
def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Exit")
    
    choice = input("Enter choice (1/2/3/4/5/6): ")
    return choice

# Calculator main function
def calculator():
    while True:
        choice = display_menu()
        
        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            
            if choice != '5':
                num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", percentage(num1, num2))
        elif choice == '6':
            print("Exiting calculator...")
            break
        else:
            print("Invalid input. Please enter 1-6.")

# Run the calculator
calculator()
