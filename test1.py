import tkinter as tk
from random import randint
def randomizer():
    canvas.delete("all")
    a = randint(0, 2)
    r = randint(0, 150)
    x = 150
    y = 150
    z = randint(0, 150)
    b = randint(1, 2)
    c = randint(0, 150)
    if a == 0:
        canvas.create_rectangle(r, z, r + c , z + c)
    elif a == 1:
        canvas.create_polygon(randint(0, 300), randint(0, 300), randint(0, 300), randint(0, 300), randint(0, 300), randint(0, 300))
    else:
        canvas.create_oval(x - r, y - r, x + r, y + r)
root=tk.Tk()
root.title("Приложение")
root.geometry("500x500")
button1 =tk.Button(
    root,
    text="создать",
    width=15,
    height=2,
    bg="white",
    command=randomizer)
button1.pack()
canvas = tk.Canvas(root, width = 300, height = 300, bg = "lightblue")
canvas.pack()
root.mainloop()