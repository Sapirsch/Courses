# Introduction to python
 All queries from the Introduction to python course

# Assignment 3

# Q1 - Given a list called A containing positive integers, and given a positive integer a, assign variable res with the index of the first number in the list which is divisible by a. If there is no such number, print -1. You can assume . that a is different from 0, but A could also be an empty list.

#the following lines are used to get an input from user. do not change them
a = int(input("integer: "))
res = -1
for i in A:
    if int(i) % a == 0:
        res = A.index(i)
        break

# Q2 - Given a list of strings (variables of type str) called B, find the average length of the strings in the list. nd print the number of strings whose length is strictly greater than the average length. Do this both with a while loop and with a for loop. You can assume that the list B contains at least one string.

#suppose that B is given - you don't need to assign it
lengths = [len(word) for word in B]
ave_size = sum(lengths) // len(lengths)
counter_for_loop = 0
for item in B:
    if len(item) > ave_size:
        counter_for_loop+=1
print(f"The number of strings longer than the average is: {counter_for_loop}")
i = 0
lengths_while = 0
while i < len(B):
    lengths_while = lengths_while + len(B[i])
    i+=1
ave_size_while = lengths_while // len(B)
ind = 0
counter_while_loop = 0
while ind < len(B):
    if len(B[ind]) > ave_size:
        counter_while_loop+=1
    ind+=1
print(f"The number of strings longer than the average is: {counter_while_loop}")
        


# Q3 - Given a list of numbers called C, write a piece of code that prints the sum of the product of each pair of adjacent numbers in the list.

# suppose the list C is defined - don't assign C in your code
prev = 0
sum_adjacent = 0
for item in C:
    new = int(item) * prev
    sum_adjacent+=new
    prev = int(item)
print(sum_adjacent)


# Q4 - You are given a list of integers C. Use this list to make another list res_list that every element of it is absolute value of each element in C.

res_list = [abs(int(item)) for item in C]

# Q5 - You are given a list of items C. Use this list to create another list res_list that contains only the C items that are integers. 

res_list = [item for item in C if str(item).isdigit()]

# Q6 - sort the given list C in a descending order of absolute values of its items and save the sorted list in res_list.

res_list = sorted(C, reverse = True, key = abs)

# Q7 - Ask user to enter a string using input() function (argument must be "enter your str: "). Split the string by spaces separator and store it as a list. For every item in this list check if the item is numeric and if so calculate the sum of the numbers. Store this information in another list and sort it based on the value of sum. If the item is not numeric drop it.

#input from user - don't change this 
str_in = input("enter your str: ")
list_in = str_in.split()
w = [item for item in list_in if item.isdigit()]
res = []
for num in w:
    sum_digits = 0
    for digit in num:
        sum_digits += int(digit)
    res.append(sum_digits)
res = sorted(res)


# Q8 - You are given 3 lists A, B, C. Assume that they are defined before and create a new list that will be the concatenation of these 3 lists.

A.extend(B)
A.extend(C)
print(A)