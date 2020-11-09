import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")
text_box1 = tk.Entry(root, width=20)
text_box2 = tk.Entry(root, width=20)
button_multiple = tk.Button(root, text="+")
label = tk.Label(root, bg='black', fg='white')
text_box1.pack()
text_box2.pack()
button_multiple.pack()
label.pack()


def multiple(event):
    text1 = text_box1.get()
    text2 = text_box2.get()
    label["text"] = int(text1) + int(text2)


def main():
    button_multiple.bind("<Button-1>", multiple)
    root.mainloop()
    print(__name__)

if __name__ == '__main__':
    main()
