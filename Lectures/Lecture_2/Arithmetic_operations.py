
#What is none?
x = None
type(x)
print(x)

# Some operations and what will be the result from them?

print(3/2) #this division will not remove the digits after the comma -> 1,5
print(3//2)# this division will rome the digits -> 1
print(0.1 + 0.2) # -> 0,300000...004
#0.1 is stored as something like 0.1000000000000000055511151231257827021181583404541015625.
#0.2 is stored as something like 0.200000000000000011102230246251565404236316680908203125.
# Adding these approximations together results in 0.30000...4
#The result of 0.1 + 0.2 in Python is 0.30000000000000004 because of how floating-point numbers are represented in binary,
# causing small precision errors. This behavior is common across most programming languages that use floating-point arithmetic.
# You can mitigate this by rounding the result or using Python's decimal module for higher precision when needed.
print(0.1+0.1) # 0.2
print(0.3/3)
