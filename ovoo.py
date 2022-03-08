# solve a single test case
def solve(tc):
    n = int(input())
    ovoo = 0
    favor = 0

    print(f"Clan #{tc}:")

    for i in range(n):
        s = input()

        if s == "WORSHIP":
            favor += ovoo
            print(favor)
        else:
            ovoo += 1

    print()

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        solve(tc+1)