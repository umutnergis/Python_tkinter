from tkinter import *

root = Tk()
root.title("Check Box")

vari = IntVar()
    
check_box = Checkbutton(root,text="Click or Not",variable = vari)
check_box.pack()



def click():
    my_label = Label(root,text=vari.get()).pack()
my_button =Button(root,text="Click",command=click).pack()

root.mainloop()