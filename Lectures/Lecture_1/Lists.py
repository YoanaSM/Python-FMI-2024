
#list = array
#elements can be from different types

my_list = []
my_list.append("hi, i am")
my_list.append(21)
my_list.append("years old.")
my_list.append(True)

print(my_list)
print(my_list[1]==20)

my_list[1]=20
print(my_list[1]==20)

del(my_list[1])
print(my_list[1])
print(len(my_list))

print("years old." in my_list)
print(21 in my_list)

#lists - slicing

print(my_list[1:3])#from element on the first pos to th element on the third pos
print(my_list[-2])
print(my_list[::-1])# printing backwards
