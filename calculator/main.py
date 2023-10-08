import tkinter as tk
import math

root = tk.Tk()
root.configure(bg="black")
root.title("计算器")

result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result, font=('Arial', 20))
result_entry.configure(bg="black", fg="white")
result_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)



def number_click(number):
    current = result.get()
    if current == '0':
        result.set(number)
    else:
        result.set(current + number)

def operator_click(operator):
    current = result.get()
    if current[-1] in ['+', '-', '*', '/']:
        result.set(current[:-1] + operator)
    else:
        result.set(current + operator)

def equal_click():
    current = result.get()
    if current[-1] in ['+', '-', '*', '/']:
        current = current[:-1]
    try:
        result.set(eval(current))
    except ZeroDivisionError:
        result.set("除数不能为零")
    except:
        result.set("输入有误")

def clear_click():
    result.set("0")

def sin_click():
    current = result.get()
    try:
        result.set(math.sin(eval(current)))
    except:
        result.set("输入有误")

def cos_click():
    current = result.get()
    try:
        result.set(math.cos(eval(current)))
    except:
        result.set("输入有误")

def pow_click():
    current = result.get()
    try:
        result.set(eval(current)**2)
    except:
        result.set("输入有误")
buttons = [
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("0", 5, 0),
    (".", 5, 1)
]

for btn_text, row, column in buttons:
    btn = tk.Button(root, text=btn_text, font=('Arial', 20), command=lambda text=btn_text: number_click(text), width=3, height=1, bg="gray")
    btn.grid(row=row, column=column, padx=5, pady=5)

btn_clear = tk.Button(root, text="C", font=('Arial', 20), command=clear_click, width=3, height=1)
btn_clear.grid(row=1, column=0, padx=5, pady=5)

btn_divide = tk.Button(root, text="/", font=('Arial', 20), command=lambda: operator_click("/"), width=3, height=1)
btn_divide.grid(row=1, column=1, padx=5, pady=5)

btn_multiply = tk.Button(root, text="*", font=('Arial', 20), command=lambda: operator_click("*"), width=3, height=1)
btn_multiply.grid(row=1, column=2, padx=5, pady=5)

btn_minus = tk.Button(root, text="-", font=('Arial', 20), command=lambda: operator_click("-"), width=3, height=1, bg="orange")
btn_minus.grid(row=1, column=3, padx=5, pady=5)

btn_plus = tk.Button(root, text="+", font=('Arial', 20), command=lambda: operator_click("+"), width=3, height=1, bg="orange")
btn_plus.grid(row=2, column=3, padx=5, pady=5)

btn_dot = tk.Button(root, text=".", font=('Arial', 20), command=lambda: number_click("."), width=3, height=1, bg="gray")
btn_dot.grid(row=5, column=1, padx=5, pady=5)

btn_equal = tk.Button(root, text="=", font=('Arial', 20), command=equal_click, width=3, height=1, bg="gray")
btn_equal.grid(row=5, column=2, padx=5, pady=5)

btn_sin = tk.Button(root, text="sin", font=('Arial', 20), command=sin_click, width=3, height=1, bg="orange")
btn_sin.grid(row=3, column=3, padx=5, pady=5)

btn_cos = tk.Button(root, text="cos", font=('Arial', 20), command=cos_click, width=3, height=1, bg="orange")
btn_cos.grid(row=4, column=3, padx=5, pady=5)

btn_pow = tk.Button(root, text="^", font=('Arial', 20), command=pow_click, width=3, height=1, bg="orange")
btn_pow.grid(row=5, column=3, padx=5, pady=5)

root.mainloop()
