# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def reverse(inp: int):
    # naive approach traverse it O(n)
    inp = str(inp)
    if inp[0] == '-':
        return "-"+inp[:0:-1]
    else:
        return inp[::-1]

if __name__=='__main__':
    print(reverse(0o121))
