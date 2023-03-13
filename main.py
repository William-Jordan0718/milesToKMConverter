from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)


def button_clicked():
    input_miles = input.get()
    kilometer = float(input_miles) * 1.609344
    km_result_label.config(text=f"{kilometer}")


# Entry
input = Entry(width=7)
input.grid(column=1, row=0)

# Miles hard coded
miles_label = Label(text="Miles", font=("Courier", 24, "bold"))
miles_label.grid(column=2, row=0)

# is equal to hard coded
# conversion f string
# KM hard coded
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)

# KM label
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

# Calculate button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)





window.mainloop()
