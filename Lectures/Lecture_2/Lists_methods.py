
cake = ['sugar','milk','cream']
shopping_cart = ['meat','eggs', cake,'oranges','meat']

#What methods the lists have?

#1: To return the index of the first occurrence of an element:
print(shopping_cart.index('eggs'))
print(shopping_cart.index(cake))
#But we can not do the following:
#print(shopping_cart.index('sugar'))
# because 'sugar' is not an element of shopping_cart.
# 'sugar' is an element inside the cake list, which is itself an element of shopping_cart.

#2: Counting occurrence of an element:
print(shopping_cart.count('meat'))

#3: .sort()(lexicographically) and .append() #.sort(reverse=True) for sorting ascending
#4: extend(element) - to add elements of element in th elist but faster than +

shopping_cart + cake
print(shopping_cart)

shopping_cart.extend(cake)
print(shopping_cart)

shopping_cart.extend("apple")
print(shopping_cart)

#if we add apple like that it will add all symbols of apple but char by char
one_el_tuple = ('One element tuple')
print(one_el_tuple)