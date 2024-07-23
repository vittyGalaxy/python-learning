import tkinter

root = tkinter.Tk()
root.title("Salva nomi")

enter_text = tkinter.Entry(root, width=60, bg="black", fg="white")
enter_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

save = []


def btn_save():
    t = enter_text.get()
    save.append(t)
    f = open("file.txt", "w")
    f.write(t)
    f.close()
    s = "salvato il nome " + t
    write = tkinter.Label(root, text=s)


def btn_load():
    load = []
    f = open("file.txt", "r")
    for l in f:
        load.append(l)
    f.close()

    print(load)


btn_s = tkinter.Button(root, text="save", padx=39, pady=20, command=btn_save)
btn_l = tkinter.Button(root, text="load", padx=39, pady=20, command=btn_load)


btn_s.grid(row=1, column=0)
btn_l.grid(row=1, column=1)


def main():
    pass


root.mainloop()

if __name__ == '__main__':
    main()
