# Introduction to python
#All queries from the Introduction to python course

# Assignment 2

# Q1 - The code receives from user a number (this part is already done - don't touch). you want to complete the code to get the following output in variable res: if the number that is received between 0 and 3 (included)  the code will return 2. if the number that is received between 4 and 7 (included) the code will receive 3. if the number that is received between 8 and 15 (included) the code will receive 4. in all other cases it will return a string "out of memory"

num = input("enter your number: ")
res = "out of memory"
if 0 < int(num) <= 3:
    res = 2
elif 4 < int(num) <= 7:
    res = 3
elif 8 < int(num) <= 15:
    res = 4

# Q2 - The following code is receiving a string from user and stores it in variable string_to_check. You need to complete the code so that it stores in variable res a Boolean value - true if the input string is palindrome and false if its not a palindrome.

string_to_check = input("string: ")
res = True
if string_to_check != string_to_check[::-1]:
    res = False

# Q3 - This code is supposed to count dots (.) in a given string. But it has few bugs in it. Fix the bugs to get the right code and right output.

str_in = input("enter a string: ") #this is built in line - please don't erase/change
dots = 0
i = 0
while i < len(str_in):
    if str_in[i] != ".":
        i+=1
        continue
    dots+=1 
    i+=1

# Q4 - The following code receives from user some grades on coursers that he took in previous semester and their weights (נ"ז). when user is done he will type "done" instead the grade. you need to complete the missing parts in the answer window to get the code that compute weighted average and store it in variable res rounded to hundredths. *weighted average = sum(grade*points)/sum(points). some important notices: assume the grades and points are integer values. the input of first grade and its points is written already for you. please don't change it, just add the rest of the code below. the input messages for the next grades  must be the same as the input message for the first grade and points input (see the example)

grade = input("enter your grade: ")
points = input("enter the points: ")
sum1 = int(grade) * int(points)
total_points = int(points)
#write a while loop that terminates when the user enters "done" to grade variable
while grade != "done":
    grade = input("enter your grade: ")
    if grade == "done":
        break
    else: 
        points = input("enter the points: ")
        sum1 = sum1 + int(grade) * int(points)
        total_points = total_points + int(points)
#calculate the grade to variable res in this format XX.XX
res = "%.2f"%(sum1 / total_points)

# Q5 - One way to compute square roots is Newton's method. suppose that you want to know the square root of a. if you start with almost any estimate, x, you can compute a better estimate with the following formula: y = (x+a/x)/2.
# for example if a =4 and we start from x = 3 --> y = (x+a/x)/2 = 2.1666 that is closer to square root of 4 than the initial value x =3. if we repeat, with new estimate it gets even closer:
# x = y
# y = (x+a/x)/2 
# print y 
# 2.006
# implement this algorithm in python using while loop, which will terminate when the estimation y is close enough to real square root of  a, in the meaning of absolute error :
# |y**2 - a| <0.005 (|      | is absolute value)
# x and a are input from user (given already in the answer window). the code will save the estimated square root in variable newtons_square_root. and the number of iterations that it used in number_of_iterations. and the error value |y**2 - a| in variable err

a = int(input("enter the value for squared root calculation: "))
x = int(input("enter your initial guess for squared root of " + str(a) + ": "))
y = (x + (a / x)) / 2 
number_of_iterations = 1
while float(abs(y**2 - a)) > 0.005:
    x = y
    y = (x + (a / x)) / 2
    number_of_iterations+=1
newtons_square_root = "{0:.2f}".format(y)
err = "{0:.2f}".format(float(abs(y**2 - a)))