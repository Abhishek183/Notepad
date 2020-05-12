from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from tkinter.filedialog import *
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()

def Cut():
    TextArea.event_generate(("<>"))

def Copy():
    TextArea.event_generate(("<>"))

def paste():
    TextArea.event_generate(("<>"))

def about():
    showinfo("Notepad", "Notepad by A๖hiŞhēk ๓iŞhrค")



if __name__ == '__main__':
            root = Tk()


            root.geometry("644x700")
            root.title("untitled  F5-Notepad")

            root.iconbitmap(r'C:\Users\abhishek\Pictures\emoji.jpg')
            root.wm_state("zoomed")

            TextArea = Text(root)
            TextArea.pack(fill=BOTH, expand=1)

            TextArea.config(
                borderwidth=4,
                font=("Arial", 14, "bold", "italic"),
                foreground="blue",
                background="black",
                insertbackground="white", # cursor
                selectforeground="white", # selection
                selectbackground="#006000",
                wrap=WORD, # use word wrapping
                width=64,
                undo=True, # Tk 8.4
                )

            TextArea.focus_set()
            file=None

            menubar=Menu(root)
            filemenu=Menu(menubar,tearoff=0)
            filemenu.add_command(label="New",accelerator="Ctrl+N",command=newfile)
            filemenu.add_command(label="Open",accelerator="Ctrl+O",command=openfile)
            filemenu.add_command(label="Save",accelerator="Ctrl+S",command=savefile)
            filemenu.add_separator()
            filemenu.add_command(label="Exit",command=quitapp )
            menubar.add_cascade(label="File",menu=filemenu)



            editmenu=Menu(menubar,tearoff=0)
            editmenu.add_command(label="Cut", accelerator="Ctrl+X",
                                 command=lambda: TextArea.event_generate('<Control-x>'))  # todo: make it work
            editmenu.add_command(label="Copy", accelerator="Ctrl+C",
                                 command=lambda: TextArea.event_generate('<Control-c>'))  # todo: make it work
            editmenu.add_command(label="Paste", accelerator="Ctrl+V",
                                 command=lambda: TextArea.event_generate('<Control-v>'))
            menubar.add_cascade(label="Edit", menu=editmenu)

            helpmenu=Menu(menubar,tearoff=0)
            helpmenu.add_command(label="About-notepad",command=about)
            menubar.add_cascade(label="About",menu=helpmenu)


            Scroll = Scrollbar(TextArea)
            Scroll.pack(side=RIGHT,  fill=Y)
            Scroll.config(bg="black", activebackground="#314131",command=TextArea.yview)
            TextArea.config(yscrollcommand=Scroll.set)



            root.configure(menu=menubar)



            root.geometry("644x666")




            root.mainloop()



