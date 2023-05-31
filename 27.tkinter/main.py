from tkinter import *


def miles_to_km():
    miles = float(my_input.get())
    km = round(miles * 1.609, 2)
    result_label.config(text=f"{km}")
    
# window
window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

my_input = Entry(width=10)
# my_input.insert(END, string="0")
my_input.grid(row=0, column=1)
my_input.focus()

miles_label = Label(text="Miles", font=("Arial", 18, "normal"))
miles_label.grid(row=0, column=2)
miles_label.config(padx=10)

is_equal_label = Label(text="is equal to", font=("Arial", 14, "normal"))
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0", font=("Arial", 18, "normal"))
result_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 18, "normal"))
km_label.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)






    





















mainloop()