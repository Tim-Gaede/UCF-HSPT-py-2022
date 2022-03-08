# array.py by Jacob Steinebronn
# There are many, many ways to solve this problem. I chose this because it was fun :)
print("\n".join( # We'll provide an array of strings, and this will put a newline between each one
    [
        [input(), input()+" "][1] # For each testcase, read 2 lines and take the second one
        for _ in range(int(input()))])) # do this once for each testcase