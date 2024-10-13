
# Definition for set: a collection without duplicated elements
# The ORDER is NOT guaranteed
# We DO NOT have DIRECT ACCESS to the elements!!!
# We use them in math context
# Elements must be IMMUTABLE
# Sets are MUTABLE


#Examples:

odd_numbers_set = set();
odd_numbers_set.add(1);
odd_numbers_set.add(3);
odd_numbers_set.add(5);
odd_numbers_set.add(9);
odd_numbers_set.add(9);

print(odd_numbers_set);#the number 9 is added only once

#also we can create a set like that:
even_numbers_set = {0,2,0,4,8,8,10}
print(even_numbers_set);
print({}) # ->this is not the empty set. THIS IS EMPTY DICTIONARY bc the dicts are more frequently used that the sets
print(len(even_numbers_set));#-> the size is the number i=of distinct elements

#How to create empty set?
#Answer:
empty_set = set()
print(empty_set)

#More examples:

random_set = {1,2,3,4}
print(random_set)

random_set.add(5)
print(random_set)

random_set.add(4)#it is not added bc it is already in the set
print(random_set)

random_set.remove(3)
print(random_set)

random_list = [1,9,7,7,8]
print(set(random_list))# when we make a set from list it  makes a set from the elements of the list, but it includes them only once
print(random_list)# the previous operation does not change the list itself

#we can check if an element is inside the set
print(7 in set(random_list))
print(6 in set(random_list))
