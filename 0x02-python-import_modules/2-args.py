#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_nums = len(sys.argv)
    if arg_nums == 1:
        print("0 arguments.")
    elif arg_nums == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_nums - 1))
    for i in range(arg_nums):
        print("{}: {}".format(i, sys.argv[i]))
