# artifacts.py by Jacob Steinebronn
from math import sqrt

numTests = int(input())

# Returns the square of the distance between two points
def dist2(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

# Takes a list of artifacts, and a single special artifact "target" and merges every artifact
# from the list that can reach the target. Returns a tuple of 2 elements, the first being
# the list of remaining artifacts after one iteration, and the second being either the 
# new, merged target after some merges were performed, or False, indicating no merges occurred
def reduce(artifacts, target):
    res = []
    targx, targy, targr = target
    sumx, sumy, numMerged = targx, targy, 1
    radiusSquaredSum = targr**2
    
    for xi, yi, ri in artifacts:
        # If the distance between the points is within the sum of radii, then this
        # artifact will merge with the target
        if dist2(targx, targy, xi, yi) <= (targr + ri)**2:
            sumx += xi
            sumy += yi
            radiusSquaredSum += ri**2
            numMerged += 1
        else: res.append((xi, yi, ri))
    # If the sum of the radii^2 of the merged artifacts is just the target,
    # then no merges happened.
    if numMerged == 1:
        res.append(target)
        return (res, False)
    # At least one merge happened. The new target is the average x and y, 
    # and the radius is the sqrt of sum of radii
    return (res, (sumx/numMerged, sumy/numMerged, sqrt(radiusSquaredSum)))

for tn in range(numTests):
    n = int(input())
    arts = []
    for i in range(n):
        # Read in the next point. It will be the target point, since
        # it's the newest artifact and all new merges this turn will include it.
        targ = tuple(map(int, input().strip().split()))
        # Continually simulate merges until there is an iteration with no merge
        while targ != False:
            arts, targ = reduce(arts, targ)
    print(len(arts))