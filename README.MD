# 🚀 Bootcamp - Lesson 01

## 📝 Overview
This project is a simple Python program that calculates the **total annual bonus** based on a user's **monthly salary** and **bonus percentage**. The program ensures input validation and prevents common errors that could lead to incorrect calculations or crashes.

---

## 🎯 **Functionality**
1. **Greets the user and requests their name.**
2. **Prompts the user to input their salary and bonus percentage.**
3. **Validates input to prevent errors (e.g., negative values, non-numeric input).**
4. **Calculates the annual bonus, including an additional fixed amount of R$ 1000.**
5. **Displays the correctly formatted result.**

---

## 🛠 **Code Implementation**
```python
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
````
## 🐞 Bug Fixes & Improvements
Below is a list of **potential issues** in the previous version of the code and how they were **resolved**.

| 🐞 Bug | 💥 Cause | 🔧 Solution |
|--------|---------|------------|
| **1️⃣ Invalid Input** | The user may enter a **non-numeric** value (e.g., `"five thousand"`) for salary or bonus, causing a `ValueError`. | **Use `try-except`** to catch errors and prevent crashes. |
| **2️⃣ Negative Values** | If `salary` or `bonus` is negative, the calculation may produce **incorrect results**. | **Ensure values are positive** before processing. |
| **3️⃣ Empty Input** | Pressing `Enter` without typing anything causes an error when converting `""` to `float`. | **Check if input is empty** before converting it. |
| **4️⃣ Extra Spaces in Input** | Input with **leading/trailing spaces** may cause unexpected behavior. | The **`.strip()` function** ensures clean input. |
| **5️⃣ Formatting Issues** | Printing `total` directly may display unformatted numbers. | **Use `:.2f` formatting** to ensure two decimal places. |
| **6️⃣ Incorrect Bonus Calculation** | The previous code **assumed** the bonus was a direct multiplier instead of a percentage. | **Clarify input format** (`1.5 = 150%`) and correctly apply the percentage. |

## 🎯 Key Takeaways
✔️ **Better Input Validation** → Prevents crashes and incorrect calculations.  
✔️ **Improved User Experience** → Clearer instructions and better formatting.  
✔️ **More Robust Calculations** → Ensures bonus is applied correctly.  

## 📌 How to Run
To run this program, make sure you have **Python 3.x** installed, then execute:

```bash
python main.py
```
## 👨‍💻 Author
👤 **Luiz Otavio Delgado**  
📧 **Contact:** luizotavio.delgado@gmail.com  
🔗 **GitHub:** https://github.com/luizodelgado  
