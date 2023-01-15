# Introduction to python
#All queries from the Introduction to python course

# Assignment 1

# Q1 - Assign variable with name varName to be the string: "happy to learn python" . save half of the string (including the middle char) to another variable called resultVar.

varName = "happy to learn python"
#write the rest here:
length = len(varName)
half = -(-length//2)
resultVar = varName[:half]

# Q2 - StrInput stores input from user. write a code that stores in variable res a substring of strInput that does not include first 3 characters and the last 3 characters.

strInput = input("your string: ")
#your code here: 
res = strInput[3:-3]

# Q3 - Assign : p_val = 0.000003345. assign p_val_sci variable with the p_value but in a scientific form using 2 decimal places. Use string formatting syntax: "{:.<number of decimal places>e}".format(p_val)

p_val = 0.000003345
p_val_sci = "{0:.2e}".format(p_val)

# Q4 - Read an input from user to variable user_input. replace all the spaces in this input using string built in method "replace" with the string "!space!". Save the result to res

user_input = input('your string with spaces please: ')
res = str.replace(user_input, " ", "!space!")

# Q5 - The amino acid sequence is given in variable input_seq. you need to split this sequence using "VV" separator. save the result to variable res, don't forget to use str() function to turn your output to string.

input_seq = "MSIHRITRHHATPARPSALRFSWEVLFSWRVVLFSWRVLFSWRALFAWGALLSPVVDAAPMPVVAPAPAAVAPAPLQYYALTEDDLRTLTVVERNAIQSQLDALAGYQFTSLVALNNAVVRPLIRQLPGTQPRPNEEEQILRRIVDVVPISDGLAHRASPSRSSIPGGNSTAGIQERARDANPRPDDEAGTPAAYSLNQPALEQWYQTLNLVAPDKETLARLSRLNPQDRQRIEAVARKNGVPTLAAAPMVWRAPADCGCEDSTPNINGDDATFYGFYPYWQPLAEGQTLNFRQLDRIGYFSAAIVPATRGPQLVLPPNWRENRPYSDFIRLAHRYRTAIDLVVSSPRALSPSTLAGLFTPSLVAQLSNSVQTPLDGWANRAKPWLTFGISTRDTMADGVTLDNLQALLPYIDRFILQSDTPDGAGESRRTRDQLSDLRQFLSQQPQTDVAGLYRKMVPVLITDANRRQTTELTELVRYSSWSFLSAAYWPLPLDDASQQLISRTYYPVASLPTPLAQLVSAANAVIDVVCPNRWVLRLILFITFWGIVVTGVVSLWLFPVRKVTESLWFAGFVVLFAATLMLALVADPYWQQYQTLILLLFAAVVAITVLQRLRKTRRERNP"
res = str(input_seq.split("VV"))

# Q6 - Assign the variable named strVar with the string "hello hello my name is Dora". sample this string using str[x:y:z] starting from the char with the index 0 position, ending by the char with the last position index and with step = 9.  store the result in a new variable called res.

strVar = "hello hello my name is Dora"
res = strVar[::9]

# Q7 - inputStr stores input string from user (can be of different length) write a code that stores in variable res the last character in the inputStr.

inputStr = input("string: ")
#write the rest if the code here:
res = inputStr[-1]

# Q8 - Write a code that asks the user "what is your name? " and saves the input in variable user_name. then it asks the user for his age and saves this input to user_age. then save in res the formatted string. user's name is ___ . user's age is___ . where ___ are filled with the values from the user that were received.

user_name = input("what is your name? ")
user_age = input("what is your age? ")
res = f"user's name is {user_name}\nuser's age is {user_age}"

# Q9 - Get user's email address into the variable mail. this email address has the following pattern: firstname.lastname@mailserver.com/ac.il. use the built functions to obtain user's first name and user's last name in two different variables. assign res variable with concatenation of user's name and user's last name separated by whitestace and with capitalized first letters.

mail = input('please enter your mail: ')
first_name_index = mail.index(".")
last_name_index = mail.index("@")
first_name = mail[:first_name_index]
last_name = mail[first_name_index+1:last_name_index]
res = str.title(first_name + " " + last_name)


