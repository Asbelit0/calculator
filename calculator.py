import tkinter
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#ced3d9")

equation = ""

def show(value):
    global equation
    equation += value
    labe_result.config(text=equation)

def clear():
    global equation
    equation = ""
    labe_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
    labe_result.config(text=result)

#pantalla de la calculadora
labe_result = Label(root, width=25, height=2, text="", font=("arial", 30))
labe_result.pack()

#Fila 1
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#ff8ac8", command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=430, y=100)

#Fila 2
Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=200)

#Fila 3
Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=300)

#Fila 4
Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=400)

Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=500)

#Fila 5
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=500)
Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=430, y=400)

root.mainloop()