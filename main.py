from tkinter import *

root = Tk()
root.configure(bg="black")
root.geometry('1440x720')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red',  # change to black later
    width=1440,
    height=180
)
top_frame.place(x=0, y=0)

root.mainloop()