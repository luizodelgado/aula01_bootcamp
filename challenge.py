# 1. Greet the user and request name input
name = input("Hello! Enter your name: ").strip()

# 2. Function to validate and obtain a positive numeric value
def get_value(message):
    while True:
        try:
            value = float(input(message).strip().replace(",", "."))  # Supports comma as decimal separator
            if value < 0:
                print("Error: The value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

# 3. Request salary and bonus (percentage)
salary = get_value(f"Welcome, {name}! Enter your monthly salary: ")
bonus_percentage = get_value(f"{name}, enter your bonus percentage (e.g., 10 for 10%): ")

# 4. Calculate the total annual bonus (including 1000 fixed additional)
bonus_total = (salary * (1 + (bonus_percentage / 100))) + 1000

# 5. Display the correctly formatted result
print(f"{name}, your total annual bonus is: R$ {bonus_total:.2f}")