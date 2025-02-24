# Program Name: Assignment3.py
# Course: IT3883/Section 17540
# Student Name: Kalyb Sanders
# Assignment Number: 3
# Due Date: 02/ 23/ 2025
# Purpose: GUI interface that allows the conversion from
#           miles per gallon to kilometers per liter (mpg to kpl).
#
# List Specific resources used to complete the assignment.
#   I used the reading provided in the class
#   as well as the tkinter documentation.

from tkinter import*

# 'key_pressed' Callback Function (bound to key press event on Text)
def key_pressed(event):
    # after 1ms of event, call update_result function
    main_window.after(1, update_result)

# 'update_result' Function called after every 'key_pressed' event
def update_result():
    # get text from Text field as string
    text_in = mpg_value.get("1.0", "end")

    # if text field empty, set to no result text
    if text_in.replace(" ", "").replace("\n", "") == "":
        kpl_result.config(text="")
        return

    # try catch input
    # unit conversion and output should update
    # except in case of non-number inputs (i.e. letters)
    try:
        num = float(text_in)
        if num < 0:
            kpl_result.config(text="Please enter a positive number!")
            return

        converted_num = round(mpg_to_kpl(num), 4)
        text_out = "= " + str(converted_num) + " kpl"
        kpl_result.config(text=text_out)
    except ValueError:
        kpl_result.config(text="Please enter a valid number value!")

# Function converts Miles per Gallon ---> Kilometers per Liter
def mpg_to_kpl(mpg):
    return mpg * 0.425143707


# window and size
main_window = Tk()
main_window.geometry("400x100")
main_window.title("MPG to KPL unit conversion!")

# label for text field
mpg_label = Label(text="mpg")

# create text field and bind key event
mpg_value = Text(main_window, width=20, height=1)
mpg_value.bind("<Key>", key_pressed)

# result label (read-only)
kpl_result = Label(main_window)

# button to quit program
quit_button = Button(main_window, text="Quit", command=main_window.destroy)

mpg_label.pack()
mpg_value.pack()
kpl_result.pack()
quit_button.pack()

main_window.mainloop()