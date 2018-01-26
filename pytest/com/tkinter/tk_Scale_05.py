import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg="yellow", width=20, text="empty")
l.pack()


def print_selection(v):
    l.config(text='you have selected ' + v)


# resolution 保留多少小数
# tickinterval 表示显示的间隔数
s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200,
             showvalue=0, tickinterval=3, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
