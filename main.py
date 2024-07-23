import tkinter
import random


def change_color():
    colors = ["red", "green", "yellow", "purple", "orange"]
    root.config(bg=random.choice(colors))


root = tkinter.Tk()
root.title("cambio colore")
root.geometry("300x200")

enter_text = tkinter.Entry(root, width=60, bg="black", fg="white")
enter_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn_color = tkinter.Button(root, text="change color", command=change_color)

btn_color.grid(row=1, column=1)


def main():
    pass


root.mainloop()

if __name__ == '__main__':
    main()
