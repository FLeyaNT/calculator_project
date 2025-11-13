from mainwindow import MainWindow
import tkinter as tk


class Calculator(MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setUp()
        self.first_dig = True
        self.number = tk.StringVar()
        self.number.set("0")
        self.entry1.config(textvariable=self.expression)
        self.entry2.config(textvariable=self.number)
        self.button_0.config(command=lambda: self.setNum("0"))
        self.button_1.config(command=lambda: self.setNum("1"))
        self.button_2.config(command=lambda: self.setNum("2"))
        self.button_3.config(command=lambda: self.setNum("3"))
        self.button_4.config(command=lambda: self.setNum("4"))
        self.button_5.config(command=lambda: self.setNum("5"))
        self.button_6.config(command=lambda: self.setNum("6"))
        self.button_7.config(command=lambda: self.setNum("7"))
        self.button_8.config(command=lambda: self.setNum("8"))
        self.button_9.config(command=lambda: self.setNum("9"))
        self.button_del.config(command=self.delDigit)

    def setNum(self, num: chr) -> None:
        if (self.number.get() == "0") or (self.first_dig == True):
            self.number.set(num)
        else:
            self.number.set(self.number.get() + num)
        self.first_dig = False

    def delDigit(self) -> None:
        if (len(self.number.get()) < 2 or ("-" in self.number.get() and len(self.number.get()) == 2)):
            self.number.set("0")
        else: self.number.set(self.number.get()[0:len(self.number.get())-1])

if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()
