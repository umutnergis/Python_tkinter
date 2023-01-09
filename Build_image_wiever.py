from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Image Wiever")
global number
number = 0

def go_right():
    global number
    if(number <=5):
        photo_list[number].grid(column=0,row=0)
        number = number + 1
def go_left():
    global number
    if(number >=0):
        photo_list[number].grid(column=0,row=0)
        number = number - 1
    

image1 = ImageTk.PhotoImage(Image.open("Cars/A1.jpg"))
image2 = ImageTk.PhotoImage(Image.open("Cars/A2.jpg"))
image3 = ImageTk.PhotoImage(Image.open("Cars/A3.jpeg"))
image4 = ImageTk.PhotoImage(Image.open("Cars/A4.jpg"))
image5 = ImageTk.PhotoImage(Image.open("Cars/A5.jpg"))
image6 = ImageTk.PhotoImage(Image.open("Cars/A6.jpg"))

exit_button = Button(root,text="Exit",activebackground="red",command = root.quit)
right_button = Button(root,text=">>",activebackground="green",command = go_right)
left_button = Button(root,text="<<",activebackground="blue",command = go_left)

my_Label1 = Label(image=image1)
my_Label2 = Label(image=image2)
my_Label3 = Label(image=image3)
my_Label4 = Label(image=image4)
my_Label5 = Label(image=image5)
my_Label6 = Label(image=image6)


exit_button.grid(row=2,column=1,padx=40,pady=20)
right_button.grid(row=2,column=2,padx=20,pady=20)
left_button.grid(row=2,column=0,padx=20,pady=20)


photo_list = [my_Label2,my_Label3,my_Label4,my_Label5,my_Label6]



root.mainloop()