from decimal import Decimal, getcontext


class CalculatorLogic:
    
    def __init__(self):
        self.first_dig = True
        self.expression = ""
        self.number = "0"
        getcontext().prec = 50
    
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
                result = self.calculate(self.expression)
                self.number = result
            except:
                self.number = "Ошибка"
            self.expression = f"{self.expression} ="
        self.first_dig = True

    def calculate(self, expression: str) -> str:
        try:
            tokens = expression.split()
            decimal_tokens = []
            
            for token in tokens:
                if token in ['+', '-', '*', '/', '=']:
                    decimal_tokens.append(token)
                else:
                    try:
                        decimal_num = Decimal(token)
                        decimal_tokens.append(f"Decimal('{token}')")
                    except:
                        decimal_tokens.append(token)
            
            decimal_expression = ' '.join(decimal_tokens)
            
            result = eval(decimal_expression, {'Decimal': Decimal})
            
            return self._format_decimal(result)
        except:
            return "Ошибка"
   
    def clearNum(self) -> None: 
        self.number = "0"

    def clearAll(self) -> None:
        self.expression = ""
        self.number = "0"
    
    def getFunction(self, func: str) -> None:
        try:
            num = Decimal(self.number)
            if func == "√": 
                if num < 0:
                    self.number = "Ошибка"
                    return
                result = num.sqrt()
            elif func == "x^2": 
                result = num * num
            elif func == "1/x": 
                if num == 0:
                    self.number = "Ошибка"
                    return
                result = Decimal(1) / num
            
            self.number = self._format_decimal(result)
        except:
            self.number = "Ошибка"
        
    def setPoint(self) -> None:
        if "." not in self.number:
            self.number = self.number + "."
            self.first_dig = False
            
    def getPercent(self) -> None:
        try:
            if len(self.expression) > 0:
                parts = self.expression.strip().split()
                if len(parts) >= 2:
                    action = parts[-1]
                    first_number_str = parts[-2]
                    
                    first_part_result_str = self.calculate(first_number_str)
                    if first_part_result_str == "Ошибка":
                        self.number = "Ошибка"
                        return
                    
                    first_number = Decimal(first_part_result_str)
                    current_number = Decimal(self.number)
                    
                    if action == '*' or action == '/':
                        result = current_number / Decimal(100)
                        self.number = self._format_decimal(result)
                        self.getResult()
                    elif action == '+' or action == '-':
                        percent_value = first_number * (current_number / Decimal(100))
                        self.number = self._format_decimal(percent_value)
                        self.getResult()
                else:
                    self.number = "Ошибка"
            else:
                num = Decimal(self.number)
                result = num / Decimal(100)
                self.number = self._format_decimal(result)
        except:
            self.number = "Ошибка"
    
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

    def _format_decimal(self, value):
        try:
            if isinstance(value, (int, float)):
                decimal_value = Decimal(str(value))
            else:
                decimal_value = value
            
            decimal_value = decimal_value.normalize()
            
            decimal_value = decimal_value.quantize(Decimal('1.0000000000'))
            
            formatted = format(decimal_value, 'f')
            
            if '.' in formatted:
                formatted = formatted.rstrip('0')
                if formatted.endswith('.'):
                    formatted = formatted[:-1]
            
            return formatted
        except:
            return "Ошибка"
