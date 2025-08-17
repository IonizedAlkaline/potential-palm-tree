from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Virus Detection")
window.geometry('500x500')
def checking():
    messagebox.showwarning("Alert","Virus Detected")
button=Button(text="Download",command=checking)
button.pack()
window.mainloop()