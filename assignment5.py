#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a python function to calculate the factorial of the non negetive integer and the function take the number as an argument
def factorial(num):
    if num == 0:
        return 1
    if num > 0:
        result = num * factorial(num - 1)
        return result

num = int(input("Enter a Non-Negative-Integer Number:"))

if num >= 0:
    result = factorial(num)
    print("The Factorial of input Number is: ",result)
else:
    print("You enter a Wrong Number. Enter a non negetive number")


# In[21]:


#Write a python function that accepts a string and calculate the number of upper case and lower case letter
def upperlower(strings):
    upperstr = 0
    lowerstr = 0
    for string in strings:
        if string.isupper() == True:
            upperstr += 1
        elif string.islower() == True:
            lowerstr += 1
    print(f"Your Entered Strings has {upperstr} upper characters and {lowerstr} lower characters")
strings = input("Enter any String: ")
upperlower(strings)


# In[52]:


#Write a python function to print even number from a given list
def even(lists):
    Even = []
    for check in lists:
        if check % 2 == 0:
            Even.append(check)
    print(f"The Even Number in your defined list:\n{Even}")
lists = [12,22,17,1,13,5,7]
even(lists)


# In[56]:


#Write a Python function that checks whether a passed string is palindrome or not.
w = input("Enter any word: ")
palindrome = ""
for letter in w[-1::-1].lower():
    palindrome = palindrome + letter
if palindrome == w.lower():
    print(f"Your Entered words \"{w}\" are Palindrome")
else:
    print(f"Your Entered words {w} are not Palindrome")


# In[58]:


#Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime(num):
    count=0
    for i in range(1,num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num,"is a prime number!")
    else:
        print(num,"is not a prime number!")
        
num = int(input("Enter a number: "))
prime(num)


# In[60]:


#Write a function which accepts the multiple arguments of user shopping list andprint all the items which user bought from market.
def items(*item):
    print("The Customer Shopping's list are: ")
    for value in item:
        print(value)
items("Vegetables", "Clothes", "Acessories","Breads")


# In[ ]:




