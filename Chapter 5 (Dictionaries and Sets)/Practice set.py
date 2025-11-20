"""Question # 1"""
"""Write a program to create a dictionary of words with values as their English
translation. Provide user with an option to look it up!"""
# urdu_dict = {
#     "Aaj": "Today",
#     "Kal": "Tomorrow or Yesterday",
#     "Pani": "Water",
#     "Khana": "Food",
#     "Ghar": "Home",
#     "Kitaab": "Book",
#     "Dosti": "Friendship",
#     "Mohabbat": "Love",
#     "Zindagi": "Life",
#     "Aadmi": "Man",
#     "Aurat": "Woman",
#     "Bachcha": "Child",
#     "Kaam": "Work",
#     "Haqiqat": "Truth",
#     "Jhoot": "Lie",
#     "Madad": "Help",
#     "Khushi": "Happiness",
#     "Gam": "Sadness",
#     "Tez": "Fast",
#     "Dheema": "Slow",
#     "Sawaal": "Question",
#     "Jawaab": "Answer",
#     "Shehar": "City",
#     "Gaon": "Village",
#     "Rasta": "Road",
#     "Dard": "Pain",
#     "Sehat": "Health",
#     "Soch": "Thought",
#     "Zaban": "Language"
# }

# word = input("Enter Your Word: ")

# print(f"English meanning of {word} is {urdu_dict[word]}")

"""Questions # 2"""
"""Write a program to input eight numbers from the user and display all the unique
numbers (once).
"""

# un = set()

# for item in range(8):
#     numb = int(input("Enter Your Number: "))
#     un.add(numb)

# for i in un:
#     print(i)

"""Question # 3 & 4"""
"""Can we have a set with 18 (int) and '18' (str) as a value in it?"""

# s = {18,"18",18.0}
# print(len(s))

"""Question # 5"""
"""s = {}
What is the type of 's'?"""

# s = {}
# print(type(s))
"""It's types is a dictionary: <class 'dict'> """

"""Question # 6"""
"""Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique."""

# friend_lang = {}
# for _ in range(4):
#     name = input("Enter your Name: ")
#     lang = input("Enter your Favorite Language: ")

#     friend_lang[name] = lang

# for name, lang in friend_lang.items():
#     print(f"{name} favourite language is {lang}")

"""Question # 7"""
"""Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}"""

# s = {8, 7, 12, "Harry", [1,2]}
# print(s[4])
"""No, the values in a set cannot be changes and even a set cannot contain a list in it as sets are unhashable"""