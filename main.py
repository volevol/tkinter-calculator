from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("362x325")

# Data
equation = []


# Functions

# Main functions
def add(eq, sign):
    print(sign, end=" ")
    eq += [sign]
    print(eq)
    if len(eq) > 3:
        count(eq)
        print(eq)


def count(eq):
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
    return eq


# Number functions
def add_1():
    add(equation, "1")


def add_2():
    add(equation, "2")


def add_3():
    add(equation, "3")


def add_4():
    add(equation, "4")


def add_5():
    add(equation, "5")


def add_6():
    add(equation, "6")


def add_7():
    add(equation, "7")


def add_8():
    add(equation, "8")


def add_9():
    add(equation, "9")


def add_0():
    add(equation, "0")


# Math functions
def plus():
    add(equation, "+")


def minus():
    add(equation, "-")


def multiply():
    add(equation, "*")


def divide():
    add(equation, "/")


# Special functions
def c():
    pass


def equal():
    pass


# Output labels
process_label = Label(root, anchor=E, text="2+2*2", width=24, font=("Arial", 18), bg="gray", fg="gray20")
answer_label = Label(root, anchor=E, text="8", width=24, font=("Arial", 18), bg="gray")

# Number labels
button_1 = Button(root, text="1", width=4, font=("Arial", 18), bg="gray", command=add_1)
button_2 = Button(root, text="2", width=4, font=("Arial", 18), bg="gray", command=add_2)
button_3 = Button(root, text="3", width=4, font=("Arial", 18), bg="gray", command=add_3)
button_4 = Button(root, text="4", width=4, font=("Arial", 18), bg="gray", command=add_4)
button_5 = Button(root, text="5", width=4, font=("Arial", 18), bg="gray", command=add_5)
button_6 = Button(root, text="6", width=4, font=("Arial", 18), bg="gray", command=add_6)
button_7 = Button(root, text="7", width=4, font=("Arial", 18), bg="gray", command=add_7)
button_8 = Button(root, text="8", width=4, font=("Arial", 18), bg="gray", command=add_8)
button_9 = Button(root, text="9", width=4, font=("Arial", 18), bg="gray", command=add_9)
button_0 = Button(root, text="0", width=4, font=("Arial", 18), bg="gray", command=add_0)

# Math labels
button_add = Button(root, text="+", width=4, font=("Arial", 18), bg="gray", command=plus)
button_subtract = Button(root, text="-", width=4, font=("Arial", 18), bg="gray", command=minus)
button_multiply = Button(root, text="*", width=4, font=("Arial", 18), bg="gray", command=multiply)
button_divide = Button(root, text="/", width=4, font=("Arial", 18), bg="gray", command=divide)

# Special labels
button_c = Button(root, text="C", width=4, font=("Arial", 18), bg="gray", command=c)
button_equal = Button(root, text="=", width=4, font=("Arial", 18), bg="gray", command=equal)

# PLACE Output labels
process_label.place(x=10, y=10)
answer_label.place(x=10, y=50)

# PLACE Number labels
button_1.place(x=10, y=100)
button_2.place(x=102, y=100)
button_3.place(x=194, y=100)
button_4.place(x=10, y=155)
button_5.place(x=102, y=155)
button_6.place(x=194, y=155)
button_7.place(x=10, y=210)
button_8.place(x=102, y=210)
button_9.place(x=194, y=210)
button_0.place(x=100, y=265)

# PLACE Math labels
button_add.place(x=286, y=100)
button_subtract.place(x=286, y=155)
button_multiply.place(x=286, y=210)
button_divide.place(x=286, y=265)

# PLACE Special labels
button_c.place(x=10, y=265)
button_equal.place(x=194, y=265)

root.mainloop()
