from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry('500x500')
def handling(event):
    print(event.char)
window.bind("<Key>",handling)
button = Button(text="click me")
button.pack()
def click(event):
    print("Button Clicked")
button.bind("<Button-1>",click)
window.mainloop()