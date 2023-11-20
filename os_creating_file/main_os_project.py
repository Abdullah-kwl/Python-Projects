import os

# i extracted name in files to list1 

# with open("file.txt") as f:    #this was old before pretify
with open("File.txt") as f:      #i was forget to convert img in jpg therefor i run again with this name'Filetxt'
    sample=f.readlines()

list1=[]
for element in sample:
    list1.append(element.strip())

# print(list1)

list2=os.listdir()
# print(list2)


# making other list
jpg_list=[]
py_list=[]

# gathering data in other list
for element in list2:
    if (element.endswith(".jpg")):
        jpg_list.append(element)


for element in list2:
    if element.endswith(".py"):
        py_list.append(element)
        
# removing the gathered data from list2 of os.listdir
for element in list1:
    list2.remove(element)

for i in jpg_list:
    list2.remove(i)

for j in py_list:
    list2.remove(j)


# here we have spacific list of all the seprated items

# print(jpg_list)
# print(py_list)
# print(list2)

# ---------------------------------------------
#here we will start the os operation on the lists

# i capatelize all the name in list2(e.g folder or file.txt)

for k in list2:
    sample_name=k.capitalize()
    os.rename(k , sample_name)

# i rename all the (.jpg) formate files

a=11
for n in jpg_list:
    os.rename( n , (f"{a} image.jpg"))
    a=a+1


# i successfuly completed the task