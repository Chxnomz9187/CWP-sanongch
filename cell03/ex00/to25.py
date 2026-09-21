num = int(input("Enter a number less than 25\n"))
if num > 25:
    print("Error")
else:
    for i in range(num, 26, 1):
        print(f"Inside the loop, my variable is {i}")