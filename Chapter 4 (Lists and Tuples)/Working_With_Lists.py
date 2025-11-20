"""Looping Through a List"""
# numbers_list = [945, 976, 114, 20, 343, 688, 601, 193, 92, 104, 512, 231, 77, 845, 667, 430, 28, 999, 402, 215]
# strings_list = [ 'alice', 'charlie', 'frank', 'ivan', 'bob', 'Hannah', 'David', 'Grace', 'Eva', 'Julia']

# for names in strings_list:
#     print(f"{names.title()}, You are a great magician!")
#     print(f"I can't wait to see your next trick, {names.title()}\n")

# print("Thank you, every one. That was a great magic show!")

"""Range Function()"""
# Remeber always use one more than the actual range you want to run the code becuase it is always off by one it is a behaviour of the range function.
# for value in range(1,11):
#     print(value)
# for value in range(11):
#     print(value)
# squared = []
# for value in range(1,11):
#     squared.append(value ** 2)
# print(squared)

"""Functions that can be perform numbers of list"""

# print(sum(numbers_list))
# print(min(numbers_list))
# print(max(numbers_list))

"""List comprehensions"""
"""In Python, list comprehension is a concise way to create a list using a single line of code. It combines a for loop and optional conditions inside square brackets."""

# squares = [value ** 2 for value in range(1,11)]
# print(squares)

# for values in strings_list[:3]:
#     print(values)