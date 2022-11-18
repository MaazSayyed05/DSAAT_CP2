# Menus and submenus in Tkinter
# Messaagebox module of Tkinter

# from tkinter import *
# import tkinter.messagebox as tmsg
# root=Tk()
# root.geometry("700x600")
# def myfunc():s
#     lb1=Label(text="You clicked on file menu\n")
#     lb1.pack()

# def help():
#     # l1=Label(root,text="This is Help\n")
#     # l1.pack()
#     a=tmsg.showinfo("This is help")
#     l1=Label(root,text=a)
#     l1.pack()


# def rate():
#     a=tmsg.askquestion("Are you okay\n")
#     if a=="yes":
#         msg="Greta Rate us now\n"
#     else:
#         msg="Zaroorat Nahi Rate ki\n"
#     tmsg.showinfo("Experience",msg)
#     # l1=Label(root,text=a)
#     # l1.pack()


# def friend():
#     ans=tmsg.askretrycancel("Pata lunga mai use","Chappal padegi nikal le")
#     if ans:
#         l1=Label(root,text="Mai kal aur ata")
#         l1.pack()
#     else:
#         l1=Label(root,text="Chal nikal chudail kahi ki")
#         l1.pack()


# # # Use this to create a non-dropdown menu
# # root.title("MENU")
# # mymenu=Menu(root)
# # mymenu.add_command(label="File",command=myfunc)
# # mymenu.add_command(label="Exit",command=quit)
# # root.config(menu=mymenu)

# mainmenu=Menu(root)

# m1=Menu(mainmenu,tearoff=0)
# m1.add_command(label="New Project",command=myfunc)
# m1.add_command(label="Edit",command=myfunc)
# m1.add_separator()#line
# m1.add_command(label="Save",command=myfunc)
# m1.add_command(label="Save As",command=myfunc)
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="File",menu=m1)



# m2=Menu(mainmenu,tearoff=0)
# m2.add_command(label="Cut",command=myfunc)
# m2.add_command(label="Copy",command=myfunc)
# m2.add_separator()#line
# m2.add_command(label="Paste",command=myfunc)
# m2.add_command(label="Find",command=myfunc)
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="Edit",menu=m2)

# m3=Menu(mainmenu,tearoff=0)
# m3.add_command(label="Help",command=help)
# m3.add_command(label="Rate Us",command=rate)
# m3.add_command(label="Friend",command=friend)
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="HELP",menu=m3)
# root.mainloop()


# Sliders in Tkinter
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
def getdollar():
    Label(root,text=f"You get -{myslider.get()} dollars").pack()
    tmsg.showinfo("Kaisa Laga Mera Mazak")
root.geometry("700x500")
root.title("Sliders in Tkinter")


Label(root,text="How many Dollars you want?").pack()
myslider=Scale(root,from_=0,to=10,orient=HORIZONTAL,tickinterval=2,bg="sky blue",fg="red")
myslider.set(30)

myslider.pack()

Button(root,text="Get Dollars",command=getdollar).pack()

# myslider2=Scale(root,from_=0,to=200)
# myslider2.pack()

root.mainloop()





