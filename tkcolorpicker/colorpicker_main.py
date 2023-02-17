
import tkinter as tk
from tkcolorpicker.functions import tk, ttk
from tkcolorpicker import askcolor


def select_color1():
    print(askcolor(color="sky blue", parent=root))
    return color

def select_color2():
    print(askcolor(color=(255, 120, 0, 100), parent=root, alpha=True))
    return color


root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')
ttk.Label(root, text='Color Selection:').pack(padx=4, pady=4)
ttk.Button(root, text='solid color',
           command=select_color1).pack(fill='x', padx=4, pady=4)
ttk.Button(root, text='with alpha channel',
           command=select_color2).pack(fill='x', padx=4, pady=4)
root.mainloop()

