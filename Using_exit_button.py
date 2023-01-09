from tkinter import *

root = Tk()
root.title("Exit Example")
exit_button = Button(root,text="Exit",command=root.quit)
exit_button.grid(padx=40,pady=40,column=0,row=0)
root.mainloop()