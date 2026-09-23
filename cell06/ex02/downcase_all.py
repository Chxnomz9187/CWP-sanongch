import sys

def downcase_it(word):
    return word.lower()

if len(sys.argv) > 1:
    words = []
    for i in range(1, len(sys.argv)):
        words.append(sys.argv[i])

    for each in words:
        print(downcase_it(each))
        
else:
    print("none")