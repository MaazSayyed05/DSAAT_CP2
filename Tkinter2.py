# Frame in TK
# from tkinter import *
# root=Tk()
# root.geometry("800x600")
# Frame(root,bg="grey",borderwidth=5,relief=RIDGE)
# pack(side=LEFT,fill=X)

# f2=Frame(root,bg="grey",borderwidth=8,relief=RIDGE)
# f2.pack(fill=Y,side=LEFT)
# l2=Label(f2,text="Welcome to side bar",font=("century",30,"italic"),bg="red")
# l2.pack()


# l1=Label(text="Project Tkinter",font=("times new roman",26,"bold"))
# l1.pack()

# root.mainloop()



# sunken, raised, groove,ridge
# Buttons in Tk
# from tkinter import *
# def print():
#         Frame(root,bg="grey",relief=GROOVE,borderwidth=5)
#         pack(side=RIGHT)
#         b2=Button(text="Enter text\n",font=("arial",10,"bold"),bg="grey",relief=GROOVE)
#         b2.pack(side=RIGHT)

# root=Tk()
# root.geometry("700x500")
# # Frame(root,bg="grey",relief=GROOVE,borderwidth=5)
# # pack(side=LEFT,anchor=NW)

# b1=Button(borderwidth=3,relief=RAISED,bg="grey",text="1")
# b1.place(x=10,y=20)#x-> change in X-axis

# b2=Button(borderwidth=3,relief=RAISED,bg="grey",text="2")
# b2.place(x=10,y=60)

# b3=Button(borderwidth=3,relief=RAISED,bg="grey",text="3")
# b3.place(x=10,y=100)

# b4=Button(borderwidth=3,relief=RAISED,bg="dark grey",text="4")
# b4.place(x=10,y=140)

# root.mainloop()



# Widget and Grid Layout
# from tkinter import *
# root=Tk()
# root.geometry("700x500")
# def getval():
#         lb1=Label(text=uservalue.get(),font=("century",16,"bold"))
#         lb1.grid(row=4)
#         # lb1.pack()

#         lb2=Label(text=passvalue.get(),font=("century",16,"bold"))
#         lb2.grid(row=5)

# user=Label(text="Username\n")
# password=Label(text="Password\n")
# user.grid()
# password.grid()

# # variable classes in tk
# # BooleanVar, DoubleVar, intvar, Stringvar

# uservalue=StringVar()
# passvalue=StringVar()

# userentry=Entry(root,textvariable=uservalue)
# passentry=Entry(root,textvariable=passvalue)

# userentry.grid(row=0,column=3)
# passentry.grid(row=1,column=3)

# Button(text="Submit",command=getval).grid()

# root.mainloop()


from tkinter import *
def list_num(l1):
        for i in range(len(l1)):
                print(l1[i])
def printf():
        for i in range(int(row_val.get())):
                        # lb1=Label(text="Print is activated\n")
                        # lb1.grid(row=8+i,column=4) 
                        rows=Label(text="Enter number of rows: \n")
                        rows.grid(row=8+i)
                        row_vals=StringVar()
                        row_entry=Entry(root,textvariable=row_vals)
                        row_entry.grid(row=8+i,column=3)
                        l=[]
                        l.append(row_vals.get())
        
                        



root=Tk()
root.geometry("700x500")
lb1=Label(root,text="Matrix Calculator\n",font=("century",14,"bold"),fg="grey")
lb1.grid(row=0,column=8)

rows=Label(text="Enter number of rows: \n")
rows.grid(row=3)

col=Label(text="Enter number of columns: \n")
col.grid(row=4)

row_val=StringVar()
col_val=StringVar()

row_entry=Entry(root,textvariable=row_val)
col_entry=Entry(root,textvariable=col_val)

row_entry.grid(row=3,column=4)
col_entry.grid(row=4,column=4)

btn=Button(text="Submit")
btn.grid(row=6,column=2)


root.mainloop()



