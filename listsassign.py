#the empty list
my_list=[]
#appending the elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#inserting 15 at the 2nd position
my_list.insert(1,15)
#extending the list
new_list=my_list.extend([50,60,70])
#removing last element
my_list.pop()
#sorting
my_list.sort()
#printing the index
print(my_list.index(30))