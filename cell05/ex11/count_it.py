import sys
if len(sys.argv) > 1:
    words = []
    for i in range(1, len(sys.argv)):
        words.append(sys.argv[i])

    print(f"parameters: {len(words)}")

    for each in words:
        count_char = 0
        for char in each:
            count_char += 1
        print(f"{each}: {count_char}")
else:
    print("none")