import tkinter as tk
import operator

root = tk.Tk()
root.title("Calculator")
root.geometry("362x325")

# Data
equation = []


# Functions

# Main functions

def init():
    """Sets blank lines to labels values"""
    process_label.configure(text="")
    answer_label.configure(text="")


def add(eq, sign):
    """Adds a character to the "equation" list, consisting of two numbers and an operation sign between them"""
    print(sign, end=" ")
    add_more(eq, sign)
    print(eq)
    if len(eq) > 3:
        count(eq)
        print(eq)


def count(eq):
    """If the list of "equations" is full, he considers the first two numbers with the corresponding sign of the
    operation between them and rewrites the list, placing the solution as one of the numbers for subsequent operations.
    The sign of the next operation is also saved."""
    ops = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv}
    if eq[1] == "/" and eq[2] == "0":
        print("Error. Division by zero")
        for _ in range(len(eq)):
            eq.pop(0)
        process_insert("")
        answer_insert("Error. Division by zero")
    else:
        eq[0] = str(ops[eq[1]](float(eq[0]), float(eq[2])))
        for _ in range(len(eq) - 2):
            eq.pop(1)
        answer_insert(eq)
    return eq


def add_more(eq, sign):
    """Adds a character to the "equation" list, consisting of two numbers and an operation sign between them"""
    if sign == "C":
        for _ in range(len(eq)):
            eq.pop(0)
        init()
        answer_insert("0")
    elif sign == "=":
        if not eq:
            answer_insert("0")
        elif len(eq) != 2:
            eq += [sign]
            answer_insert("0")
        elif len(eq) == 2:
            if eq[-1] != "=":
                text = process_label["text"][:-1]
                process_insert("")
                process_insert(text)
            eq[1] = sign
            answer_insert(eq)
    elif sign.isdigit():
        if len(eq) >= 1:
            if eq[-1] == "0":
                if sign != "0":
                    eq[-1] = sign
                    process_insert(sign, True)
            elif eq[-1].isdigit():
                eq[-1] += sign
                process_insert(sign)
            elif eq[-1] == "=":
                process_insert("")
                eq.pop()
                eq[0] = sign
                process_insert(sign, True)
            else:
                eq += [sign]
                process_insert(sign)
        else:
            eq += [sign]
            process_insert(sign)
    else:
        if len(eq) >= 1:
            if not eq[-1].isdigit():
                if eq[-1] == "=":
                    process_insert("")
                    process_insert(eq[0] + sign)
                else:
                    process_insert(sign, True)
                eq[-1] = sign
            else:
                eq += [sign]
                process_insert(sign)
    return eq


# Number functions
def add_x(x):
    """It takes a character from a button and sends it to add()"""

    def f():
        add(equation, x)

    return f


# GUI functions
def process_insert(sign, pop=False):
    if sign == "":
        process_label.configure(text="")
    else:
        if pop:
            text = process_label["text"][:-1] + sign
        else:
            text = process_label["text"] + sign
        process_label.configure(text=text)


def answer_insert(el):
    if isinstance(el, list):
        answer_label.configure(text=el[0])
    elif isinstance(el, str):
        answer_label.configure(text=el)
    else:
        print(el)


# Output labels
process_label = tk.Label(root, anchor=tk.E, text="2+2*2", width=24, font=("Arial", 18), bg="gray", fg="gray20")
answer_label = tk.Label(root, anchor=tk.E, text="8", width=24, font=("Arial", 18), bg="gray")

# Number labels
buttons = []
for i in range(9):
    buttons.append(tk.Button(root, text=str((i + 1) % 10), width=4, font=("Arial", 18), bg="gray",
                             command=add_x(str(i + 1))))
buttons.append(tk.Button(root, text="0", width=4, font=("Arial", 18), bg="gray", command=add_x("0")))

# Math labels
button_add = tk.Button(root, text="+", width=4, font=("Arial", 18), bg="gray", command=add_x("+"))
button_subtract = tk.Button(root, text="-", width=4, font=("Arial", 18), bg="gray", command=add_x("-"))
button_multiply = tk.Button(root, text="*", width=4, font=("Arial", 18), bg="gray", command=add_x("*"))
button_divide = tk.Button(root, text="/", width=4, font=("Arial", 18), bg="gray", command=add_x("/"))

# Special labels
button_c = tk.Button(root, text="C", width=4, font=("Arial", 18), bg="gray", command=add_x("C"))
button_equal = tk.Button(root, text="=", width=4, font=("Arial", 18), bg="gray", command=add_x("="))

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

init()

root.mainloop()

# выглядит страшно
# как минимум гуи стоит выносить в отдельный файл
# а функции в отдельный

# а ты регулярки не использовал?
# чтобы строку разбить тип на числа и знаки
