import unicodedata

text = "\n"
uni_dict = {
    'Mathematical Operators': ['2200', '22ff'],
    'Miscellaneous Mathematical Symbols1': ['27c0', '27ef'],
    'Miscellaneous Mathematical Symbols2': ['2980', '29ff'],
    'Dingbats': ['2700', '27bf'],
    'Miscellaneous Symbols': ['2600', '26ff'],
    'Currency Symbols': ['20a0', '20cf'],
    'Arrows': ['2190', '21ff'],
    'Geometric Shapes': ['25a0', '25ff'],
    'Box Drawing': ['2500', '257f'],
    'Pictographs': ['1f300', '1f5ff']
}

for key in uni_dict.keys():
    for u_code in range(int(uni_dict[key][0], 16), int(uni_dict[key][1], 16) + 1):
        try:
            hex_code = hex(u_code)[2:]
            char = chr(u_code)
            name = unicodedata.name(char)
            text += f"{char},{hex_code},{key.upper()},{name}\n"
        except:
            continue

with open("D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\unicode_data.txt", "w", encoding="utf-8") as file:
    file.write(text)