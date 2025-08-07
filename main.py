'''This is a simple NotePad modeb created by Abhay14-python with the teaching of Clear Code'''

import tkinter as tk
from tkinter import ttk

def button_func():
    print("A button was pressed")

# def hello():
#     print("Hello")

# create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x550")

# ttk label
label = ttk.Label(master = window , text = "This is a NotePad") 
label.pack()

# tk text
text =tk.Text(master = window)
text.pack()

# entry
entry = ttk.Entry(master = window)
entry.pack()

# exercise text label
text_label = tk.Label(master = window , text = "My Label")
text_label.pack()

#  exercise hello button
# button1 = ttk.Button(master = window , text = "Hello?" , command = hello)
button1 = ttk.Button(master = window , text = "Hello?" , command = lambda:print("Hello Bro"))
button1.pack()
# ttk button
button = ttk.Button(master = window , text = "A Button" , command = button_func)
button.pack()

# run 
window.mainloop()

print("Thnaks for your support !")
