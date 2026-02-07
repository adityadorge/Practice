def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))

        # pos[x] = index of value x in p
        pos = [0] * (n + 1)
        for i in range(n):
            pos[p[i]] = i

        # suffix_max[i] = max value in p[i:]
        suffix_max = [0] * n
        suffix_max[-1] = p[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], p[i])

        # find first position where improvement is possible
        for i in range(n):
            if p[i] != suffix_max[i]:
                j = pos[suffix_max[i]]
                p[i:j + 1] = reversed(p[i:j + 1])
                break

        print(*p)

if __name__ == "__main__":
    solve()