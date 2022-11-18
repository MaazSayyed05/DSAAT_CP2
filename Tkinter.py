from tkinter import *
from PIL import Image
from PIL import ImageTk
# from DSAAT_CP import check_sparse
root=Tk() #basic gui is created

# gui logic here

# geometry("width x height")
root.geometry("200x500")

# minsize(width , height)
root.minsize(600,600)

#maxsize(width,height)
# root.maxsize(1200,1200)


# Label
# lb1=Label(text="This is Label of GUI\n")
# lb1.pack()
# lb1=Label(text="Welcome to Tkinter\n")
# lb1.pack()


# Images
# img1=PhotoImage(file="fami.png") error hai
# lab_img1=Label(image=img1)
# lab_img1.pack()

# # for jpg images
# image=Image.open("fam.jpg")
# photo=ImageTk.PhotoImage(image)

# lab_img1=Label(image=photo)
# lab_img1.pack()

lab2=Label(text="This is Umar Azam Sayyed\n")
lab2.pack()

# Title
root.title("My GUI") #change the title of tk 


# Important Label Options
# text=   adds the text
# bd   background
# fg   foreground
# font   sets and font
# padx   padding in x
# pady   padding in y
# relief    border styling   sunken, raised, groove,ridge

# for i in range(5):
#     kb3=Label(text="The number = "+str(i))
#     kb3.pack()


# Title_label1=Label(text="""
# \nMyself Muhammad Muaz Aslam Sayyed. I am currently pursuing B.Tech. at Vishwakarma Institute of \nTechnology in Pune. I live in Solapur city which is famous for its bedsheets, handlooms, and power \nlooms. It is located at boundary of Maharashtra, Telangana, and Karnataka, which is a special \ncharacteristic of our city. Solapur is also the important railway junction of Central Indian \nRailways while going to South India after Konkan Railways. In Solapur the medical facilities are \ngood and a government medical college is also located in Solapur. Solapur had one of the first \nmultiplex in India which was known as Bhagwat Theatre. In south eastern India Solapur is the city \nthat churns out the best pomegranates in Maharashtra. """,  bg="black",  fg="white", padx=60,pady=20, font=("century",20,"italic") ,borderwidth=10,relief=RIDGE#GROOVE#SUNKEN#RIDGE
# )

# # Imp pack options
# # Aanchor=n/w/e/s/nw/ns..
# # side=top,bottom,left,right
# # fill      padx        pady

# Title_label1.pack(anchor="e",side="left",fill=Y,padx=80,pady=30)







# for i in range(10):
#     if i%2==0:
#         lb=Label(text=str(i)+" It is even\n",font=("Bookman Old Style",30,"bold"),fg="red",bg="pink",)
#         lb.pack()
        

root.mainloop()#initiate gui page






