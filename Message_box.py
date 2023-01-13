from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Message Box")

#showinfo,showarning,showerror,askquestion,askokcancel,askyesno

def clicked():
    response = messagebox.askyesno("Warning","Something went wrong")
    my_label = Label(root,text="Response " + str(response)).pack()
    if response == True:
        Label(root,text=str(response)).pack()
    else:
        Label(root,text=str(response)).pack()

buton = Button(root,text="Click Me",padx=20,pady=20,command=clicked).pack()
root.mainloop()