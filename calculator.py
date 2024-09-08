import tkinter
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

#pantalla de la calculadora
labe_result = Label(root, width=25, height=2, text="", font=("arial", 30))
labe_result.pack()

#Fila 1
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=430, y=100)

#Fila 2
Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36").place(x=430, y=200)



root.mainloop()