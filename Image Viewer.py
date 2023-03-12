from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("360x480")
root.title("Image Viewer")
root.iconbitmap("./iconfinder-image-4341296_120549.ico")

my_image1 = ImageTk.PhotoImage(Image.open("images/wp4833742-anime-dark-1920x1080-wallpapers.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("images/wp5239703-anime-dark-1920x1080-wallpapers.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("images/wp6351150-anime-dark-1920x1080-wallpapers.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("images/wp7218226-anime-dark-1920x1080-wallpapers.jpg"))
my_image5 = ImageTk.PhotoImage(Image.open("images/wp7218261-anime-dark-1920x1080-wallpapers.jpg"))
my_image6 = ImageTk.PhotoImage(Image.open("images/anime.jpg"))

image_list = [my_image1 , my_image2 ,my_image3 , my_image4 , my_image5 , my_image6]



my_label = Label(image=my_image1 ,height=200 ,width=200)
my_label.grid(row=0 , column=0 , columnspan=3 )

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1] ,height=200 ,width=200)
    button_forward = Button(root , text=">>" , command=lambda: forward(image_number+1))
    button_back = Button(root , text="<<" , command=lambda: back(image_number-1))

    my_label.grid(row=0 , column=0 , columnspan=3)
    button_back.grid(row=1 ,column=0)
    button_forward.grid(row=1 , column=2)
def back():
    global my_label
    global button_forward
    global button_back


button_back = Button(root , text="<<" , command=back())
button_exit = Button(root , text="Exit Program" , command=root.quit)
button_forward = Button(root , text=">>" , command=lambda:forward(2))

button_back.grid(row=1 ,column=0)
button_exit.grid(row=1 ,column=1)
button_forward.grid(row=1 , column=2)



root.mainloop()
