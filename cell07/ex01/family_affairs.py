def find_the_redheads(dict_fam):
    people = []
    for each in dict_fam:
        if dict_fam[each] == 'red':
            people.append(each)

    return people

# your method definition here
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))