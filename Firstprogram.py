import tkinter as tk

def input(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)
#make window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")


entry = tk.Entry(window, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]


frame = tk.Frame(window)
frame.pack()


row_index = 0
for row in buttons:
    col_index = 0
    for button_text in row:
        button = tk.Button(frame, text=button_text, font=("Arial", 18), width=5, height=2,
                           command=lambda text=button_text: input(text))
        button.grid(row=row_index, column=col_index, padx=5, pady=5)
        col_index += 1
    row_index += 1


window.mainloop()




import math

operator = input("enter an operator( - * / log root square sin cos tan arcsin):")

if operator in ["+", "-", "*", "/"]:
   number1 = float(input("enter the first number:"))
   number2 = float(input("enter the second number:"))



if operator == "+":
    print(number1 + number2)
    
elif operator == "-":
    print(number1 - number2)

elif operator == "*":
    print(number1 * number2)    

elif operator == "/":
        if number2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(number1 / number2)

elif operator == "log":
    number = float(input("enter a number greater than zero:"))
    base = input("input the base:")
    if base == "":
            result = math.log(number)
            print(f"ln({number}) = {result}")
            
else:
            base = float(input("input the base:"))
            number = float(input("enter a number greater than zero:"))
        
            if base <= 0 or base == 1:
                print("Error: Base must be > 0 and ≠ 1.")
                result = math.log(number, base)
                print(f"log base {base} of {number} = {result}")

if operator == "root":
    number = float(input("enter a number greater than zero:"))
    if number < 0:
        print("Error") 
    else: 
         result = math.sqrt(number)
         print(f"Square root of {number} = {result}")     

elif operator == "square":
     number = float(input("enter a number:"))
     result =(number*number)
     print(f"{number} squared:{result}")

elif operator == "sin":
     number = float(input("enter an angle:"))
     radians = math.radians(number)
     result = math.sin(number)
     print(f"sin{number}: {result}")

elif operator == "cos":
     number = float(input("enter an angle:"))
     radians =math.radians(number)
     result = math.cos(number)
     print(f"cos{number}: {result}")
     
elif operator == "tan":
     number = float(input("enter an angle:"))
     radians =math.radians(number)
     result = math.tan(number)
     print(f"cos{number}: {result}")

elif operator == "arcsin":
     number = float(input("enter an angle:"))
     if number >-1 or number < 1:
      print("error out of domain")
else: 
     number = float(input("enter a number:"))
     radians =math.radians(number)
     result = math.asin(number)
     print(f"arcsin{number}: {result}")



    
