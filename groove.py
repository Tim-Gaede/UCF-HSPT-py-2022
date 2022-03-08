# groove.py by Jacob Steinebronn
numTests = int(input().strip())

for _ in range(numTests):
    # read in input
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    # i = left pointer, j is right pointer
    ans, i, j = 0, 0, n-1
    while i < j:
        # if our left and right pointers have arrived at the target,
        # great! add 1 to our answer and keep sweeping inwards
        if arr[i] == ans+1 and arr[j] == ans+1: ans += 1
        # if our left-pointer is not at the next possible answer, move it right
        if arr[i] != ans+1: i += 1
        # if our right-pointer is not at the next possible answer, move it left
        if arr[j] != ans+1: j -= 1
    print(ans)