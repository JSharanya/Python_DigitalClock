from tkinter import *
from time import strftime



window=Tk()
window.geometry("500x200")
window.title("DIGITAL CLOCK")
window.resizable(0,0)
window.config(bg="black")


def Run_Clock():
    Current_time=strftime("%I : %M : %S %p")
    clock_lable.config(text=Current_time)
    clock_lable.after(1000,Run_Clock)

def Run_Date():
    Current_date=strftime("%a %B-%d-%Y")
    date_lable.config(text=Current_date)
    date_lable.after(1000,Run_Date)


clock_lable=Label(window,fg="#3EC70B",bg="black",font=("DS-Digital",60,"bold"))
#clock_lable.place(x=75,y=35)
clock_lable.grid(row=4,column=1,padx=10,pady=25)

date_lable=Label(window,fg="#3AB0FF",bg="black",font=("DS-Digital",20,"bold"))
#date_lable.place(x=75,y=50)
date_lable.grid(row=6,column=1)

Run_Clock()
Run_Date()
window.mainloop()
