# solve a single test case
def solve():
    n, m = map(int, input().split())
    
    # read in input matrix
    a = [[int(c) for c in input().strip()] for _ in range(n)]
    
    # count the number of zeroes in the matrix 
    monkeys = sum(sum(x == 0 for x in row) for row in a)

    # do a bfs for each possible answer, and only visit positions with value <= ans
    for ans in range(10):
        seen = [[False] * m for _ in range(n)]
        queue = []
        qi = 0
        found = 0

        def insert(x, y):
            if 0 <= x < n and 0 <= y < m and not seen[x][y] and a[x][y] <= ans:
                queue.append((x, y))
                seen[x][y] = True
        
        # insert all of the edges into the bfs
        for i in range(n):
            insert(i, 0)
            insert(i, m-1)
        for j in range(m):
            insert(0, j)
            insert(n-1, j)

        while qi < len(queue):
            x, y = queue[qi]
            qi += 1
            found += a[x][y] == 0

            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                insert(x + dx, y + dy)

        if found == monkeys:
            print(ans)
            return

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()