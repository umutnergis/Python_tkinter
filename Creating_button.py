from tkinter import *
root = Tk()
def myCLick():
    myLabel = Label(root,text = "I clicked button! ")
    myLabel.pack()
    
#,state = DISABLED -- It means button doesn't work  
#,padx = Horizontal axis , pady = Vertical axis 
myButton = Button(root,text = "Click me ",padx=10 ,pady = 10,background= "green",activebackground="red",command= myCLick)
myButton.pack()
root.mainloop()