

# We can make unions/intersections/differences etc.

first_group_of_elements = {1,2,3}
second_group_of_elements = {2,3,4}

union = first_group_of_elements | second_group_of_elements
print(union)

intersection = first_group_of_elements & second_group_of_elements
print(intersection)

diff = first_group_of_elements - second_group_of_elements# the elements of the first without th elements of the second
print(diff)

common_elements= first_group_of_elements ^ second_group_of_elements
print(common_elements)

#we can check whether a set is a subset
print(first_group_of_elements < second_group_of_elements)#False
print({2,3} < second_group_of_elements)#True

print({2,3}=={2.0,3})#True

#!!! Sets can be used if we want to get only the unique elements of a list.