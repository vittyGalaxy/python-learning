import tkinter


def main():
    root = tkinter.Tk()

    my_label = tkinter.Label(root, text="Ciao sono Vittorio")
    my_label2 = tkinter.Label(root, text="Ti presento GUI")
    my_label3 = tkinter.Label(root, text="-----------")

    my_label.grid(row=0, column=0)
    my_label2.grid(row=1, column=0)
    my_label3.grid(row=1, column=1)

    my_label2.grid(row=1, column=5)
    my_label3.grid(row=1, column=1)

    root.mainloop()


if __name__ == '__main__':
    main()
