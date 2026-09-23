import sys
if len(sys.argv) > 2:
    start = int(sys.argv[1])
    stop = int(sys.argv[2]) 

    result = []

    for i in range(start, stop + 1):
        result.append(i)

    print(result)
    
else:
    print("none")