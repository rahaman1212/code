import calculator
import tkinter as tk


window = tk.Tk()
window.title("calculator".upper())

label1 = tk.Label(text="WELCOME TO MY BASIC CALCULATOR!!!".upper())
label1.pack()

tk.Label(window, text="ENTER FIRST NUMBER:").pack()
num1_entry = tk.Entry(window)
num1_entry.pack()
 

tk.Label(window, text="ENTER ANY OPERATOR:").pack()
operator_entry = tk.Entry(window)
operator_entry.pack()


tk.Label(window, text="ENTER SECOND NUMBER:").pack()
num2_entry = tk.Entry(window)
num2_entry.pack()

# Result label
result_label = tk.Label(window, text="RESULTS = 👉 ")
result_label.pack()

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operator = operator_entry.get()
        if operator == "+":
            result = calculator.add(num1, num2)
        elif operator == "-":
            result = calculator.subtract(num1, num2)
        elif operator == "*":
            result = calculator.multiply(num1, num2)
        elif operator == "/":
            result = calculator.divide(num1, num2)
        elif operator == "%":
            result = calculator.modulo(num1, num2)
        else:
            result = "Invalid operator ☠️💀👹"
    except ValueError:
        result = "Error: Invalid input"
    result_label.config(text=f"RESULTS = 👉 {result}")

tk.Button(window, text="ANSWER", command=calculate).pack()

window.mainloop()