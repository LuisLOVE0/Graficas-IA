import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def plot_function():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        x = np.linspace(0, 10, 100)
        y = a * x + b
        
        plt.plot(x, y,"b-")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid()
        plt.legend()
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

root = tk.Tk()
root.title("Grafico de linea recta")

tk.Label(root, text="ax + b    (a):").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="ax + b    (b):").pack()
entry_b = tk.Entry(root)
entry_b.pack()

btn_plot = tk.Button(root, text="Gráfico", command=plot_function)
btn_plot.pack()

root.mainloop()
