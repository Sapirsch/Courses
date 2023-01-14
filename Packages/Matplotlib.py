# Matplotlib assignment


# Q1 - Display the grades of the students from the file csv.StudentsGrades as a 2dline graph where the x-axis is the different subjects and the y-axis is the grades in these subjects. Choose a total of 4 students (4 lines on the graph). Add an appropriate title to the graph. Add labels xticks of the subjects. Set the thickness of the line to be 3. Define different markers for each graph.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsGrades.csv')
df_no_names = df.drop('Name', 1)

yael_row = df_no_names.loc[0,:]
yael_data = np.array(yael_row)

noga_row = df_no_names.loc[1,:]
noga_data = np.array(noga_row)

michal_row = df_no_names.loc[2,:]
michal_data = np.array(michal_row)

david_row = df_no_names.loc[3,:]
david_data = np.array(david_row)

plt.plot(yael_data, c = "Black", ls = '--', marker = "1", label = 'Yael', linewidth = 3.0)
plt.plot(noga_data, c = "Red", ls = 'solid', marker = "o", label = 'Noga', linewidth = 3.0)
plt.plot(michal_data, c = "Green", ls = '-', marker = ",", label = 'Michal', linewidth = 3.0)
plt.plot(david_data, c = "Blue", ls = '-.', marker = "^", label = 'davod', linewidth = 3.0)

plt.xticks(list(range(7)), df.columns.tolist()[1:], rotation = 'vertical')
plt.legend(loc = 'upper left', bbox_to_anchor = (1,1))
plt.title('Grades')
plt.show()


# Q2 - A student stays a year if he fails two or more subjects. Based on the information that appears in the csv.StudentsGrades file. Build a piechart that describes how many students stay one year and how many moved to the next year

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsGrades.csv', index_col='Name')
#df_no_names = df.drop('Name', 1)

students_number_of_fails = df[df < 60].count(axis = 1).tolist()
students_fail_counter = 0
for students_fails in students_number_of_fails:
    if students_fails >= 2:
        students_fail_counter+=1

students_pass_counter = len(df) - students_fail_counter

fig = plt.figure()
ax = fig.add_subplot(111)
sizes = [students_fail_counter, students_pass_counter]
labels = ('fail', 'pass')
ax.pie(sizes, labels = labels)

# Q3 - Draw 20 points randomly from the standard normal distribution. Save them in the variable x which is of type numpy. Build a figure with two subplots. Define y to be 8+2*x. Save the scatter plot of x and y in subplot1. Define Z to be sqrt(8 - x**2), and save the scatter of x and y in subplot2. Is it possible to define the algebraic relationship from the graphs?

import numpy as np
import matplotlib.pyplot as plt
    
x = np.random.randn(20)
y = x * 2 + 8
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.scatter(x,y)

z = 8 - x**2
ax2 = fig.add_subplot(122)
ax2.scatter(x,z)




