# from tkinter import *
# root=Tk()
# canvas_width=800
# canvas_height=400

# root.geometry(f"{canvas_width}x{canvas_height}")
# root.title("Canvas")a

# can_widget=Canvas(root,width=canvas_width,height=canvas_height)
# can_widget.pack()

# 1. The line goes from x1,y1 to x2,y2  
# can_widget.create_line(100,100,300,100,fill="blue")# create_line(x1,y1,x2,y2)
# can_widget.create_line(200,0,200,100,fill="red")# create_line(x1,y1,x2,y2)

# 2.Create rectangle    create_rectangle(top-left,bottom-right)
# can_widget.create_rectangle(100,50,400,300,fill="sky blue")
# can_widget.create_rectangle(120,70,430,330,fill="dark red")
# can_widget.create_rectangle(140,90,460,360,fill="grey")


# 3.Create text   centre coordinate
# can_widget.create_text(100,300,text="This is text")

# 4.Create oval   pass coordinates of rectangle
# can_widget.create_oval(100,30,600,390,fill="red")

# root.mainloop()

# Events in Tkinter
from tkinter import *

def new(event):
    r1=Tk()
    r1.geometry("300x400")
    for i in range(5):
        l1=Label(r1,text="This is label\n")
        l1.pack()
    btn=Button(r1,text="Submit",command=quit)
    btn.pack()
    r1.mainloop()
def printf(event):
    for i in range(4):
        lb1=Label(root,text="Button is clicked")
        lb1.pack()
root=Tk()
root.title("Events in Tkinter")
root.geometry("700x500")
widget=Button(root,text="Click Me")
widget.pack()
# Check all events of tkinter
widget.bind('<Button-1>',new)
widget.bind('<Double-1>',quit)#...

root.mainloop()



