import sys
if len(sys.argv) > 1:
    words = []
    for i in range(1, len(sys.argv)):
        words.append(sys.argv[i])

    for each in words:
        if each[-3:] in 'ism':
            continue
        else:
            print(each + 'ism')
else:
    print("none")

