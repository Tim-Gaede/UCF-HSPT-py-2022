# Catching Those Zs!
# Python 3 solution by Santiago Rodriguez

# read number of lines
n = int(input())

# iterate over cases
for _ in range(n):
    line = input()

    # count number of lower and uppercase z's
    num_zs = 0
    for char in line:
        if char == 'z' or char == 'Z':
            num_zs += 1

    # print appropriate output
    if num_zs >= 3:
        print("Time to take a nap.")
    else:
        print("Perry saves the day!")