import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg="yellow", width=20, text="empty")
l.pack()
var1 = tk.IntVar()
var2 = tk.IntVar()


def print_selection():
    if var1.get() == 1 and var2.get() == 1:
        l.config(text='love both')
    elif var1.get() == 1 and var2.get() == 0:
        l.config(text='love python')
    elif var1.get() == 0 and var2.get() == 1:
        l.config(text='love c++')
    else:
        l.config(text='love neither')


c1 = tk.Checkbutton(window, text='python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='c++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c2.pack()
window.mainloop()
