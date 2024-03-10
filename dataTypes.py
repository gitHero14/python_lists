#creating an empty list
my_list = []

#appending to Lists
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#extending to Lists
new_list = [50,60,70]
my_list.extend(new_list)

#removing an element from lists
del my_list[-1]

#sorting lists
my_list.sort()

#indexing lists
print(my_list.index(30))
