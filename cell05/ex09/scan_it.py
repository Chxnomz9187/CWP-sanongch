import sys
if len(sys.argv) > 2:
    key = sys.argv[1]
    inp_words = sys.argv[2]

    words = inp_words.split()
    count = 0
    for each in words:
        if each in key:
            count += 1

    print(count)
else:
    print("none")
