fav_lang = {"Arham":"Python","Warda":"Cobol,C++","Muqeet":"Flutter","Talha":"C++","Ahmad":"Javascript"}
# print(fav_lang.get("Warda","No person with this name"))

for key, value in sorted(fav_lang.items()):
    print(f'{key}: {value}\n')