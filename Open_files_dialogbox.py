from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Open Files")
#initialdir = begining path, filetypes = which you want
root.filename = filedialog.askopenfilename(initialdir="/Python",title="Select File",filetypes=(("Png files","*.png"),("All files","*.*")))
#it return file directory
my_label = Label(root,text=root.filename).pack()



root.mainloop()