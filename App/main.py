import tkinter as tk
import re


class Buttons:
    def __init__(self, root):
        self.text_box1 = tk.Entry(root, width=20)
        self.text_box2 = tk.Entry(root, width=20)
        self.button_addition = tk.Button(root, text="+")
        self.button_subtraction = tk.Button(root, text="-")
        self.button_multiplication = tk.Button(root, text="*")
        self.button_division = tk.Button(root, text="/")
        self.label = tk.Label(root, width=20, bg='black', fg='white', text="Ответ")
        for button in self.text_box1, self.text_box2, \
                      self.button_addition, self.button_subtraction, \
                      self.button_multiplication, self.button_division, self.label:
            button.pack()


class Actions(Buttons):
    def __init__(self, root):
        super().__init__(root)
        self.button_addition["command"] = self.addition
        self.button_subtraction["command"] = self.subtraction
        self.button_multiplication["command"] = self.multiplication
        self.button_division["command"] = self.division

    def addition(self):
        first_number: str = self.text_box1.get()
        second_number: str = self.text_box2.get()
        if re.sub("[.,]", "", first_number).isdigit() and re.sub("[.,]", "", second_number).isdigit():
            answer = float(first_number.replace(",", ".", 1)) + float(second_number.replace(",", ".", 1))
            self.label["text"] = "%g" % answer
        else:
            self.label["text"] = "Введите числа"

    def subtraction(self):
        first_number: str = self.text_box1.get()
        second_number: str = self.text_box2.get()
        if re.sub("[.,]", "", first_number).isdigit() and re.sub("[.,]", "", second_number).isdigit():
            answer = float(first_number.replace(",", ".", 1)) - float(second_number.replace(",", ".", 1))
            self.label["text"] = "%g" % answer
        else:
            self.label["text"] = "Введите числа"

    def multiplication(self):
        first_number: str = self.text_box1.get()
        second_number: str = self.text_box2.get()
        if re.sub("[.,]", "", first_number).isdigit() and re.sub("[.,]", "", second_number).isdigit():
            answer = float(first_number.replace(",", ".", 1)) * float(second_number.replace(",", ".", 1))
            self.label["text"] = "%g" % answer
        else:
            self.label["text"] = "Введите числа"

    def division(self):
        first_number: str = self.text_box1.get()
        second_number: str = self.text_box2.get()
        if re.sub("[.,]", "", first_number).isdigit() and re.sub("[.,]", "", second_number).isdigit():
            answer = float(first_number.replace(",", ".", 1)) / float(second_number.replace(",", ".", 1))
            self.label["text"] = "%g" % answer
        else:
            self.label["text"] = "Введите числа"


def main():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x200")
    action = Actions(root)
    root.mainloop()


if __name__ == '__main__':
    main()
