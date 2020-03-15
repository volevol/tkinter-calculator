from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("362x325")


def do_nothing():
    pass


# Output labels
process_label = Label(root, anchor=E, text="2+2*2", width=24, font=("Arial", 18), bg="gray", fg="gray20")
answer_label = Label(root, anchor=E, text="8", width=24, font=("Arial", 18), bg="gray")

# Number labels
button_1 = Button(root, text="1", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_2 = Button(root, text="2", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_3 = Button(root, text="3", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_4 = Button(root, text="4", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_5 = Button(root, text="5", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_6 = Button(root, text="6", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_7 = Button(root, text="7", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_8 = Button(root, text="8", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_9 = Button(root, text="9", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_0 = Button(root, text="0", width=4, font=("Arial", 18), bg="gray", command=do_nothing)

# Math labels
button_add = Button(root, text="+", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_subtract = Button(root, text="-", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_multiply = Button(root, text="*", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_divide = Button(root, text="/", width=4, font=("Arial", 18), bg="gray", command=do_nothing)

# Special labels
button_c = Button(root, text="C", width=4, font=("Arial", 18), bg="gray", command=do_nothing)
button_equal = Button(root, text="=", width=4, font=("Arial", 18), bg="gray", command=do_nothing)

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
