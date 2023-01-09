from tkinter import *
from PIL import ImageTk,Image

root = Tk()
#root.iconbitmap('Photo.ico') // It's for icon

my_img = ImageTk.PhotoImage(Image.open("Photo/Photo.jpeg"))   
my_Label = Label(image=my_img)
my_Label.pack()



root.mainloop()