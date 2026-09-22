age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")

y = 10
for i in range(3):
    print(f"In {y} years, you'll be {age + 10} years old.")
    y += 10
    age += 10