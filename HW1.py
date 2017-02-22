
# # Homework 1
# ### Python homework for 25.01.2017


# ## Task1
# Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is a good exercise.)

def maximum (a,b):
    if a>b:
        return a
    else:
        return b

a = input("a = ")
b = input("b = ")

(max(a,b))



# ## Task2
# The function max() from exercise 1 will only work for two. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many of them are there? Write a function max_in_list() that takes a list of numbers and returns the largest one.

def maximum_in_list(*a):
    maximum = 0
    for arg in a:
        if arg>maximum:
            maximum = arg
    return maximum

maximum_in_list(5, 16, 98, 99, 15, 2)



# ## Task3
# Download your favorite book in txt format. Use regular expressions to replace the name of the main character with your name. Write result in the new file.

#Let's consider "1984" by George Orwell

import re
book = open(r'/Users/natasha/Documents/Master/BDSDI/HW 1/1984 George Orwell.txt', 'r')
str = book.read()

replacement = re.sub('Winston', 'Nathan', str)
book_new = open(r'/Users/natasha/Documents/Master/BDSDI/HW 1/Task3.txt', 'w')
book_new.write(replacement)
book_new.close()
print("Done it!")



# # Task4
# Download your favorite book in txt format. Create a regular expression which will select chapter titles. Create the new file. Write list of chapter titles in the new file.

#Chapter title looks like:
# 	CHAPTER THREE
#
#	The Ministry of Truth

import re
book = open(r'/Users/natasha/Documents/Master/BDSDI/HW 1/1984 George Orwell.txt', 'r')
str = book.read()

regular_expr = re.findall(r'CHAPTER+\s+\w+\n+.*\n\n',str)
book_new = open(r'/Users/natasha/Documents/Master/BDSDI/HW 1/Task4.txt', 'w')
book_new.writelines(regular_expr)
book_new.close()
print("Done it!")

