# Introduction to python
 All queries from the Introduction to python course

Assignemt 6

 # Q1 - write a function named circle_s(r) that gets a radius as an argument and returns the surface of the circle with radius r. use pi constant from math module and pow function (don't forget to import this model before the function)

import math
def circle_s(r):
    surface = math.pi * pow(r, 2)
    return surface

# Q2 - Write a function named log_of_list(lst1) with one argument lst1 - a list with positive numbers. The function returns the list of natural log of the lst1 numbers formatted to float with 2 decimal places. 

import math
def log_of_list(lst1):
    base = math.e
    lst2 = [str("%.2f" % round(math.log(elem, base), 2)) for elem in lst1 if float(elem) >= 0]
    return lst2

# Q3 - You are given a text file, this file contains a nucleotide sequence. Nucleotide sequence is a sequence of 4 letters 'A', 'T', 'C', 'G'. The first line in the file is a header - information about the organism. The first line does not contain the nucleotide sequence. The sequence starts from the second line. Each line contains the same number of nucleotides. The example of this file is attached to the exercise. Write a function called nuc_freq(file_name) that opens the file for reading and checks how many of each nucleotides ('A', 'T', 'C', 'G') are in this genetic sequence. The function will return the most frequent nucleotide of the sequence. suppose there is one most frequent nucleotide. Write another function called dna_2_rna(file_name) that translates the genetic code from the file to rna code. The translation is done by the following rules: 'A' is translated to 'A', 'C' is translated to 'C', 'G' is translated to 'G' and 'T' is translated to 'U'.  The function will return the number of 'U's in the rna code. *for both functions suppose that the file is in the same folder with the python functions (so you can open it by it's name)

def nuc_freq(name_of_file):
    f = open(name_of_file, 'r')
    freq_dict = {}
    f.readline()
    for line in f:
        for letter in line:
            freq_dict[letter] = freq_dict.get(letter, 0) + 1 
    f.close()
    sorted_dict = sorted(freq_dict.keys(), key = freq_dict.get, reverse = True)
    return sorted_dict[0]
    
    
def dna_2_rna(name_of_file):
    f2 = open(name_of_file, 'r')
    f3 = open('ex7_ques3_rna.txt', 'w')
    counter = 0
    f2.readline()
    for line in f2:
        for char in line:
            if char != "T":
                f3.write(char)
            else:
                f3.write("U")
                counter+=1
    f2.close()
    return counter

