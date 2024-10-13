
#What is the type of the following?
things  = ['milk',('egg','egg','egg'),'cheese'];
print(type(things[1][2][2]))
# this way we will print the type of the g in the 3rd egg -> str
#What if we want to change this element?
#things[1][2][2] = 'o'
#-> we can not do that because string is immutable

#Lists contain references to elements:
coffee,milk,cappuccino =  'coffee','milk','cappuccino'
#example of multiple assignment (also called unpacking),
# where you're assigning values to multiple variables in a single statement.

my_shopping_cart= [coffee,milk,cappuccino]
your_shopping_cart = [cappuccino,milk,coffee]

print(my_shopping_cart[0]==your_shopping_cart[2])
print(my_shopping_cart[0] is your_shopping_cart[2])

#What does 'is' in Python?
#is checks identity, not equality. It returns True if both variables point to the same object, and False otherwise.
#To check if two objects have the same value, use the == operator instead of is.

#optimization
room_1 = 10000
room_2 = 10000
print(room_1 == room_2)
print(room_1 is room_2)

#here it is not optimized
room_1 = [10000]
room_2 = [10000]

print(room_1 == room_2)  # True, because the lists have the same value
print(room_1 is room_2)  # False, because they are different objects



fruits = ['apple','banana','cherry']
fruits.append('pear')
print(fruits[-1])
fruits.append(fruits)#we can append the list to itself
print(fruits[-1])
print(fruits[-1] is fruits)

genres = ['pop','rock','jazz']
instruments = ['guitar','piano','violin']

music = [genres,instruments]
print(music[1][2])
music[1][2] = 'drums'
print(music[1][2])# we can change elements in lists but not in tuples

music[1][2] = ['drums','gaida','saxophone']
print(instruments)# we can change elements of the list that is inside other list

#What if elements was a tuple?

genres = ['pop','rock','jazz']
#instruments = ('guitar','piano','violin')

music = (genres,instruments)
music[1][2] = ('drums','gaida','saxophone')
print(instruments)# we can change elements of the list that is inside tuple
#This means we do not change the tuple but the list inside it which can be done bc the lists are immutable
#But if "instruments" was a tuple this could not be done

