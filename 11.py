import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())
        
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                messagebox.showerror("Error", "Division by Zero!")
                return
            result = a / b
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid numbers!")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

tk.Label(root, text="Enter First Number:").pack()
entry_num1 = tk.Entry(root, width=20)
entry_num1.pack()

tk.Label(root, text="Enter Second Number:").pack()
entry_num2 = tk.Entry(root, width=20)
entry_num2.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0)
tk.Button(frame, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1)
tk.Button(frame, text="*", width=5, command=lambda: calculate("*")).grid(row=0, column=2)
tk.Button(frame, text="/", width=5, command=lambda: calculate("/")).grid(row=0, column=3)

label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()
