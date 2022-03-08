from math import gcd

# solve a single test case
def solve():
    s = input()
    t = input()
    n = len(s)

    # how many characters match on the left and right ends of t
    L = 0
    R = 0
    while L < n-1 and s[L] == t[L]:
        L += 1
    # in python, s[-1] = last character in string, s[-2] = second to last, etc.
    while R < n-1 and s[-R-1] == t[-R-1]:
        R += 1

    p = 0
    q = n
    for i in range(n):
        if L >= i and R >= n - i - 1:
            p += 1
    # divide the fraction by the gcd
    g = gcd(p, q)
    p //= g
    q //= g
    print(f"{p}/{q}")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()