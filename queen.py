# number of test cases;
# the way this input is happening is we are grabbing our
# next line of input, and then casting it into an int
n = int(input())

# loop over every test case and solve each one at a time
for testNum in range(n):
    # k as defined in the problem
    k = int(input())

    # in this problem and in many others, it can often be
    # easier to count the opposite of what the problem is
    # asking and then using this opposite to compute our
    # actual result

    # for this problem, we can count the total number of
    # squares, and also the number of squares that the queen
    # can reach; we can then solve for the number of squares
    # that the queen can't reach with some algebra as follows:
    # numSquaresCanReach + numSquaresCannotReach = totalNumSquares
    # numSquaresCannotReach = totalNumSquares - numSquaresCanReach

    # some helpful values to have
    boardLength = k + 1 + k

    # let's compute our two known values:

    # an n by n grid has n * n squares
    totalNumSquares = boardLength * boardLength

    # there are 8 directions that the queen can go from the center
    # of the board, and she can go up to k squares in each of these
    # directions; we will also count the square she is currently standing
    # on as a reachable square
    numSquaresCanReach = 8 * k + 1

    # grab our unknown:
    numSquaresCannotReach = totalNumSquares - numSquaresCanReach

    # print our answer
    print(numSquaresCannotReach)