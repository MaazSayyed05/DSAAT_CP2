from tkinter import *
root=Tk()

# geometry("width x height")
root.geometry("900x600")

# minsize(width , height)
# root.minsize(600,600)

#maxsize(width,height)
# root.maxsize(1200,1200)

# f1=Frame(root,bg="grey",relief=GROOVE,
# f1.pack(side=LEFT,anchor=NW)
root.title("String Analyzer")

tlt=Label(text="  STRING  ANALYZER   ",font=("consolas",30,"bold"),bg="yellow",bd=4,relief=SOLID)
tlt.place(x=180,y=20)

l1=Label(text="Starts with x/Ends with x                                                   ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l1.place(x=100,y=100)

l2=Label(text="Occurence of alphabets from input set in a string                 ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l2.place(x=100,y=140)

l3=Label(text="String must include string 'x' in it.                                      ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l3.place(x=100,y=180)

l4=Label(text="Even occurence of 'x'/ Odd occurence of 'y'.                           ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l4.place(x=100,y=220)

l5=Label(text="Condition based on inequalities of a string.                           ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l5.place(x=100,y=260)

l6=Label(text="String do NOT contain 'x'or'xyz' in it.                                   ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l6.place(x=100,y=300)

l7=Label(text="Occurence of 'x' and starts with 'a'/ Ends with 'b'.                  ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l7.place(x=100,y=340)

l8=Label(text="String must contain 'xyz' in it and do NOT contain 'abc' in it. ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l8.place(x=100,y=380)

l9=Label(text="Inequalities of 'xyz' and followed by 'abc'.                              ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l9.place(x=100,y=420)

l10=Label(text="Starts with x/Ends with x                                                     ",font=("century",15,"bold"),bg="grey",borderwidth=3,relief=GROOVE)
l10.place(x=100,y=460)



b1=Button(borderwidth=3,relief=RAISED,bg="yellow",text="  1   ")
b1.place(x=30,y=100)#x-> change in X-axis

b2=Button(borderwidth=3,relief=RAISED,bg="grey",text="  2   ")
b2.place(x=30,y=140)

b3=Button(borderwidth=3,relief=RAISED,bg="grey",text="  3   ")
b3.place(x=30,y=180)

b4=Button(borderwidth=3,relief=RAISED,bg="grey",text="  4   ")
b4.place(x=30,y=220)

b5=Button(borderwidth=3,relief=RAISED,bg="grey",text="  5   ")
b5.place(x=30,y=260)

b6=Button(borderwidth=3,relief=RAISED,bg="grey",text="  6   ")
b6.place(x=30,y=300)

b7=Button(borderwidth=3,relief=RAISED,bg="grey",text="  7   ")
b7.place(x=30,y=340)

b8=Button(borderwidth=3,relief=RAISED,bg="grey",text="  8   ")
b8.place(x=30,y=380)

b9=Button(borderwidth=3,relief=RAISED,bg="grey",text="  9   ")
b9.place(x=30,y=420)

b10=Button(borderwidth=3,relief=RAISED,bg="grey",text="  10  ")
b10.place(x=30,y=460)





root.mainloop()



