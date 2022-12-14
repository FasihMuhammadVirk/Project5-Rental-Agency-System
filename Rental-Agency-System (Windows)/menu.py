import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

from PIL import Image, ImageTk
import Customer as C
import Owner as O
import Rented_Apartment_House as A
import Forsale as F
import Rent as R
import Society as S
import Search as sr

s = S.Society()
c = C.Customer()
o = O.Owner()
a = A.RENT()
f = F.ForSale()
r = R.ForRent()

    

def main():

    root1 = Tk()
    root1.geometry("1300x1080")
    windows = root1

    load = Image.open('images/pic1.png')
    render = ImageTk.PhotoImage(load)

    img = Label (root1, image = render)
    img.place(x=0,y=0,relwidth = 1, relheight = 1)
    
    root = LabelFrame(root1,bg = 'linen',padx=30,pady =10)
    root.pack(padx=400,pady=150)
    
    def call():
        root1.destroy()
        sr.main()
    


    def ext():
        # root.destroy()
        root1.destroy()
            
    root1.title("Main Menu")
   
    Label(root,bg = 'linen',text='Welcome to Rent and Sale', bd=20, font=('times new roman', 20, 'bold'), relief="groove",width=300).pack()
    Label(root,text="",bg = 'linen').pack()
    
    Button(root,highlightbackground = 'linen', text="Societies",command = s.main,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Customer Information",command = c.main,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Owner Information",command = o.main,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Rented Apartment",command = a.main,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Sale Information",command = f.main,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Rent Information",command = r.main,height=1, width= 16).pack()
    Button(root,highlightbackground = 'linen', text="Search Data",command = call ,height=1, width= 22).pack()
    Button(root,highlightbackground = 'linen', text="Quit",command = ext,height=1, width= 7).pack()


    root1.mainloop()
    
    
