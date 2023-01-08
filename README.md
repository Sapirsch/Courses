# Introduction to python
 All queries from the Introduction to python course

# Assignment 4

# Q1 - implement a function called sum_of_mult_of_adjacent(lst1) that receives a list lst1 as an argument and returns the sum of the product of each pair of adjacent numbers in the list.

def sum_of_mult_of_adjacent(lst1):
    sum_of_adjacent_numbers = 0
    for i, elem in enumerate(lst1[:-1]):
        sum_of_adjacent_numbers+= (elem * lst1[i+1])
    return sum_of_adjacent_numbers

# Q2 - Implement a function called sum_divisible_by_k which receives 2 arguments: a list of numbers called lst and a positive number k which default value is 1, and returns the sum of all numbers in the list that are divisible by k. If there is no number divisible by k (for example when the list is empty), you will return 0.

def sum_divisible_by_k(lst, k=1):
    sum_of_numbers = 0
    for number in lst:
        if number % k == 0:
            sum_of_numbers += number
    return sum_of_numbers


# Q3 - Implement a function parallel_vec(lst1, lst2) with 2 arguments lst1 lst2 that are list of length n, that represent two vectors, the function will return True if the vectors are parallel , else False. defenition. two vectors  v1=(n1,n2,n3) v2=(k1,k2,k3) are parallel vectors if the ratio between all components is the same:  n1/k1 = n2/k2 = n3/k3

def parallel_vec(lst1, lst2):
    previous_devision = lst1[0] / lst2[0]
    for i,j in zip(lst1, lst2):
        if i / j != previous_devision:
            return False
            break
    return True
        
# Q4 - Implement a function called mult_odd_digits(n) which receives a positive integer n and returns the product of its digits that are odd. If there are no odd digits, return 1.

def mult_odd_digits(n):
    multiplication_of_odd_digits = 1
    str_n = str(n)
    for digit in str_n:
        if int(digit) % 2 == 1:
            multiplication_of_odd_digits *= int(digit)
    return multiplication_of_odd_digits


# Q5 - mplement function sort_by_n_char(lst1, n) that receives a list lst1 and an int n and returns sorted lst1 by the n-th character of each string in lst1.

def sort_by_n_char(lst1, n):
    res = sorted(lst1, key = lambda x : x[n])
    return res

    