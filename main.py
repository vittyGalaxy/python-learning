import tkinter

root = tkinter.Tk()
root.title("La mia calcolatrice")

enter_text = tkinter.Entry(root, width=35, borderwidth=5)
enter_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def click_btn(number):
    enter_text.insert(0, number)


btn_1 = tkinter.Button(root, text="1", padx=40, pady=20, command=lambda: click_btn(1))
btn_2 = tkinter.Button(root, text="2", padx=40, pady=20, command=lambda:click_btn(2))
btn_3 = tkinter.Button(root, text="3", padx=40, pady=20, command=lambda:click_btn(3))
btn_4 = tkinter.Button(root, text="4", padx=40, pady=20, command=lambda:click_btn(4))
btn_5 = tkinter.Button(root, text="5", padx=40, pady=20, command=lambda:click_btn(5))
btn_6 = tkinter.Button(root, text="6", padx=40, pady=20, command=lambda:click_btn(6))
btn_7 = tkinter.Button(root, text="7", padx=40, pady=20, command=lambda:click_btn(7))
btn_8 = tkinter.Button(root, text="8", padx=40, pady=20, command=lambda:click_btn(8))
btn_9 = tkinter.Button(root, text="9", padx=40, pady=20, command=lambda:click_btn(9))
btn_0 = tkinter.Button(root, text="0", padx=40, pady=20, command=lambda:click_btn(0))
btn_sum = tkinter.Button(root, text="+", padx=39, pady=20, command=lambda:click_btn())
btn_equal = tkinter.Button(root, text="=", padx=39, pady=20, command=lambda:click_btn())
btn_cancel = tkinter.Button(root, text="Cancella", padx=199, pady=20, command=lambda:click_btn())

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)

btn_sum.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_cancel.grid(row=5, column=0, columnspan=3)


def main():
    pass


root.mainloop()

if __name__ == '__main__':
    main()
