import tkinter

count = 0


def counter():
    global count
    count += 1
    print(count)


root = tkinter.Tk()
root.title("cambio colore")
root.geometry("300x200")

enter_text = tkinter.Entry(root, width=60, bg="black", fg="white")
enter_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn_count = tkinter.Button(root, text="click me", command=counter)

btn_count.grid(row=1, column=1)


def main():
    pass


root.mainloop()

if __name__ == '__main__':
    main()
