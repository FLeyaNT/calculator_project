from mainwindow import MainWindow


class Calculator(MainWindow):
    def __init__(self):
        super().__init__()
        self.setUp()


if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()
