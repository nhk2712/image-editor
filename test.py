from tkinter import *
from PIL import Image, ImageTk, ImageEnhance
import cv2 as cv

img = Image.open("C:/Users/Admin/Downloads/chemtech.jpg")
enhancer = ImageEnhance.Brightness(img)
out = enhancer.enhance(1)

app = Tk()
app.title('Image Editor')
app.geometry('640x480')
app.iconbitmap('icon.ico')

imgtk = ImageTk.PhotoImage(image=out)
imgDisp=Label(app, image= imgtk)
imgDisp.pack()

def change(event):
    val = slider.get()/10
    img = Image.open("C:/Users/Admin/Downloads/chemtech.jpg")
    enhancer = ImageEnhance.Brightness(img)
    out = enhancer.enhance(val)

    imgtk = ImageTk.PhotoImage(image=out)
    imgDisp=Label(app, image= imgtk)
    imgDisp.pack()
slider = Scale(app,from_=0,to=20,orient='horizontal',command=change)
slider.set(10)
slider.pack()

app.mainloop()