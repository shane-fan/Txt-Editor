from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox
from colored import fg, bg, attr
color = fg("white") + bg("black")

filename = None

def openFile(): #Opens existing file
    file_ = filedialog.askopenfile(mode='r')
    data = file_.read()
    text.delete(0.0, END)
    text.insert(0.0, data)

def newFile(): #Opens new file
    global filename
    filename = "untitled"
    text.delete(0.0, END)

def saveFile(): #Stores text from textbox
    global filename
    data = text.get(0.0, END)
    file_ = open(filename, 'w')
    file_.write(data)
    file_.close()

def saveAs(): #Save new
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get(0.0, END)
    try:
        f.write(data.rstrip()) #cutoff whitespace
    except:
        messagebox.showerror(title='Error', message='Cannot save file') #shouldn't have error, but here if there is

def about():
    messagebox.showinfo("About", "A convenient and clean notepad!")

def quitProgram():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

def helpMe():
    messagebox.showinfo("Help", "Haha, bamboozled: no help here")


root = Tk()
root.title("Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)
text = scrolledtext.ScrolledText(root, width=400, height=400)
text.pack()

font_specs = (color + "monaco", 8)
menubar = Menu(root, font=font_specs)
root.config(menu=menubar)

filemenu = Menu(menubar, font=font_specs, tearoff=0)
filemenu.add_command(label='New', command=newFile)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save', command=saveFile)
filemenu.add_command(label='Save As', command=saveAs)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=quitProgram)
menubar.add_cascade(label='File', menu=filemenu)

helpMenu = Menu(menubar)
menubar.add_cascade(label='Help', command=helpMe)
menubar.add_cascade(label='About', command=about)

root.mainloop()
