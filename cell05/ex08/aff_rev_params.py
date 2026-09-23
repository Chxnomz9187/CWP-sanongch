import sys
n = len(sys.argv)
if n > 2:
    for i in range(n - 1, 0, -1):
        print(sys.argv[i])
else:
    print("None")