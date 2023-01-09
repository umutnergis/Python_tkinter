from tkinter import *
root = Tk()
root.title("Simple Calculator") #It means title where when the program runs you can see on upside

e = Entry(root,width=35,borderwidth=5,bg= "blue")
e.grid(row=0,column=0,padx = 10,pady=10,columnspan=3)

sum = 0
def button_click(number):
    #e.delete(0,END) // This line delete everything that why we can write only one digit
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_cl():
    e.delete(0,END)
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(first_number)
    e.delete(0,END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "Multiply"
    f_num = int(first_number)
    e.delete(0,END)
def button_substract():
    first_number = e.get()
    global f_num
    global math
    math = "Substract"
    f_num = int(first_number)
    e.delete(0,END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "Divide"
    f_num = int(first_number)
    e.delete(0,END)        
def equal_func():
    second_number = e.get()
    e.delete(0,END)
    if(math == "Divide"):
        e.insert(0,f_num / int(second_number))
    elif(math == "Addition"):
        e.insert(0,f_num + int(second_number))
    elif(math == "Substract"):
        e.insert(0,f_num - int(second_number))
    else:
        e.insert(0,f_num * int(second_number))

button_1 = Button(root,text="1",padx=40,pady=20,command= lambda:button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command= lambda:button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command= lambda:button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command= lambda:button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command= lambda:button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command= lambda:button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command= lambda:button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command= lambda:button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command= lambda:button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command= lambda:button_click(0))
button_sum = Button(root,text ="+",padx =39,pady =20,command =button_add) 
button_equal= Button(root,text="=",padx=91,pady=20,command =equal_func)
button_clear = Button(root,text ="Clear",padx=79,pady= 20,command =lambda:button_cl())
button_substractt = Button(root,text ="-",padx =40,pady =20,command =button_substract)
button_multiplyy = Button(root,text ="*",padx =40,pady =20,command =button_multiply)
button_divider = Button(root,text ="/",padx =40,pady =20,command =button_divide)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2) 

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_sum.grid(row=5,column=0) 
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)

button_multiplyy.grid(row=6,column=0)
button_divider.grid(row=6,column=1)
button_substractt.grid(row=6,column=2)

root.mainloop()