import tkinter

root = tkinter.Tk()


enter_text = tkinter.Entry(root, width=60, bg="black", fg="white")
enter_text.pack()


def click_here():
    welcome = "Ciao " + enter_text.get()
    write = tkinter.Label(root, text=welcome)
    write.pack()


def main():

   my_button = tkinter.Button(root, text="Inserisci il tuo nome", command=click_here, padx=30)
   my_button.pack()

   root.mainloop()


if __name__ == '__main__':
    main()
