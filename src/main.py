from src.mainwindow import MainWindow
import tkinter as tk
import math

class Calculator(MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setUp()
        self.first_dig = True
        self.expression = tk.StringVar()
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
        self.button_min.config(command=lambda: self.setActionSign("-"))
        self.button_plus.config(command=lambda: self.setActionSign("+"))
        self.button_div.config(command=lambda: self.setActionSign("/"))
        self.button_mul.config(command=lambda: self.setActionSign("*"))
        self.button_root.config(command=lambda: self.getFunction("√"))
        self.button_pow.config(command=lambda: self.getFunction("x^2"))
        self.button_sub.config(command=lambda: self.getFunction("1/x"))
        self.button_C.config(command=self.clearNum)
        self.button_CE.config(command=self.clearAll)
        self.button_eq.config(command=self.getResult)
        self.button_del.config(command=self.delDigit)
        self.button_sign.config(command=self.setNegative)
        self.button_comma.config(command=self.setPoint)
        self.button_perc.config(command=self.getPercent)

    def setNum(self, num: chr) -> None:
        if (self.number.get() == "0") or (self.first_dig == True):
            self.number.set(num)
        else:
            self.number.set(self.number.get() + num)
        self.first_dig = False
    
    def setActionSign(self, sign: chr) -> None:
        if "=" in self.expression.get():
            self.expression.set("")
        self.expression.set(f"{self.expression.get()} {self.number.get()} {sign}")
        self.first_dig = True

    def getResult(self) -> None:
        if ("=" not in self.expression.get()):
            self.expression.set(f"{self.expression.get()} {self.number.get()}")
            try:
                self.number.set(str(eval(self.expression.get())))
            except:
                self.number.set("Ошибка")
            self.expression.set(f"{self.expression.get()} =")
        self.first_dig = True
   
    def clearNum(self) -> None: self.number.set("0")

    def clearAll(self) -> None:
        self.expression.set("")
        self.number.set("0")
    
    def getFunction(self, func: str) -> None:
        if func == "√": result = math.sqrt(float(self.number.get()))
        elif func == "x^2": result = math.pow(float(self.number.get()), 2)
        elif func == "1/x": result = 1 / float(self.number.get())
        self.number.set(str(result)) 
        
    def setPoint(self) -> None:
        if "." not in self.number.get():
            self.number.set(self.number.get() + ".")
            self.first_dig = False
            
    def getPercent(self) -> None:
        if len(self.expression.get()) > 0:
            action = self.expression.get()[-1]
            string = self.expression.get()[0:len(self.expression.get())-1]
            self.expression.set(f"{str(eval(string))} {action}")
            if action == '*' or action == '/':
                self.number.set(str(float(self.number.get()) / 100))
            elif action == '+' or action == '-':
                num1 = float(self.expression.get()[0:len(self.expression.get())-2])
                num2 = float(self.number.get())
                self.number.set(str(num1 * ((num2) / 100)))
            self.getResult()
        else:
            num1 = float(self.number.get())
            self.number.set(str(num1 / 100))
    
    def delDigit(self) -> None:
        if (len(self.number.get()) < 2 or ("-" in self.number.get() and len(self.number.get()) == 2)):
            self.number.set("0")
        else: self.number.set(self.number.get()[0:len(self.number.get())-1])

    def setNegative(self) -> None:
        if ("-" not in self.number.get()): self.number.set(f"-{self.number.get()}")
        else: self.number.set(self.number.get()[1:len(self.number.get())])

    def delDigit(self) -> None:
        if (len(self.number.get()) < 2 or ("-" in self.number.get() and len(self.number.get()) == 2)):
            self.number.set("0")
        else: self.number.set(self.number.get()[0:len(self.number.get())-1])

    def setNegative(self) -> None:
        if ("-" not in self.number.get()): self.number.set(f"-{self.number.get()}")
        else: self.number.set(self.number.get()[1:len(self.number.get())])

    def setPoint(self) -> None:
        if "." not in self.number.get():
            self.number.set(self.number.get() + ".")
            self.first_dig = False

    def getPercent(self) -> None:
        if len(self.expression.get()) > 0:
            action = self.expression.get()[-1]
            string = self.expression.get()[0:len(self.expression.get())-1]
            self.expression.set(f"{str(eval(string))} {action}")
            if action == '*' or action == '/':
                self.number.set(str(float(self.number.get()) / 100))
            elif action == '+' or action == '-':
                num1 = float(self.expression.get()[0:len(self.expression.get())-2])
                num2 = float(self.number.get())
                self.number.set(str(num1 * ((num2) / 100)))
            self.getResult()
        else:
            num1 = float(self.number.get())
            self.number.set(str(num1 / 100))

if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()
