"""Question # 1"""
"""Write a program to store seven fruits in a list entered by the user."""

# my_list = []

# my_list.append(input("Enter Your first Fruit: "))
# my_list.append(input("Enter Your first Second: "))
# my_list.append(input("Enter Your first Third: "))
# my_list.append(input("Enter Your first Forth: "))
# my_list.append(input("Enter Your first Fifth: "))
# my_list.append(input("Enter Your first Sixth: "))
# my_list.append(input("Enter Your first Seventh: "))

# print(my_list)

"""Question # 2"""
"""Write a program to accept marks of 6 students and display them in a sorted
manner."""

# marks = []

# marks.append(int(input("Enter first student marks :")))
# marks.append(int(input("Enter second student marks :")))
# marks.append(int(input("Enter third student marks :")))
# marks.append(int(input("Enter fourth student marks :")))
# marks.append(int(input("Enter fifth student marks :")))
# marks.append(int(input("Enter sixth student marks :")))

# marks.sort()
# print(marks)

"""Question # 3"""
"""Check that a tuple type cannot be changed in python."""
# I have tested is and it cannot be changes as it is immutable.

"""Question # 4"""
"""Write a program to sum a list with 4 numbers."""

# my_list = [10,20,30,40]

# sum_list = sum(my_list)

# print(sum_list)

"""Question # 5"""
"""Write a program to count the number of zeros in the following tuple:"""
""""""

# a = (7, 0, 8, 0, 0, 9)
# print(a.count(0))

"""Question # 6"""
"""Use a for loop to print the numbers from 1 to 20,
inclusive."""

# for values in range(1,21):
#     print(values)

"""Question # 7"""
"""Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.)"""

# for values in range(1,1000001):
#     print(values)

"""Question # 8"""
"""Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers."""

# million = [values for values in range(1,1_000_001)]
# print(min(million))
# print(max(million))
# print(sum(million))

"""Question # 9"""
""" Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number."""

# for value in range(1,21,2):
#     print(value)

"""Question # 10"""
"""Make a list of the multiples of 3, from 3 to 30. Use a for loop to
print the numbers in your list."""

# for values in range(3,31,3):
#     print(values)

"""Question # 11"""
"""A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube."""

# for values in range(1,11):
#     print(f"Cube of {values} is {values ** 3}")

"""Question # 12"""
"""Use a list comprehension to generate a list of the first
10 cubes."""

# cubes = [values ** 3 for values in range(1,11)]
# for items in cubes:
#     print(items)

"""***********************************************************************"""