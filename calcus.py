import calculator


try:
    print("❤️ WELCOME TO MY BASIC CALCULATOR👌")
    print("😎 HEY PLEASE ENTER NUMBERS ONLY🤬!!!")
    num1 = int(input("ENTER FIRST NUMBER: "))
    operator = input("ENTER ANY OPERATOR: ")
    num2 = int(input("ENTER SECOND NUMBER: "))


    def calculate():
        if operator == "+":
            return calculator.add(num1, num2)
        elif operator == "-":
            return calculator.subtract(num1, num2)
        elif operator == "*":
            return calculator.multiply(num1, num2)
        elif operator == "/":
            return calculator.divide(num1, num2)
        elif operator == "%": 
            return calculator.modulo(num1, num2)
        else:
            print("you cannot calculate☠️💀👹")


    results = calculate()
    print(f"RESULTS = 👉 {results}")

except ValueError:
    print("INVALID INPUT👹☠️💀")
