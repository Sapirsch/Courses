# Pandas assignment

# The Ministry of Health wanted to test the achievements of a new training program. For several consecutive months, data was collected on the candidates. The data is collected in csv tables so that the names of the participants appear in the first column, the names of the months in the first row, and each row is a collection of the data at the end of each month. That is, in the second column will appear the data of each candidate at the end of the first month, in the second column at the end of the second month and so on. (see the file on the model website)

# Q1 - Write a function data_of_columns that receives the name of the file and returns the names of the columns as a list.

def columns_of_data(file_name):
    import pandas as pd
    df = pd.read_csv('weights.csv')
    columns_list = []
    for col in df.columns.tolist():
        columns_list.append(col)
    return columns_list


# Q2 - Write a values_mean function that accepts the name of the file and returns its data frame plus the average row (last row of the weight average for each month), and the average column (a column called Mean and in which the average weight for each participant)

def mean_values(file_name):
    import pandas as pd
    global df1
    df1 = pd.read_csv('weights.csv')
    df1_no_names = df1.drop('Unnamed: 0', 1)
    df1 ['Mean'] = df1_no_names.mean(axis = 1) #adding a new columns cald 'Mean' with the avg for each person (each row)
    
    df1 = df1.append(df1.mean(axis = 0, numeric_only = True), ignore_index = True) #adding a new row with the avg of each month (each column)
    
    return df1

# Q3 -Write a weight_avg_min function that receives the data frame returned by the values_mean function and returns in which month the average was the lowest.

def min_avg_weight(df1):
    import pandas as pd
    df = pd.read_csv('weights.csv')
    df1 = mean_values(df)
    df1_wo_names = df1.drop('Unnamed: 0', 1)
    df1['lowest_lost_weight'] = df1_wo_names.idxmin(axis=1)
    print(df1['lowest_lost_weight'].tolist()[-1])
    
# Q4 - Write a function loss_weight that receives the name of the file and the names of the columns as a list, and returns a brand new data frame, where the row index is the names of the participants and its column index is the same as the column index of the input, and the values (the data) is weight loss in the current month. (difference between columns) Next to the current of the received data frame.

# Question_no_4 - calculation of the weight loss of each month
def weight_loss(file_name, *months_names):
    import pandas as pd
    df = pd.read_csv(file_name)
    global df2
    df2 = pd.DataFrame(index = df['Unnamed: 0'])
    for i, month in enumerate(months_names[:-1]):
        df2[str(month + "-" + (months_names[i+1]))] = (df[str(month)] - df[str(months_names[i+1])]).values
    return df2


  # Q5 - Write a function loss_weight_max that receives a data frame in the style of a data frame that returns a function in section 4 and returns which of the participants lost the most total weight during the months that appear in the data frame.      
#Question_no_5 - the participent that had the highest weight loss:
def max_weight_loss(df2):
    import pandas as pd
   
    df = df2.sum(axis=1)
    winner = df.idxmax(axis=1)
    return winner
    

    
    
    
    
    
    
