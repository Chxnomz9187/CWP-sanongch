import sys
def shrink(word):
    return word[:8]

def enlarge(word):
    while len(word) < 8:
        word += 'Z'
    return word

if len(sys.argv) > 1:
    words = []
    for i in range(1, len(sys.argv)):
        words.append(sys.argv[i])

    # print(words)

    for each in words:
        count = 0
        for char in each:
            count += 1

        # print(count)
        if count == 8:
            print(each)
        elif count > 8:
            print(shrink(each))
        elif count < 8:
            print(enlarge(each))

else:
    print("none")
    
