from .mainwindow import MainWindow
import tkinter as tk
from .logic import CalculatorLogic


class Calculator(MainWindow):
    
    def __init__(self, testing_mode=False):
        super().__init__()
        if not testing_mode:
            self.setUp()
        
        self.logic = CalculatorLogic()
        
        self.expression_var = tk.StringVar()
        self.number_var = tk.StringVar()
        self.number_var.set("0")
        
        self.entry1.config(textvariable=self.expression_var)
        self.entry2.config(textvariable=self.number_var)
        
        self.bind_buttons()
        
        self.update_display()

    def bind_buttons(self):
        self.button_0.config(command=lambda: self.on_number_click("0"))
        self.button_1.config(command=lambda: self.on_number_click("1"))
        self.button_2.config(command=lambda: self.on_number_click("2"))
        self.button_3.config(command=lambda: self.on_number_click("3"))
        self.button_4.config(command=lambda: self.on_number_click("4"))
        self.button_5.config(command=lambda: self.on_number_click("5"))
        self.button_6.config(command=lambda: self.on_number_click("6"))
        self.button_7.config(command=lambda: self.on_number_click("7"))
        self.button_8.config(command=lambda: self.on_number_click("8"))
        self.button_9.config(command=lambda: self.on_number_click("9"))
        
        self.button_min.config(command=lambda: self.on_operation_click("-"))
        self.button_plus.config(command=lambda: self.on_operation_click("+"))
        self.button_div.config(command=lambda: self.on_operation_click("/"))
        self.button_mul.config(command=lambda: self.on_operation_click("*"))
        
        self.button_root.config(command=lambda: self.on_function_click("√"))
        self.button_pow.config(command=lambda: self.on_function_click("x^2"))
        self.button_sub.config(command=lambda: self.on_function_click("1/x"))
        self.button_C.config(command=self.on_clear_num_click)
        self.button_CE.config(command=self.on_clear_all_click)
        self.button_eq.config(command=self.on_equals_click)
        self.button_del.config(command=self.on_delete_click)
        self.button_sign.config(command=self.on_sign_click)
        self.button_comma.config(command=self.on_point_click)
        self.button_perc.config(command=self.on_percent_click)

    def update_display(self):
        self.expression_var.set(self.logic.get_expression())
        self.number_var.set(self.logic.get_number())

    def on_number_click(self, num: str):
        self.logic.setNum(num)
        self.update_display()
    
    def on_operation_click(self, sign: str):
        self.logic.setActionSign(sign)
        self.update_display()

    def on_equals_click(self):
        self.logic.getResult()
        self.update_display()

    def on_clear_num_click(self):
        self.logic.clearNum()
        self.update_display()

    def on_clear_all_click(self):
        self.logic.clearAll()
        self.update_display()
    
    def on_function_click(self, func: str):
        self.logic.getFunction(func)
        self.update_display()
        
    def on_point_click(self):
        self.logic.setPoint()
        self.update_display()
            
    def on_percent_click(self):
        self.logic.getPercent()
        self.update_display()
    
    def on_delete_click(self):
        self.logic.delDigit()
        self.update_display()

    def on_sign_click(self):
        self.logic.setNegative()
        self.update_display()


if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()
