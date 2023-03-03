#!/usr/bin/env python
# coding: utf-8

# In[4]:


x = "bilal" 
y = "Mazhar" 


# In[5]:


print(x)
print(y)


# In[6]:


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# In[7]:


counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Bilal Mazhar"   # Creates a string variable

print (counter)
print (miles)
print (name)


# In[12]:


x = str(3)    # x will become string :  '3'
y = int(3)    # y will become int 3
z = float(3)  # z will become flost: 3.0 


# In[13]:


x = 10 
y = "bilal Mazhar"

print(type(x))
print(type(z))


# In[18]:


x = 10 
y = 10 
print ("Addition") 
print (x+y)   # Addtion 
print ("Subtraction") 
print(x-y)    # Subtraction
print ("Multiply") 
print(x*y)    # Multiply
print ("division") 
print (x/y)   # division 


# In[19]:


x = 5
y = 3

print(x == y)     # Equal 
print(x != y)     # Not equal
print(x > y)      # Greater than
print(x < y)      # Less than
print(x >= y)     # Greater than or equal to
print(x <= y)     # Less than or equal to


# In[24]:


# List 
thislist = ["apple", "banana", "cherry"]
print(thislist) 
# List Length
print(len(thislist))
# Data Type
print(type(thislist))


# In[30]:


# Accessing the lists 

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#Range of Indexes
print(thislist[2:5])
#By leaving out the start value, the range will start at the first item:
print(thislist[:4])
#This example returns the items from "cherry" to the end:
print(thislist[2:])
#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
      print("Yes, 'apple' is in the fruits list") 
#adding the new item in index
thislist[1] = "Bilal Mazhar"
print (thislist)


# In[34]:


# Tuples 

thistuple = ("apple", "banana", "cherry")
print(thistuple)
# length 
print(len(thistuple))
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#From Python's perspective, tuples are defined as objects with the data type 'tuple':
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


# In[36]:


# Python Conditions and If statements
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif b == a: 
    print("b is equal to a")
elif b < a:
    print("b is less a")
elif b <= a:
    print("b is greater than or equal to  a")
elif b >= a:
    print("b is less than or equal to  a")


# In[41]:


# Python has two primitive loop commands:
    # while loops
    #for loops
i = 1
while i < 6:
    print(i)
    i += 1


# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# In[42]:


#loops 

name = ["Bilal", "Mazhar", "DevOps_Bootcamp"]
for x in name:
      print(x)


# In[44]:


# Even strings are iterable objects, they contain a sequence of characters:
for x in "bilal_Mazhar_DevSecOps":
      print(x)


# In[46]:


# Function
def my_function():
      print("Hello from a Bilal Mazhar") 


# In[47]:


my_function()


# In[49]:


def my_function(fname):
  print(fname + " DevOps")

my_function("Bilal")
my_function("BootCamp")
my_function("2023")


# In[50]:


def my_function(fname, lname):
 print(fname + " " + lname)

my_function("Bilal", "Mazhar") 


# In[51]:


def my_function(country = "Norway"):
        print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# In[ ]:


# Project 1 
# Create a game where the computer chooses a random number between 1 and 100 and the user has to guess the number. The computer should provide feedback if the user's guess is too high or too low until the user guesses the correct number.

import random

def guess_number():
    number = random.randint(1, 100)
    guess = int(input("Guess the number between 1 and 100: "))
    while guess != number:
        if guess > number:
            print("Too high!")
        else:
            print("Too low!")
        guess = int(input("Guess again: "))
    print("Congratulations! You guessed the number!")

guess_number()


# In[ ]:


# Project 2 
# Create a program that takes a sentence as input and returns the number of words in the sentence.
def word_count(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter a sentence: ")
count = word_count(sentence)
print("The sentence has", count, "words.")


# In[ ]:


# Project 3 

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# Main program
print("Welcome to the Python Calculator!")
print("Please select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user input
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform selected operation
if choice == '1':
    result = add(num1, num2)
    print(num1, "+", num2, "=", result)
elif choice == '2':
    result = subtract(num1, num2)
    print(num1, "-", num2, "=", result)
elif choice == '3':
    result = multiply(num1, num2)
    print(num1, "*", num2, "=", result)
elif choice == '4':
    result = divide(num1, num2)
    print(num1, "/", num2, "=", result)
else:
    print("Invalid input")


# In[ ]:




