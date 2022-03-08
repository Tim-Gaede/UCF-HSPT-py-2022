# Read in the number of missions
days = int(input())
for t in range(days):
    # Read in number of sticks, number of pillars, respectively.
    sticks, stacks = input().split()
    sticks = int(sticks)
    stacks = int(stacks)
    if stacks == 0:
        # If there are no pillars, print "this is madness"
        # Very important check to ensure no divide by 0 errors occur.
        print("this is madness")
    else:
        print("%.3f" %(sticks/stacks))
