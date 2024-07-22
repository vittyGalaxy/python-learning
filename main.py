import tkinter

root = tkinter.Tk()
root.title("La mia calcolatrice")

enter_text = tkinter.Entry(root, width=35, borderwidth=5)
enter_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def click_btn(number):
    num_current = enter_text.get()
    enter_text.delete(0, "end")
    enter_text.insert(0, str(num_current) + str(number))


def btn_canc():
    enter_text.delete(0, "end")


def btn_sum():
    first_number = enter_text.get()
    global f_num
    global op_mat
    op_mat = "somma"
    f_num = int(first_number)
    enter_text.delete(0, "end")


def btn_sub():
    first_number = enter_text.get()
    global f_num
    global op_mat
    op_mat = "sottrazione"
    f_num = int(first_number)
    enter_text.delete(0, "end")


def btn_mul():
    first_number = enter_text.get()
    global f_num
    global op_mat
    op_mat = "moltiplicazione"
    f_num = int(first_number)
    enter_text.delete(0, "end")


def btn_div():
    first_number = enter_text.get()
    global f_num
    global op_mat
    op_mat = "divisione"
    f_num = int(first_number)
    enter_text.delete(0, "end")


def btn_equal():
    second_number = enter_text.get()
    enter_text.delete(0, "end")
    if op_mat == "somma":
        enter_text.insert(0, f_num + int(second_number))

    elif op_mat == "sottrazione":
        enter_text.insert(0, f_num - int(second_number))

    elif op_mat == "moltiplicazione":
        enter_text.insert(0, f_num * int(second_number))

    elif op_mat == "divisione":
        enter_text.insert(0, f_num / int(second_number))


btn_1 = tkinter.Button(root, text="1", padx=40, pady=20, command=lambda: click_btn(1))
btn_2 = tkinter.Button(root, text="2", padx=40, pady=20, command=lambda: click_btn(2))
btn_3 = tkinter.Button(root, text="3", padx=40, pady=20, command=lambda: click_btn(3))
btn_4 = tkinter.Button(root, text="4", padx=40, pady=20, command=lambda: click_btn(4))
btn_5 = tkinter.Button(root, text="5", padx=40, pady=20, command=lambda: click_btn(5))
btn_6 = tkinter.Button(root, text="6", padx=40, pady=20, command=lambda: click_btn(6))
btn_7 = tkinter.Button(root, text="7", padx=40, pady=20, command=lambda: click_btn(7))
btn_8 = tkinter.Button(root, text="8", padx=40, pady=20, command=lambda: click_btn(8))
btn_9 = tkinter.Button(root, text="9", padx=40, pady=20, command=lambda: click_btn(9))
btn_0 = tkinter.Button(root, text="0", padx=40, pady=20, command=lambda: click_btn(0))
btn_summ = tkinter.Button(root, text="+", padx=28, pady=20, command=btn_sum)
btn_subb = tkinter.Button(root, text="-", padx=31, pady=20, command=btn_sub)
btn_mull = tkinter.Button(root, text="*", padx=30, pady=20, command=btn_mul)
btn_divv = tkinter.Button(root, text="/", padx=31, pady=20, command=btn_div)
btn_equal = tkinter.Button(root, text="=", padx=39, pady=20, command=btn_equal)
btn_cancel = tkinter.Button(root, text="Canc", padx=28, pady=20, command= btn_canc)

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

btn_summ.grid(row=1, column=4)
btn_subb.grid(row=2, column=4)
btn_mull.grid(row=3, column=4)
btn_divv.grid(row=4, column=4)
btn_equal.grid(row=4, column=2)
btn_cancel.grid(row=4, column=0)


def main():
    pass


root.mainloop()

if __name__ == '__main__':
    main()
