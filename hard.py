# 2022 UCF HSPT - A Very Hard Problem
# Chris Gittings

# take in the number of test cases
days = (int)(input().strip())

# for each test case
for day in range(days):

    # take in the input
    l1, c1, l2, c2 = map(int, input().split())

    # multiply the length and complexity to get the difficulty
    difficulty1 = l1 * c1
    difficulty2 = l2 * c2

    # output the bigger number
    print(max(difficulty1, difficulty2))
