# Remember these three terms:
# - Ordered: items have a defined sequence or position.
# - Mutable: you can change the object after creating it.
# - Duplicate: the same value appears more than once.

# 01 :--- Strings (str)

# A string is a sequence of characters used to represent text.

name = "shivam"
message = 'Hello, python!'
multiline = """ My name is 
                Shivam Barpete"""

print(name)
print(message)
print(multiline)


#====================================================================================================================

# indexing 

word = "ymmi"
print(word[0])
print(word[1])
print(word[2])
print(word[3])

#====================================================================================================================

# slicing 

# ?slicing extracts a portion of a string

# syntax : string[start : stop : step]
#   the stop index is excluded 

word1 = "shivambarpete"
print(word1[0:3])
print(word1[::2])

#====================================================================================================================

#important string methods 
text = "  shivam  barpete  "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("shivam", "barpete"))
print(text.strip().split())
print("shivam".capitalize())

print("python".startswith("py"))  # True
print("hello world".find("world")) # 6
print("banana".count("a"))         # 3
print("123".isdigit())             # True

#====================================================================================================================

#String are immutable

word2 = "Python"
# word2[0] = 'j'// it have erro because string is immutable 

word2 = 'J' + word[1:]
print(word2)

#====================================================================================================================
# sting formatting with f-string 

thisName = "shivam1411"
thisAge = 23
print(f"My name is {thisName} and my age is {thisAge}")

#====================================================================================================================


#LIST (list)

# A list stores multiple items in a single variable. Lists are ordered, mutable, and allow duplicates.

fruits = ["apple", "banana", "mango"]

print(fruits[0])  # apple
print(fruits[2])  # mango

data = ["Shivam", 25, True, 5.8]

print(data[0])
print(data[1])

fruits[1] = "orange"
fruits.append("grapes")
fruits.extend([4,5])
fruits.insert(0,"the")
fruits.remove(4)
fruits.pop()
fruits.reverse()
fruits.sort()
fruits.index("the")
fruits.count("apple")
fruits.clear()

print(fruits)

#====================================================================================================================

# List slicing 
number = [10,20,40,560]
print(number[1:4])
print(number[-2])

#====================================================================================================================

# Copying lists: a common beginner mistake
a = [1, 2, 3]
b = a

b.append(4)

print(a)  # [1, 2, 3, 4]

#====================================================================================================================


# Tuples (tuple)
# A tuple is an ordered collection that cannot be modified after creation.
tuplee = (10,23,3,3,33)
user = ("Shivam", 25, "Developer")

name, age, role = user

print(name)  # Shivam
print(age)   # 25
print(role)  # Developer

#====================================================================================================================

# Sets(set)
# A set is a mutable collection of unique elements. It is useful when you need to eliminate duplicates or compare groups of items.
numbers = {10, 20, 10, 30, 20}

print(numbers)  # {10, 20, 30}



#====================================================================================================================
# Dictionaries (dict)

# A dictionary stores data as key-value pairs. It is one of the most important Python data structures for backend development and AI applications.

user = {
    "name": "Shivam",
    "age": 25,
    "role": "Developer"
}

print(user["name"])  # Shivam
print(user["age"])   # 25
print(user["role"])


user["city"] = "bhopal"

print(user)

print(user.keys())
print(user.values())
print(user.items())
print(user.get("age"))


# Nested dictionaries
student = {
    "name": "Shivam",
    "skills": ["Python", "JavaScript", "React"],
    "address": {
        "city": "Indore",
        "country": "India"
    }
}

print(student["skills"][0])          # Python
print(student["address"]["city"])    # Indore







