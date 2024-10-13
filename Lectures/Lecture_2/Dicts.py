

#First of all, dicts are MUTABLE
#Each item of a dictionary consists of a key and its associated value (KEY - VALUE)
#Keys must be unique and immutable(strings,tuples,numbers) -> KEYS - IMMUTABLE
#Values may be of any type and can be changed -> VALUES - ANY TYPE
#!!!The order is not guaranteed

#Example:
students_names = {
    'Asen':'Krasimirov',
    'Yoana':'Mateva',
    'Monika':'Angelova',
    'Ralitsa':'Taneva'
}

print('Asen\'s last name is',students_names['Asen'])
students_names['Asen'] = 'Svetoslavov'
print('Asen\'s last name is',students_names['Asen'])

#print(students_names[1])->this can not be done
print(students_names.values())#->prints the values
print(students_names.keys())#->prints the keys

#Is the dict unordered?
grades_by_courses = {
    'OOP':5,
    'Intro to programming':5,
    'OIS':4
}

#adding more keys-values
grades_by_courses['Algebra'] = 5
grades_by_courses['Operations research'] = 6

print('Algebra' in grades_by_courses) #checks if the course is in the dict
print(grades_by_courses.get('DIS'))# -> prints None bc the key is not existing
print(grades_by_courses.get('DIS',3))
print(grades_by_courses.get('DIS'))# -> here it still prints out None bc the last operations has not added it in the dictionary

#Three another ways to create a dictionary:

# №1: (named parameters in the constructor)

capitals = dict(France =  'Paris',Italy = 'Rome')
print(capitals)
print(capitals['Italy'])

# №2: (list of pairs)

starbucks_locations = dict([('Gen.Gurko',10),('National theatre',5)])
print(starbucks_locations['Gen.Gurko'])

# №3: list of keys and values y default

smth = dict.fromkeys([1,2,3],'Unknown')
print(smth)

