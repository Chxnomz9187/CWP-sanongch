def famous_births(inp_dict):
    result = []
    for x, obj in inp_dict.items():
        full_name_inp = obj['name']
        date_inp = obj['date_of_birth']

        result.append([date_inp, full_name_inp])

    result.sort()
    for part in result:
        full_name = part[1]
        date = part[0]
        print(f"{full_name} is a great scientist born in {date}.")
    

# your method definition here
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)