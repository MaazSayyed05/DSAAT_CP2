from math import *
from string import *
from tkinter import *

def mks(i,j):
    # k=i+j
    return i+j 

# i=48.45
# maazsayyed=50#no whitespace allowed and variable should not start with number
# k="Maaz Sayyed"
# print(i+2.334,k,maazsayyed)
# print(type(i),type(k),"Length of k = ",len(k))

# Type Casting=>change of variable from one datatype to another
# k="10"
# print(float(k)+10)
# i=20
# print(str(i)+"30")
# i=int(k)
# print(i+10)


# Strings
# str1="   Maaz Sayyed   "
# print(str1,"Length of string is",len(str1),str1[2],str1[3:6](3(first index in slicing) is not counted in slicing of STRING),str1.strip(),str1+" Aslam",str1.replace("a", "A"))

# s1="I am {}\n".format(str1)
# s2=f"I am {str1}\n"
# print(s1,s2)

# str2=input("Enter string\n").split()
# str3=input("Enter string\n").capitalize()

# str4=input("Enter string\n").isupper()
# str4=input("Enter string\n").islower()

# str5=input("Enter string\n").upper()
# str5=input("Enter string\n").lower()


# List
# list2=input().split() takes input string and convert it into a list with NO whotespaces
# list1 = [9,2,5,3,7,1]
# str1="1 2 3 4"
# l2=list(str1)
# # print(int(l2[2])*100)
# # l2[2]=200
# # print(list1)
# list1.pop()
# list1.append(2000)
# # list1.clear()
# list1.remove(2)
# list1.insert(2, 1000)
# list1.sort()
# print(list1,len(list1),list1.count(2),list1.index(9)) # [m:n]=>In LIST, n[last index of slice] is not counted in slicing       NEW LIST is Created



# Tuples
# tuple1=(1,2,3,4,2,2)
# var=tuple1
# print(var)
# # print(tuple1,tuple1.count(2),tuple1.index(2))
# l1=input("Enter string: ").split()
# t1=tuple(l1)
# l1[0]="MAAZ"
# # t1[0]="MAAZ"
# print(t1,l1)



# Set
# s1={8,6,4,2,1}
# s2={1,3,5,7,9}
# s1.add(10)
# s2.update((2,4,5,6))
# s2.discard(1)
# s1.discard(4)
# # s1.clear()
# print(s2)
# print(s1,s1.copy(),s1.difference(s2),s1.intersection(s2),s2.issubset(s1),s1.union(s2))



# Dictionary
# marksdict={
#     input("Enter key1: \n"): input("Enter Name of Student: \n"),
#     "Marks": input("Enter Marks of Student = \n"),
#     "PRN No.": input("Enter PRN No. of Student = \n"),
#     "Class": input("Enter Class of Student = \n"),
#     "Roll No.": input("Enter Roll No. of Student = \n"),
# }
# print(marksdict)
# print(marksdict["Marks"],marksdict["PRN No."])
# marksdict["Class"]="SY_IT_A"
# print(marksdict["Marks"],marksdict["PRN No."],marksdict["Class"])
# marksdict.pop("Marks")

# print(marksdict,marksdict.get("PRN No."),marksdict.items())
# m2=marksdict.copy()
# print(m2)


# mks=int(input("Enter marks of student = "))
# if(mks>50):
#     print("PASS\n")
# elif(mks==50):
#     print("REEXAM\n")
# else:
#     print("FAIL\n")

# for i in range(10):
#     for j  in range(10):
#         print(i,j)

# l1=[1,2,"Maaz",(1,2,3),[1,2],{"1","Sayyed"}]
# for i in l1:
#     print(i)

# print(mks(10, 200))





