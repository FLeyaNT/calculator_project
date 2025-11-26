from tkinter import Tk
import tkinter as tk
from PIL import Image, ImageTk


class MainWindow(Tk):
    
    def __init__(self):
        super().__init__()

        self.entry1 = tk.Label(self)
        self.entry2 = tk.Label(self)

        self.button_perc = tk.Button(self, text="%")
        self.button_CE = tk.Button(self, text="CE")
        self.button_C = tk.Button(self, text="C")
        self.button_del = tk.Button(self, text="⌫")
        self.button_sub = tk.Button(self, text="1/x")
        self.button_pow = tk.Button(self, text="x^2")
        self.button_root = tk.Button(self, text="√")
        self.button_div = tk.Button(self, text="/")
        self.button_7 = tk.Button(self, text="7")
        self.button_8 = tk.Button(self, text="8")
        self.button_9 = tk.Button(self, text="9")
        self.button_mul = tk.Button(self, text="x")
        self.button_4 = tk.Button(self, text="4")
        self.button_5 = tk.Button(self, text="5")
        self.button_6 = tk.Button(self, text="6")
        self.button_min = tk.Button(self, text="-")
        self.button_1 = tk.Button(self, text="1")
        self.button_2 = tk.Button(self, text="2")
        self.button_3 = tk.Button(self, text="3")
        self.button_plus = tk.Button(self, text="+")
        self.button_sign = tk.Button(self, text="+/-")
        self.button_0 = tk.Button(self, text="0")
        self.button_comma = tk.Button(self, text=".")
        self.button_eq = tk.Button(self, text="=")

    def setUp(self) -> None:
        self.geometry("328x415+800+350")
        self.resizable(False, False)
        self.title("Калькулятор")
        self.configure(bg = "#272727")
        image = Image.open("icon/calculator-icon_34473.png")
        photo = ImageTk.PhotoImage(image)
        self.iconphoto(True, photo)
        
        counter = 0
        for entry in self.winfo_children():
            if isinstance(entry, tk.Label):
                entry.config(
                    width = 285,
                    highlightthickness=0,
                    bg="#272727",
                    highlightbackground="#272727",
                    borderwidth=0,
                    anchor="e"
                )
                if counter == 0: 
                    entry.config(fg="#898989", font=("Helvetica", 12),)
                    counter += 1
                else: entry.config(fg="white", font=("Helvetica", 18),)

        self.entry1.pack(padx = 12, pady = (32, 0))       
        self.entry2.pack(padx = 12, pady=(10, 0))

        set_x = 8
        set_y = 120
        counter = 0
        for button in self.winfo_children():
            if isinstance(button, tk.Button):
                button.config(
                    width=5,
                    height=1,
                    font=("Helvetica", 17),
                    fg="white",
                    borderwidth=0,
                    cursor="hand2"
                )
                button.place(x=set_x, y=set_y)
                if counter != 3:
                    set_x += 80
                    counter += 1
                else:
                    set_x = 8
                    set_y += 48
                    counter = 0

                if button.cget("text") in [
                    "%", "CE", "C", "⌫", "1/x", "x^2", "√",
                    "/", "x", "-", "+"
                ]: button.config(bg="#404040")
                elif button.cget("text") == "=": 
                    button.config(bg="#33ccff")
                else: button.config(bg="#5a5a5a")
