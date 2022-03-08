# Parade
# Python 3 solution by Santiago Rodriguez

# read number of years
y = int(input())

# iterate over cases
for _ in range(y):
    raw_vals = input().split()

    # read size of parade and number of doors
    n, m = map(int, raw_vals)

    # print person at front of line
    print((m % n) + 1)