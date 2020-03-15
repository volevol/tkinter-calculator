import tkinter as tk
import operator

root = tk.Tk()
root.title("Calculator")
root.geometry("362x325")

# Data
equation = []


# Functions

# Main functions
def add(eq, sign):
    """Adds a character to the "equation" list, consisting of two
    numbers and an operation sign between them"""
    print(sign, end=" ")
    add_more(eq, sign)
    print(eq)
    if len(eq) > 3:
        count(eq)
        print(eq)


def count(eq):
    """If the list of "equations" is full, he considers the first
    two numbers with the corresponding sign of the operation between
    them and rewrites the list, placing the solution as one of the
    numbers for subsequent operations. The sign of the next operation
    is also saved."""
    if eq[1] == "+":
        eq[0] = float(eq[0]) + float(eq[2])
    elif eq[1] == "-":
        eq[0] = float(eq[0]) - float(eq[2])
    elif eq[1] == "*":
        eq[0] = float(eq[0]) * float(eq[2])
    elif eq[1] == "/":
        if eq[2] == "0":
            print("Error. Division by zero")
            eq.pop(0)
            eq.pop(0)
            eq.pop(0)
            eq.pop(0)
            return eq
        else:
            eq[0] = float(eq[0]) / float(eq[2])
    else:
        print("Unsupported operation")
    eq.pop(1)
    eq.pop(1)
    eq[0] = str(eq[0])
    return eq


def add_more(eq, sign):
    """Adds a character to the "equation" list, consisting of two numbers
    and an operation sign between them"""
    if sign.isdigit():
        if len(eq) > 1 and eq[-1].replace('.', '', 1).isdigit():
            eq[-1] += sign
        else:
            eq += [sign]
    else:
        if len(eq) > 1 and not eq[-1].replace('.', '', 1).isdigit():
            eq[-1] = sign
        else:
            eq += [sign]
            if not eq[0].replace('.', '', 1).replace('-', '', 1).isdigit():
                eq.pop()
    return eq


# Number functions
def add_x(x):
    """It takes a character from a button and sends it to add()"""
    def f():
        add(equation, x)

    return f


# Special functions
def c():
    pass


def equal():
    pass


# Output labels
process_label = tk.Label(root, anchor=tk.E, text="2+2*2", width=24, font=("Arial", 18), bg="gray", fg="gray20")
answer_label = tk.Label(root, anchor=tk.E, text="8", width=24, font=("Arial", 18), bg="gray")

# Number labels
buttons = []
for i in range(9):
    buttons.append(tk.Button(root, text=str((i + 1) % 10), width=4, font=("Arial", 18),
                             bg="gray", command=add_x(str(i + 1))))
buttons.append(tk.Button(root, text="0", width=4, font=("Arial", 18),
                         bg="gray", command=add_x("0")))

# Math labels
button_add = tk.Button(root, text="+", width=4, font=("Arial", 18), bg="gray", command=add_x("+"))
button_subtract = tk.Button(root, text="-", width=4, font=("Arial", 18), bg="gray", command=add_x("-"))
button_multiply = tk.Button(root, text="*", width=4, font=("Arial", 18), bg="gray", command=add_x("*"))
button_divide = tk.Button(root, text="/", width=4, font=("Arial", 18), bg="gray", command=add_x("/"))

# Special labels
button_c = tk.Button(root, text="C", width=4, font=("Arial", 18), bg="gray", command=c)
button_equal = tk.Button(root, text="=", width=4, font=("Arial", 18), bg="gray", command=equal)

# PLACE Output labels
process_label.place(x=10, y=10)
answer_label.place(x=10, y=50)

# PLACE Number labels
for i in range(len(buttons) - 1):
    buttons[i].place(x=10 + 92 * (i % 3), y=100 + 55 * (i // 3))
buttons[9].place(x=100, y=265)

# PLACE Math labels
button_add.place(x=286, y=100)
button_subtract.place(x=286, y=155)
button_multiply.place(x=286, y=210)
button_divide.place(x=286, y=265)

# PLACE Special labels
button_c.place(x=10, y=265)
button_equal.place(x=194, y=265)

root.mainloop()

# выглядит страшно
# как минимум гуи стоит выносить в отдельный файл
# а функции в отдельный

# а ты регулярки не использовал?
# чтобы строку разбить тип на числа и знаки
