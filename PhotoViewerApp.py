from tkinter import*
from PIL import ImageTk,Image

root= Tk()

root.title("PhotoViewerApp")

# displaying current image
def show_current_image():
        global current_index
        c_img = my_images[current_index]
        label= Label(image=c_img)
        label.grid(row=0,column=0,columnspan=3)

# displaying previous image
def previous_image():
        global current_index
        if(current_index > 0):
            current_index=current_index-1
            show_current_image()
        else:
               pass
        
# displaying next image        
def next_image():
        global current_index
        if(current_index < len(my_images)-1):
            current_index=current_index+1
            show_current_image()
        else:
                pass
        
# IMAGES FOLDER
img1= ImageTk.PhotoImage(Image.open("images\\img1.jpg").resize((250,250)))
img2= ImageTk.PhotoImage(Image.open("images\\img2.jpg").resize((250,250)))
img3= ImageTk.PhotoImage(Image.open("images\\img3.jpg").resize((250,250)))
img4= ImageTk.PhotoImage(Image.open("images\\img4.jpg").resize((250,250)))
img5= ImageTk.PhotoImage(Image.open("images\\img5.jpg").resize((250,250)))
my_images = [img1,img2,img3,img4,img5]

# calling current image
current_index = 0
show_current_image()

# previous button
left_button = Button(root,text="<<" ,command=previous_image, activebackground="green" , padx=20)
left_button.grid(row=1,column=0) 

# exit button
exit_button = Button(root,text="Exit Program" , command=root.quit, activebackground="red")
exit_button.grid(row=1,column=1)

# forward button
right_button = Button(root,text=">>" , command=next_image, activebackground="green" , padx= 20)
right_button.grid(row=1,column=2)

root.mainloop()