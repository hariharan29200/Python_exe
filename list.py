list1=["apple","orange","mango","banana"]
print(list1)
print(type(list1))
for x in list1:
    print(x)

print()

list1[2]="bomb"
print(list1)

print(len(list1)) # print the size of list

print(list1.pop()) # pop the last element from the list
print(list1)
list1.insert(1,"dog") #insert the new element with the list at the index(1)
print(list1)


#output----------------------------------
['apple', 'orange', 'mango', 'banana']
<class 'list'>
apple
orange
mango
banana

['apple', 'orange', 'bomb', 'banana']
4
banana
['apple', 'orange', 'bomb']
['apple', 'dog', 'orange', 'bomb']
