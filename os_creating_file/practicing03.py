import os


list2=os.listdir()
# print(list2)


# making other list
list1=['this', 'that', 'normal']
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

# print(jpg_list)
# print(py_list)


# print(list2)