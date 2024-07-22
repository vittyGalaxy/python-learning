import tkinter

root = tkinter.Tk()
root.title("La mia calcolatrice")

enter_text = tkinter.Entry(root, width=35, borderwidth=5)
enter_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def aggBtn():
    return


btn_1 = tkinter.Button(root, text="1", padx=40, pady=20, command=aggBtn)
btn_2 = tkinter.Button(root, text="2", padx=40, pady=20, command=aggBtn)
btn_3 = tkinter.Button(root, text="3", padx=40, pady=20, command=aggBtn)
btn_4 = tkinter.Button(root, text="4", padx=40, pady=20, command=aggBtn)
btn_5 = tkinter.Button(root, text="5", padx=40, pady=20, command=aggBtn)
btn_6 = tkinter.Button(root, text="6", padx=40, pady=20, command=aggBtn)
btn_7 = tkinter.Button(root, text="7", padx=40, pady=20, command=aggBtn)
btn_8 = tkinter.Button(root, text="8", padx=40, pady=20, command=aggBtn)
btn_9 = tkinter.Button(root, text="9", padx=40, pady=20, command=aggBtn)
btn_0 = tkinter.Button(root, text="0", padx=40, pady=20, command=aggBtn)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=1)
def main():
    pass


root.mainloop()

if __name__ == '__main__':
    main()
