from tkinter import *
from tkinter import messagebox



def get_height():
     height = float(ENTRY2.get())
     return height

def get_weight():
    weight = float(ENTRY1.get())
    return weight

def calculate_bmı():
    BMI = get_weight() / (get_height()/100)**2
    if BMI <= 18.4:
        print("You are underweight.")
    elif BMI <= 24.9:
        print("You are healthy.")
    elif BMI <= 29.9:
        print("You are over weight.")
    elif BMI <= 34.9:
        print("You are severely over weight.")
    elif BMI <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")
if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmı)
    TOP.geometry("400x400")
    TOP.configure(background="Gray")
    TOP.title("BMI Calculator")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="yellow", text="Welcome to BMI Calculator", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, bg="pink", text="Enter Weight (in kg):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="blue", text="Enter Height (in cm):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=121)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=121)
    BUTTON = Button(bg="green", bd=12, text="BMI", padx=33, pady=15, command=calculate_bmı,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    TOP.mainloop()