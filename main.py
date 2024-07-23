import tkinter

not_domestic_animal = []
domestic_animal = []


def button_save():
    t = enter_text.get()
    if (t == "cat") or (t == "dog") or (t == "rabbit") or (t == "hamster") or (t == "turtle"):
        domestic_animal.append(t)

    else:
        not_domestic_animal.append(t)

    f = open("file_copia.txt", "w")
    f.write(str(domestic_animal))
    f.close()

    f = open("file.txt", "w")
    f.write(str(not_domestic_animal))
    f.close()


def button_load():
    load_domestic = []
    load_not_domestic = []
    print("Gli animali domestici sono: ")
    f = open("file_copia.txt", "r")
    for l in f:
        load_domestic.append(l)
    f.close()

    f = open("file.txt", "r")
    for l in f:
        load_not_domestic.append(l)
    f.close()
    print(load_domestic)
    print("Gli animali non domestici: ")
    print(load_not_domestic)


root = tkinter.Tk()
root.title("Riconoscimento")
root.geometry("300x200")

enter_text = tkinter.Entry(root, width=60, bg="black", fg="white")
enter_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn_save = tkinter.Button(root, text="save", command=button_save)
btn_load = tkinter.Button(root, text="load", command=button_load)

btn_save.grid(row=1, column=1)
btn_load.grid(row=1, column=2)


def main():
    pass


root.mainloop()

if __name__ == '__main__':
    main()
