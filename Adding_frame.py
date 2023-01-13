from tkinter import *

root = Tk()
root.title("Frame Example")

frame = LabelFrame(root,text="This is my frame",padx=50,pady=50) # padx and pady are using for distance inside of frame 
frame.pack(padx=10,pady=10) # padx and pady are using for distance between frame and root (ouside of frame)

buton = Button(frame,text="Don't click here")
buton.pack()
root.mainloop()