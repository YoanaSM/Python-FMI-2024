
#1:
(x,y) = 10,100
print(x)

#also the following is valid too:
a,b = 1,3
print(a)

#2:
quantity_of_products = (10,5,17)
apples,pears,peaches = quantity_of_products
print(apples)
#with list is the same

#3:
a,*b,c = 0,11,22,33,4
print(b)
# b = 11,22,33
#The *b syntax is used to collect any remaining values between the first and the last into a list

#How to compare lists and tuples?
# - they are compared lexicographically
#Example:

print((1,2)<(1,3))
#True
print((1,2)<(1,2))
#False
print((1,2)<(1,2,3))
#True
print([1,2]<[1,3])
#True - there is no difference whether it is a list or a tuple for comparison

#!!! we can not compare tuple and list in one comparison
#Example:
#(1,2,3) < [1,2,3]
# The error is unorderable types