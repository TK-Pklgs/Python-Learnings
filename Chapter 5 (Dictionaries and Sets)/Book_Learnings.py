# fav_lang = {"Arham":"Python","Warda":"Python","Muqeet":"Flutter","Talha":"C++","Ahmad":"Javascript"}
# print(fav_lang.get("Warda","No person with this name"))

# for value in sorted(set(fav_lang.values())):
#     print(value)

'''Nesting'''

# alien_0 = {"color":"green", "points":5}
# alien_1 = {"color":"yellow", "points":10}
# alien_2 = {"color":"blue", "points":15}

# aliens = [alien_0, alien_1, alien_2]
# aliens = []
# for items in range(1,31):
#     new_dict = {"Color" : "Green", "Points" : items, "Speed" : "Slow"}
#     aliens.append(new_dict)

# for alien in aliens[:3]:
#     if alien['Color'] == 'Green':
#         alien['Color'] = 'yellow'
#         alien['Points'] = '10'
#         alien['Speed'] = 'Medium'

# for alien in aliens[:5]:
#     print(alien)

# print("\n.....\n")
# print(f'Total number of aliens: {len(aliens)}')

'''A list in a Dictionary'''
# pizza = {
#     'crust' : 'thick',
#     'toppings' : ['mushrooms', 'extra cheese', 'extra peperoni']
# }

# print(f'You ordered a {pizza["crust"]} - crust pizza ')
# print('- With the following toppings:')

# for items in pizza['toppings']:
#     print(f'\t{items}')

# fav_lang = {
#     "Arham" : ['Cobol','Python'],
#     "Talha" : ['Python', 'HTML', 'CSS', 'Javascript'],
#     "Khalil" : ['Rust', 'Asssembly', "PHP"]
# }

# for key,value in fav_lang.items():
#     print(f'{key} favourite languages are:')
#     for values in value:
#         print(f'\t{values}')
#     print(' ')

'''A Dictionary in a Dictionary'''
# people = {
#     "1": {
#         "name": "Talha Khalil",
#         "age": 28,
#         "city": "Lahore"
#     },
#     "2": {
#         "name": "Sara Khalid",
#         "age": 30,
#         "city": "Karachi"
#     },
#     "3": {
#         "name": "Ahmed Luqman",
#         "age": 25,
#         "city": "Islamabad"
#     }
# }

# for ID, user_info in people.items():
#     print(f'User with ID = {ID}')
#     fullname = user_info["name"]
#     age = user_info["age"]
#     address = user_info["city"]
#     print(f'\tFullame: {fullname}')
#     print(f'\tAge: {age}')
#     print(f'\tAddress: {address}')

