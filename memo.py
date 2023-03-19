import os
from tkinter import *

root = Tk()
root.title("My memo")
root.geometry("640x480+300+100")

menu = Menu(root)

filename = "mynote.txt"

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0",END))

def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0",END)
            txt.insert(END, file.read())


file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="File",menu=file_menu)

edit_menu = Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu=edit_menu)

object_menu = Menu(menu,tearoff=0)
menu.add_cascade(label="Object",menu=object_menu)

view_menu = Menu(menu,tearoff=0)
menu.add_cascade(label="View",menu=view_menu)

help_menu = Menu(menu,tearoff=0)
menu.add_cascade(label="Help",menu=help_menu)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both",expand=True)

scrollbar.config(command=txt.yview)


root.config(menu=menu)

root.mainloop()