from customtkinter import *
from tkinter import *

from matplotlib.pyplot import margins

app = CTk()
set_appearance_mode("System")  # Dark and Light are possible

btn = CTkButton(master=app,
                text="Hehe",
                fg_color=("lightgrey", "white"),
                text_color=("white", "black")
                )
btn.pack()

label = CTkLabel(master=app,
                 text="CTkLabel",
                 width=120,
                 height=25,
                 corner_radius=8)
label.pack()

entry = CTkEntry(master=app,
                 width=120,
                 height=25,
                 corner_radius=10)
entry.pack()

checkbox = CTkCheckBox(master=app,
                       text="CTkCheckBox")
checkbox.pack()


def slider_event(value):
    print(value)


slider = CTkSlider(master=app,
                   width=160,
                   height=16,
                   border_width=5.5,
                   from_=0,
                   to=100,
                   command=slider_event)
slider.pack()

progressbar = CTkProgressBar(master=app,
                             width=160,
                             height=20,
                             border_width=5)
progressbar.pack()

progressbar.set(0.5)

menubar = Menu(master=app)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="hehe")
menubar.add_cascade(menu=filemenu,label="File")

app.config(menu=menubar)
app.mainloop()
