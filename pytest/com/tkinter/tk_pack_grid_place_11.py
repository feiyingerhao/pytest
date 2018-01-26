import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# tk.Label(window, text=1).pack(side='top')
# tk.Label(window, text=2).pack(side='bottom')
# tk.Label(window, text=3).pack(side='left')
# tk.Label(window, text=4).pack(side='right')

# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

# 精准放置位置
tk.Label(window, text=1).place(x=10, y=100, anchor='nw')

window.mainloop()
