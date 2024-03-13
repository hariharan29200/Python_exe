tuple1=("mango","apple","orange","bomb")
print(tuple1)
print(type(tuple1)) #to define the type of the dataset

for x in tuple1:
    print(x)

list2=["robots","code","game","animal"]
list2.extend(tuple1)
print(list2)
