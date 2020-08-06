print("Hello World!")
# type() returns the type of variable we are dealing with
# returns the actual type the compiler is interpretting it by

# variables are a way to store a value under a specific location and do what we want with it
# - can store multiple values, arrays, dictionaries, entire objects
# integers - whole numbers, floats - decimals , booleans - true/false, strings - string of characters within single or double quotes

# name 
# name = value

# type is automatically inferred in python

numberOfFriends = 10

# in python, we tend to use underscores i.e. number_of_friends

print(numberOfFriends)
print(type(numberOfFriends))

# common use of float variables is with money
paycheck = 789.53
print(type(paycheck))
print(paycheck)

paycheck = 789
print(paycheck)
print(type(paycheck))
# type can change depending on the type of variable
# this is int as the decimal was removed

# Booleans - can only hold true or False
isDoorOpen = False
isDoorOpen = 5 > 2
print(isDoorOpen)
print(type(isDoorOpen))

# Strings encompass the widest range of water
# it is anything we want so long as it is between single or double quotes
# it is a bunch of characters strung together
# string of 15 and value of 15 are different type of variables

firstName = "Kathleen"
print(firstName)
print(type(firstName))

# the value of none - similar to null or nil in other languages, has no value at this point in time 

first_name = None
print (first_name)
print(type(first_name))

# Assignment, Arithmetic and Conditional Operations

# Assignment - the equal single
# takes a variable on the left and takes in a value

# The Not Operator - makes things the opposite
isDoorClosed = not isDoorOpen
print(isDoorOpen)
print(isDoorClosed)

bank_balance = paycheck + 1000
print(bank_balance)
print(type(bank_balance))

# Gives the remainder
print(5%2)

# Discards the remainder and gives the value 
print(5//2)

numberOfFriends += 10
print(numberOfFriends)

print(5 != 2)

print("a" > "b")
# The way string comparisons work, if one is alphabetically greater(comes later in the alphabet, it is considered greater. a is less than b)


# Can add strings together
# string concatenation
fullName = firstName + " " + "Wong"
print(fullName)

year = 2020
print(type(year))
year = "2020"
print(type(year))
# can take the same variable and reassign it into a string
# anything can be converted into a string, not the other way around

print(int(bank_balance))
# this drops the decimal number here
# can tell the compiler you want a float vs an integers

print(float(year))

print(str(bank_balance))

# Can Convert to int, float and str ; cannot convert these to str

# Collections - tuples, lists and dictionaries

# Collections - ways to store multiple values in a single location
# important as it allows for extra functionality than we can perform on single value variables
# - cannot modify the individual values within tuples
# - we have full range on lists

# Dictionary - maps, stores a list of values under certain keys

# Tuples 

# tuples - tend to have less values than lists

full_name = ("Kathleen", "Wong")
print(full_name)
other_full_name = ("Rawr", "Here")
print(full_name)
# if we print multiple string values, it will print out quotes

inventory_item = ("apples", 5)
print(inventory_item)

# Lists - quite similar to tuples
# - some of the operations performed on lists cannot be performed on tuples
# - tuples are more static in the way they are stored
# - lists use square brackets; tuples use parenthesis

roster = ["Bob", "Roxas", "Sora", "Kevin"]
print(roster)

# Dictionary 
# - map values in dictionary to certain keys
# - each of the elements in an array are distinct values
# - uses curly braces
# - needs to be stored under a key
# prints all key and value pairs
# if we do not know the index of an element, we can access it by its key

inventory = {"apple": 5, "knife": 1, "shoes": 2}
print(inventory)

print(full_name[0])

print(roster[1:3])
# prints everything from index 1 to 3

print(roster[3:])
# prints everything index 3 and after

print(inventory["shoes"])
# prints out the index the key is located at

# Modifying elements
# retrieve attributes from tuples
# we can add two tuples together

full_names = full_name + other_full_name
print(full_names)

# del full_names - deletes value
print(full_names)

# print length, min and max
print(len(full_name))
print(min(full_name))
print(max(full_name))

# Array Operations

roster[1] = "Adam"
print(roster)

roster[2] = 10
print(roster)

# del roster[0]
# print(roster)

# roster.clear()
# this deletes the entire roster
# removed_value = roster.pop(0)
# print(removed_value)

roster.append("Kathleen")
print(roster)
# append adds another value

print(max(inventory.values()))
# returns all key value pairs as tuples

inventory["knife"] = 5
print(inventory)
# changes the value of knife to 5

# Control Flow Intro 
# allows us to make decisions in our code based on the outcome of certain tests
# execute only certain parameters of the code based on the text 

# if condition to test: 
#     code to execute if test passes or evaluates to true

bank_balance = 200.00
item_cost = 250.00
item_inventory = 1

isBalanceEnough = True

if item_cost < bank_balance and item_inventory >= 1:
    bank_balance -= item_cost
    print("transaction successful")
    print(bank_balance)
elif item_cost == bank_balance and item_inventory >=1:
    bank_balance -= item_cost
    print("transaction successful, but no funds left")
    print(bank_balance)
else:
    if item_inventory < 1:
        print("not enough inventory")
    else: print("transaction failed, insufficient funds")
    print(bank_balance)



# While and For Loops
# allows us to execute loops numerous times without having to call them over again

# while condition:
#     execute code as long as condition is still true


total = 0
index = 1
while index <= 10:
    total += index
    index += 1
    if index > 10:
        break

    # break is the opposite of the continue statement
    # break ends the loop and moves on to the rest of the code
    # continue continues the loop and skips the current index

# For Each Loops
# iterating through arrays
for name in roster:
    print(name)
# we never go out of bounds and we can iterate through the entire array
# cannot pick and choose which element, has to go through the entire array

for i in range(3):
    print(roster[i])

# Functions, parameters, return values

# function - way to store a statement so we can call upon it when needed

# This code will not run until it is called upon
# def name(parameters):
#     function body, code to execute

#     return statements 

starting_position = 5

# def move_player(by_amount):
#     global position
#     position += by_amount

# def move_player(by_amount):
#     global starting_position
#     position = starting_position + by_amount
#     return position

def move_player(current_position, by_amount):
    return current_position + by_amount

print(starting_position)
new_position = move_player(6)
print(starting_position)
new_position = move_player(-3)
print(starting_position)
print("difference between start and end is", starting_position - new_position)


# Classes and Objects
# classes - blueprint of an object
# code representation of state and behavior

# object - anything that has statement behavior within our code
# relate it to a real world entity

class gameCharacter:
    # attributes here - stored as variables, numbers strings booleans dictionaries objects
    name = ' '
    health points = 100
    position = 0
    # initializer - ways to create new instances of classes
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # behaviors - defined through functions/methods that exist within a class
def move_by(self, amount):
    self.position += amount

def heal_self(self, by_amount):
    self.health += by_amount
    if self.health > 100:
        self.health = 100

# create a new instance of this class 

new_character = gameCharacter("Kathleen", 10)
print(new_character)
print(new_character.name)
print(new_character.health)
print(new_character.position)

new_character.move_by(10)
print(new_character.position)
new_character.health = 100
new_character.heal_self(40)
print(new_character.health)