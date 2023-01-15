# Introduction to python
# All queries from the Introduction to python course

# Assignment 5

# Q1 - implement a function is_sub_group that has two list arguments, checks if one of the list arguments is sub group of the other, if so returns True and the union list with unique elements.  else returns False and the union list with unique elements. the function returns two different variables. 

def is_sub_group(lst1,lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return(set1.issubset(set2) or set2.issubset(set1), sorted(set1.union(set2)))

# Q2 - A student at python course in MIT wrote a function that receives 3 arguments - list, a variable of not known type and an integer. The function inserts the second argument (var with not known type)  in the given list for each index that is equal to the third argument or divisible by it.  After applying this function on a given list, he noticed that this list was changed. Help him to change the code to preserve the original list. The updated function will return the original list and the changed list.

def append_at_index(lst1, var1, n):
    new_list = []
    for i, item in enumerate(lst1):
        if i % n != 0:
            new_list.append(item)
        else:
            new_list.append(var1)
    return (lst1, new_list)
    

# Q3 - Write a function called second_most_popular_character which receives a string and returns the second most popular letter in this string. In case there is more than one such letter, you need to return the smallest among them (in the alphabetic order). no case sensitivity. 

def second_most_popular_character(text):
    lower_text = str.lower(text)
    count_dict = {}
    for char in lower_text: # lower caps
        count_dict[char] = count_dict.get(char, 0) + 1 # counting each letter's appearance 
    sorted_letters_by_counter = sorted(count_dict.keys(), key = count_dict.get, reverse = True) # sorting the keys by their values
    for i, letter1 in enumerate(sorted_letters_by_counter[:-1]):
        if count_dict[letter1] == count_dict[sorted_letters_by_counter[i+1]]: # We want the second most popular letter
            continue # It continues until we'll get the secound most popular letter
        else:
            break
    same_value = []
    for j, letter2 in enumerate(sorted_letters_by_counter[i+1:-1]): # we need to start a new loop in the position of the secound most popular letter, and see if it's value appears again
        if count_dict[letter2] == count_dict[sorted_letters_by_counter[i+1+j+1]]:
            same_value.append(letter2)
            same_value.append(sorted_letters_by_counter[i+1+j+1])             
            continue
        else:
            same_value.append(letter2)
            break    
    sorted_list_by_alphabetical_order = sorted(same_value)
    return (sorted_list_by_alphabetical_order[0])



