from checkmate import checkmate

def main():
    board = """\
..
.K\
"""
    checkmate(board)

if __name__ == "__main__":
    main()

# test case
#     board = """\
# R...
# .K..
# ..P.
# ....\
# """


#     board = """\
# ..
# .K\
# """