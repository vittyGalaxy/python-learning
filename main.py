import tkinter


def button_welcome():
    print("Benvenuto!!!")


root = tkinter.Tk()
root.title("Benvenuto!")
root.geometry("300x200")

enter_text = tkinter.Entry(root, width=60, bg="black", fg="white")
enter_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn_welcome = tkinter.Button(root, text="save", padx=40, pady=29, command=button_welcome)

btn_welcome.grid(row=1, column=1)


def main():
    pass


root.mainloop()

if __name__ == '__main__':
    main()
