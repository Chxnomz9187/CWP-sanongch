def array_of_names(persons):
    first_name = list(persons.keys())
    last_name = list(persons.values())

    list_persons = []

    for i in range(len(first_name)):
        per = ''
        for j in range(len(last_name)):
            if j == i:
                first_name_new = first_name[i][0].upper() + first_name[i][1:]
                last_name_new = last_name[i][0].upper() + last_name[i][1:]

                per = first_name_new + ' ' + last_name_new
                list_persons.append(per)

    return list_persons

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))