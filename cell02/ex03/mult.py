num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

multi = num1 * num2

print(f"{num1} x {num2} = {multi}")

if multi == 0:
    print("The result is positive and negative.")
elif multi < 0:
    print("The result is negative.")
else:
    print("The result is positive.")