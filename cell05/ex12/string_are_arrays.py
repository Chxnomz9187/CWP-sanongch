import sys
if len(sys.argv) > 1:
    inp = sys.argv[1]
    # print(inp)
    result = ''
    for each in inp:
        if each == 'z':
            result += 'z'

    if result:
        print(result)
    else:
        print("none")

else:
    print("none")