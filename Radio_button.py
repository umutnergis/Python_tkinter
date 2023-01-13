from tkinter import *
 
root = Tk()
root.title("Radio Button")


game_list = [
    ("Valorant","Valorant"),
    ("LOL","LOL"),
    ("CS-GO","CS-GO"),
    ("MTA","MTA"),
]

var = StringVar() #if variable is string then use StringVar()or IntVar()
var.set("Valorant") #set default value

def checked(value):
    print(value)
    sit_var = Label(root,text=value,padx=20,pady=20)
    sit_var.pack()
#Problem = value is coming wrong
for text,mode in game_list:
    Radiobutton(root,text=text,value=mode,variable=var).pack(anchor=W) #anchor getting radio to left side 

sit_var = Label(root,text=var.get(),padx=20,pady=20).pack()
buton =Button(root,text= "Click ",padx=20,pady=20,command=lambda: checked(var.get())).pack()

    

#Radiobutton(root,text="Option 1",value=1,variable=var,command= lambda: checked(var.get())).pack()
#Radiobutton(root,text="Option 2",value=2,variable=var,command= lambda: checked(var.get())).pack()
#Radiobutton(root,text="Option 3",value=3,variable=var,command= lambda: checked(var.get())).pack()


root.mainloop()