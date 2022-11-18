from tkinter import *
    
root=Tk()
root.geometry("900x600")

q1_l1=Label(text=" Enter Input: ",font=("century",16,"bold"),bg="grey")
q1_l1.place(x=450,y=50)

q1_input=StringVar()
q1_entry=Entry(root,textvariable=q1_input,font=("century",16,"bold"))
q1_get=q1_input.get()
q1_get.split()
q1_entry.place(x=650,y=50)


q1_starts=Label(text=" Starts with: ",font=("century",16,"bold"),bg="grey")
q1_starts.place(x=80,y=130)

q1_starts_input=StringVar()
q1_starts_entry=Entry(root,textvariable=q1_starts_input,font=("century",16,"bold"))
q1_starts_get=q1_starts_input.get()
q1_starts_get.split()
q1_starts_entry.place(x=280,y=130)



q1_ends=Label(text=" Ends with: ",font=("century",16,"bold"),bg="grey")
q1_ends.place(x=900,y=130)

q1_ends_input=StringVar()
q1_ends_entry=Entry(root,textvariable=q1_ends_input,font=("century",16,"bold"))
q1_ends_get=q1_ends_input.get()
q1_ends_get.split()
q1_ends_entry.place(x=1100,y=130)


q1_proceed=Button(text=" PROCEED ",font=("century",14,"bold"),bg="maroon")
q1_proceed.place(x=640,y=220)





root.mainloop()






