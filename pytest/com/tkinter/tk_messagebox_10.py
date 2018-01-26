import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def hit_me():
    # tk.messagebox.showinfo(title='Hi', message='haha')
    # tk.messagebox.showwarning(title='warn', message='warn')
    # tk.messagebox.showerror(title='error', message='error')
    print(tk.messagebox.askquestion(title='error', message='error'))



tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()
