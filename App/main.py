import tkinter as tk
import re


class Buttons:
    def __init__(self, root):
        self.text_box1 = tk.Entry(root, width=20, font=("System", 20))
        self.text_box1.insert(0, "Введите число 1")
        self.text_box2 = tk.Entry(root, width=20, font=("System", 20))
        self.text_box2.insert(0, "Введите число 2")
        self.button_addition = tk.Button(root, text="+", font=("System", 20))
        self.button_subtraction = tk.Button(root, text="-", font=("System", 20))
        self.button_multiplication = tk.Button(root, text="*", font=("System", 20))
        self.button_division = tk.Button(root, text="/", font=("System", 20))
        self.label = tk.Label(root, width=20, fg='black', text="Ответ", relief="ridge", font=("System", 20)) # flat, groove, raised, ridge, solid, or sunken
        for button in self.text_box1, self.text_box2, \
                      self.button_addition, self.button_subtraction, \
                      self.button_multiplication, self.button_division, self.label:
            button.pack()
        self.text_box1.bind("<Button-1>", self.on_click_text_box1)
        self.text_box2.bind("<Button-1>", self.on_click_text_box2)

    def on_click_text_box1(self, event):
        self.text_box1.delete(0, tk.END)

    def on_click_text_box2(self, event):
        self.text_box2.delete(0, tk.END)


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
    root.geometry("300x250")
    action = Actions(root)
    root.mainloop()


if __name__ == '__main__':
    main()
