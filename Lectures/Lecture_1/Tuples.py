
#tuple is immutable while list is mutable!!!

#immutable = can not be changed
#Which objects are immutable in Python? - numbers, strings, tuples, True, False etc.

elements = (2.1,7,1234.23)
print(elements[2])
print(len(elements))
print(elements[2:])# from the element on pos 2 to the end

#Example how elements can not be changed:
a = 3
a += 2
print(a)
#here a is redirected to 5, but it does not change the value 3

#mutable vs. immutable
#Mutable - list:

mutt_list = [70 ,80 ,90]
mutt_list.append(100)
mutt_list[2] = 60
print(mutt_list)

#the code above changes the list to which a is directed

#immut_list = (70,80,90)
#immut_list[2] = 60

#the code above can not be compiled - > the tuples are immutable

#Question: Why tuples are immutable?
#Answer: This is because tuples are logically connected values. The usage of tuples says that we do not want to change the data in them.
#Example: We have a vector. If we change one of its elements the vector becomes a completely different one.

# If we want to make a tuple from 1 element only we write it like that (<element>, ).
one_el_tuple = ("One element tuple",)
print(one_el_tuple)

#We can initialize a tuple without the braces:
one_el_tuple = 'One element tuple',
print(one_el_tuple)
#Tuples have index and count methods. They are the same as the ones used for the lists.
