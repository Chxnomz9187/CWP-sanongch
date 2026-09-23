import sys
if len(sys.argv) > 1:
    key = sys.argv[1]
    
    words = input().split() 
    found = False

    for each in words:
        if each in key:
            print("Good job!")
            found = True
            break

    if not found:
        print("Nope, sorry...")

else:
    print("none")