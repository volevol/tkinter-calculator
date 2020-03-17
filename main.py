import tkinter as tk
import operator

root = tk.Tk()
root.title("Calculator")
root.geometry("390x325")

# Data
equation = []


# Controller functions
def init():
    """Sets blank lines to labels values"""
    process_insert("clear")
    answer_insert("")


def add_x(x):
    """It takes a character from a button and sends it to add()"""

    def f():
        add(equation, x)

    return f


def add(eq, sign):
    """Adds a character to the "equation" list, consisting of two numbers and an operation sign between them"""
    print(sign, end=" ")
    add_more(eq, sign)
    print(eq)
    if len(eq) > 3:
        count(eq)
        print(eq)


def add_more(eq, sign):
    """Adds a character to the "equation" list, consisting of two numbers and an operation sign between them"""
    if sign == "C":
        for _ in range(len(eq)):
            eq.pop(0)
        init()
        answer_insert("0")
    elif sign == "CE":
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
                process_insert("clear")
                process_insert(text)
            eq[1] = sign
            answer_insert(eq)
    elif sign == "⇦":
        if len(eq) >= 1:
            if eq[-1].replace(".", "").isdigit():
                if eq[-1] is not "0":
                    if len(eq) == 1 and len(eq[-1]) == 1:
                        eq[-1] = "0"
                        process_insert("0", True)
                    else:
                        eq[-1] = eq[-1][:-1]
                        process_insert("", True)
                        if not eq[-1].isdigit() and len(eq[-1]) == 0:
                            eq.pop()
                            process_insert("", True)
            else:
                eq.pop()
                eq[-1] = eq[-1][:-1]
                if len(eq) == 1 and eq[-1] == "":
                    eq[-1] = "0"
                process_insert("", True)
                process_insert("", True)
    elif sign.isdigit():
        if len(eq) >= 1:
            if eq[-1] == "0":
                if sign != "0":
                    eq[-1] = sign
                    process_insert(sign, True)
            elif eq[-1] == "=":
                process_insert("clear")
                eq.pop()
                eq[0] = sign
                process_insert(sign, True)
            elif eq[-1].isdigit():
                eq[-1] += sign
                process_insert(sign)
            else:
                if "." in eq[-1]:
                    eq.pop()
                eq += [sign]
                process_insert(sign)
        else:
            eq += [sign]
            process_insert(sign)
    else:
        if len(eq) >= 1:
            if not eq[-1].isdigit():
                if eq[-1] == "=":
                    process_insert("clear")
                    process_insert(eq[0] + sign)
                else:
                    process_insert(sign, True)
                eq[-1] = sign
            else:
                eq += [sign]
                process_insert(sign)
    return eq


def count(eq):
    """If the list of "equations" is full, he considers the first two numbers with the corresponding sign of the
    operation between them and rewrites the list, placing the solution as one of the numbers for subsequent operations.
    The sign of the next operation is also saved."""
    ops = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv}
    if eq[1] == "/" and eq[2] == "0":
        print("Division by zero")
        for _ in range(len(eq)):
            eq.pop(0)
        process_insert("clear")
        answer_insert("Division by zero")
    else:
        eq[0] = str(ops[eq[1]](float(eq[0]), float(eq[2])))
        for _ in range(len(eq) - 2):
            eq.pop(1)
        answer_insert(eq)
    return eq


# GUI functions
def process_insert(sign, pop=False):
    if sign == "clear":
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
process_label = tk.Label(root, anchor=tk.E, text="2+2*2", width=26, font=("Arial", 18), bg="gray", fg="gray20")
answer_label = tk.Label(root, anchor=tk.E, text="8", width=26, font=("Arial", 18), bg="gray")

# Labels
content = ["1", "2", "3", "+", "⇦", "4", "5", "6", "-", "C", "7", "8", "9", "*", "CE", "±", "0", ".", "/", "="]
buttons = []
for i in content:
    buttons.append(tk.Button(root, text=i, width=4, font=("Arial", 18), bg="gray", command=add_x(i)))

# PLACE Labels
for i in range(len(buttons)):
    buttons[i].place(x=10 + 76 * (i % 5), y=100 + 55 * (i // 5))

# PLACE Output labels
process_label.place(x=10, y=10)
answer_label.place(x=10, y=50)

init()

root.resizable(False, False)
root.mainloop()

# выглядит страшно
# как минимум гуи стоит выносить в отдельный файл
# а функции в отдельный
