import math


class CalculatorLogic:
    
    def __init__(self):
        self.first_dig = True
        self.expression = ""
        self.number = "0"
    
    def setNum(self, num: str) -> None:
        if (self.number == "0") or (self.first_dig == True):
            self.number = num
        else:
            self.number = self.number + num
        self.first_dig = False
    
    def setActionSign(self, sign: str) -> None:
        if "=" in self.expression:
            self.expression = ""
        self.expression = f"{self.expression} {self.number} {sign}"
        self.first_dig = True

    def getResult(self) -> None:
        if ("=" not in self.expression):
            self.expression = f"{self.expression} {self.number}"
            try:
                self.number = str(self.calculate(self.expression))
            except:
                self.number = "Ошибка"
            self.expression = f"{self.expression} ="
        self.first_dig = True

    def calculate(self, expression: str) -> str:
        return eval(expression)
   
    def clearNum(self) -> None: 
        self.number = "0"

    def clearAll(self) -> None:
        self.expression = ""
        self.number = "0"
    
    def getFunction(self, func: str) -> None:
        if func == "√": 
            result = math.sqrt(float(self.number))
        elif func == "x^2": 
            result = math.pow(float(self.number), 2)
        elif func == "1/x": 
            result = 1 / float(self.number)
        self.number = str(result)
        
    def setPoint(self) -> None:
        if "." not in self.number:
            self.number = self.number + "."
            self.first_dig = False
            
    def getPercent(self) -> None:
        if len(self.expression) > 0:
            action = self.expression[-1]
            string = self.expression[0:len(self.expression)-1]
            self.expression = f"{str(eval(string))} {action}"
            if action == '*' or action == '/':
                self.number = str(float(self.number) / 100)
            elif action == '+' or action == '-':
                num1 = float(self.expression[0:len(self.expression)-2])
                num2 = float(self.number)
                self.number = str(num1 * (num2 / 100))
            self.getResult()
        else:
            num1 = float(self.number)
            self.number = str(num1 / 100)
    
    def delDigit(self) -> None:
        if (len(self.number) < 2 or ("-" in self.number and len(self.number) == 2)):
            self.number = "0"
        else: 
            self.number = self.number[0:len(self.number)-1]

    def setNegative(self) -> None:
        if ("-" not in self.number): 
            self.number = f"-{self.number}"
        else: 
            self.number = self.number[1:len(self.number)]
    
    def get_expression(self) -> str:
        return self.expression
    
    def get_number(self) -> str:
        return self.number
    
    def set_expression(self, expression: str) -> None:
        self.expression = expression
    
    def set_number(self, number: str) -> None:
        self.number = number
