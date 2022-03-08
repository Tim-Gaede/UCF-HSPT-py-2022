from re import S


t = int(input())

for q in range(t):
	
	inp = input().split(" ")

	n = int(inp[0])
	x = int(inp[1])

	inp = input().split(" ")
	tess = list(map(int, inp))

	inp = input().split(" ")
	maxie = list(map(int, inp))

	ans = 0
	# Let's assume Tess buys all the paintings
	for i in tess:
		ans += i
	
	# Let's create an array with a cost of swapping from Tess to Maxie
	swap = []
	for i in range(n):
		swap.append(maxie[i]-tess[i])

	swap.sort()
	# Now that it is sorted, let's swap the k best items
	for i in range(x):
		ans += swap[n-i-1]

	print(ans)