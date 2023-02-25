import tkinter as tk

root=tk.Tk()
root.title("Приложение")
root.geometry("500x500")

def change():
    a = str(entry1.get())
    b = "Приветствуем, " + a
    label.config(text = b)      
text = tk.Text()
text.pack()

entry1 = tk.Entry(text = "Введите Ваше имя")
entry1.pack()

button1 =tk.Button(
    root,
    text="Поприветствовать",
    width=15,
    height=2,
    bg="white",
    command= change)
button1.pack()

label = tk.Label(root,
    text="",
    width=50,
    height=2,
    bg="white")
label.pack()

root.mainloop()