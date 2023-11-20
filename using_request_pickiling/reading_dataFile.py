import pickle

# i will not use request because file is directly downloaded from the link

with open("iris.data") as f:
    data_file=f.readlines()

converted_list=[]

for value in data_file:
    converted_list.append(value.strip())

# print(converted_list)

with open("iris.txt","wb") as f:
    pickle.dump(converted_list,f)


with open("iris.txt","rb") as f:
    read_data=pickle.load(f)

print(read_data)