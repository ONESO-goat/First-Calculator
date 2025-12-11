import tkinter as tk

calculation = " "

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evauate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    pass

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

b1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial",14))
b1.grid(row=2, column=1)

b2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
b2.grid(row = 2,column = 2 )

b3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
b3.grid(row=2, column=3)

b4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width = 5, font=("Arial", 14))
b4.grid(row = 2, column = 4)

b5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width = 5, font=("Arial", 14))
b5.grid(row=3, column=1)

b6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
b6.grid(row=3, column=2)
b7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width = 5, font = ("Arial", 14))
b7.grid(row = 3, column = 3)

b8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width = 5, font = ("Arial", 14))
b8.grid(row = 3, column = 4)

b9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width = 5, font=("Arial", 14))
b9.grid(row= 4, column = 1)

b10 = tk.Button(root, text="10", command=lambda: add_to_calculation(10), width = 5, font=("Arial", 14))
b10.grid(row = 4, column = 2)


b0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width = 5, font=("Ariel", 14))
b0.grid(row = 4, column = 3)

bplus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width = 5, font = ("Ariel", 14))
bplus.grid(row = 1, column = 5)

bminus = tk.Button(root, text="-", command=lambda: add_to_calculation('-'), width =5, font = ("Ariel", 14))
bminus.grid(row = 2, column = 5)

bmuti = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width = 5, font=("Ariel", 14))
bmuti.grid(row = 3, column = 5)

bdiv = tk.Button(root, text = "/", command=lambda: add_to_calculation("/"), width = 5, font=("Ariel", 14))
bdiv.grid(row = 4, column = 5)

bequal = tk.Button(root, text="=", command=lambda: add_to_calculation("="), width = 5, font=("Ariel", 14))
bequal.grid(row = 5, column = 5)
root.mainloop()





import tkinter
calculation = " "

def add_to_calculations(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.inset(1.0, calculation)

def evauate_calculations():
    global calculation
    try:
        result = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        text_result.insert(1.0, "Error")

