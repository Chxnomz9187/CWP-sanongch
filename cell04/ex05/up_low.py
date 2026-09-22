inp = input()

result = ''
for i in inp:
    if i.islower():
        result += i.upper()
    elif i.isupper():
        result += i.lower()
    else:
        result += i

print(result)