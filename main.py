import tkinter

root = tkinter.Tk()


def click_here():
    write = tkinter.Label(root, text="Pulsante premuto!")
    write.pack()


def main():

   my_button = tkinter.Button(root, text="Clicca qui!", command=click_here, padx=30)
   my_button.pack()

   root.mainloop()


if __name__ == '__main__':
    main()
