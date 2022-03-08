# Dog Drama
# Solution by Andy Phan

# Read in number of test cases
tests = int(input())

# Iterate over test cases
for caseNum in range(tests):

    # Read in n, l, and origin point
    n, l = map(int, input().split())
    ox, oy = map(int, input().split())

    # Iterate over flowers and count number in circle
    res = 0
    for i in range(n):
        x, y = map(int, input().split())
        # Point is inside of circle if (x-o.x)^2 + (y-o.y)^2 <= r^2
        if (x-ox)**2+(y-oy)**2 <= l*l:
            res += 1
    
    # Print output
    print(res)