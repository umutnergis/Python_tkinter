from tkinter import *
def myClick():
    myLabel = Label(root,text = "Hello "+ e.get()) #e.get() = means that written stuff from user
    myLabel.pack()
#borderwidth = distance between upside to entry's upside
root = Tk()
root.title("Umut's Program")
e = Entry(root,width=50,bg= "blue",fg = "white",borderwidth=5)
e.pack()
#insert = The text inside of entry square 
e.insert(0,"Please enter your name")


myLabel = Label(root,text ="Hello I am Umut")
myLabel.pack()
#create button
buton = Button(root,text ="Click me",padx= 10,pady= 10,bg= "red",command=myClick)
buton.pack()
#mainloop
root.mainloop()
