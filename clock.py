from tkinter import *
import time

def update_time():
    """Updates the time label with the current time in 12-hour format with AM/PM."""
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="white")

clock_label = Label(root, font=("Arial", 58), bg="white", fg="black")
clock_label.pack(pady=40)

update_time()

root.mainloop()
