
# EXAMPLE PROBLEM # 

# with open(file,'r') as f: # how to open a file
#     data = f.read() # .read() returns all data as one string
#     # print(data)

#     # data_line = f.readline()
#     # print(data_line)

#     # data_list = f.readlines() # returns a list with
#     # print(data_list)          # each line, as a string, 
#     split_data = data.split()
#     print(split_data)







# NUMBER ONE #

# def write_file(filename, a_string, mode ):
#     with open(filename, mode) as f:
#         f.write(a_string)

# write_file('new_file.txt', "This is just a test", 'w')




# NUMBER TWO #

# def add_file(filename, option= 'read'):
#     with open(filename, 'read') as f:
#          if option == 'read':
#             return f.read()




# NUMBER THREE #

# def open_file(file_name, option='r'):
#     with open(file_name, 'r') as f:
#         if option == 'read':
#             return f.read()
#         elif option == 'readlines':
#             return f.readlines()
#         else:
#             return None

# data = open_file('file_name.txt', 'read')
# print(data)



# PROBLEM FOUR #


# def open_file(file_name, option='r'):
#     with open(file_name, 'r') as f:
#         if option == 'read':
#             string_nums = f.readlines()
#             for i in string_nums:
#                 string_nums[string_nums.index(i)] = int(i.split('\n')[0])
#             return sum(string_nums)
          

# data = open_file('sum_column.txt', 'read')
# print(data)



# PROBLEM FIVE #


# def sumall(filename, option = 'r'):
#     total = 0
#     with open(filename, 'r') as file:
#         if option == 'r':
#             string_nums = file.readlines()
#             # print(string_nums)
#             for line in string_nums:
#                 numbers = line.split()
#                 for i in numbers:
#                     # print(i)
#                     total += int(i)
#         return total
# data = sumall('sum_all.txt')
# print(data)     


# PROBLEM SIX #

# def read_column(filename, column_num, option = 'r'):
#     new_list = []
#     with open(filename, 'r') as f: 
#         if option == 'r':
#             lines = f.readlines()
#             for line in lines:
#                 line = line.split('\n')
#                 line.pop()
#                 # print(line)
#                 if line == line:
#                     new_list.append(line)
#             # print(new_list)
#             if column_num > 0:
#                 return new_list[column_num-1]
                

# data = read_column('read_column.txt', 2)           
# print(data)


# PROBLEM SEVEN #

# Write a function, countWord(filename, words), that takes a file and a list of words as parameters, 
# counts how many times they exist in filename, and writes the results to a new file, use any name you like for the file.  
# For purposes of this exercise words that are conjunctions can be considered a single word.

def countWord(filename, word_list, option = 'r'):
    new_list = []
    with open(filename, 'r') as file:
        if option == 'r':
            data = file.read().lower().split()
            # print(data[0])
            for word in data: # data.index[]
                if word[-1].isalpha() == False:
                    print(word[0:-1])
                    data[data.index(word)] = word[0:-1]
            print(data)

            for word in word_list:
                howmany = data.count(word)
                print(howmany)
            
                new_list.append(f"The word {word} is in this paragraph {howmany} times")
    with open('problem7.txt', 'w') as new_file:
        for i in new_list:
            new_file.write(i + '\n')
            # print(new_file)

word_list = ['ambiguity', 'better','is', 'be']
final = countWord('zen_of_python.txt', word_list)
print(final)


            




