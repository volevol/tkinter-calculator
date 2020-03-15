from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("362x325")


# Functions

# Main function
def add(sign):
    print(sign, end=" ")


# Number functions
def add_1():
    add("1")


def add_2():
    add("2")


def add_3():
    add("3")


def add_4():
    add("4")


def add_5():
    add("5")


def add_6():
    add("6")


def add_7():
    add("7")


def add_8():
    add("8")


def add_9():
    add("9")


def add_0():
    add("0")


# Math functions
def plus():
    add("+")


def minus():
    add("-")


def multiply():
    add("*")


def divide():
    add("/")


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
