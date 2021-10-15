from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('P164')
root.geometry('500x500')
root.configure(background='black')

img_label = Label(root,bg='white',highlightthickness=5)
img_label.place(relx=0.5,rely=0.2,anchor=CENTER)

img_path = ''
def stuff():
    global img_path
    img_path = filedialog.askopenfilename(title='Open Text File',filetypes=[('Image Files','*.jpg;*.gif;*.jpg;;*.png;*txt')])
    print(img_path)
    img_e = ImageTk.PhotoImage(Image.open(img_path))

    img_label['image'] = img_e
    img_e.close()

btn = Button(root,text='Open Image',command=stuff,font=('courier',18,'bold'))
btn.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()