import tkinter as tk

window = tk.Tk()
window.title="hello"
window.geometr="200x200"

var = tk.StringVar()
label = tk.Label(window, textvariable=var, font=("Arial", 12), background="blue", width=15, height=2)
label.pack()
Flag = True

def change():
    global Flag
    if Flag == True:
        var.set("aaa")
        Flag = False
    else:
        var.set("bbb")
        Flag = True


button = tk.Button(window, text="hit me", command=change, width=15, height=2)
button.pack()

window.mainloop()
