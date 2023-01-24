from tkinter import *
from PIL import ImageTK,Image


root = Tk()
root.title("First Screen")

def opensecond():
    global img
    sec_screen = Toplevel()
    sec_screen.title("Second Screen")
    img = ImageTK.PhotoImage(Image.open("Cars/A2.jpg"))
    img_lbl =Label(sec_screen,image=img).pack()
    

buton = Button(root,"Click for second screen",command=opensecond).pack()