n, m, a = map(int, input().split())

result = ((n + a - 1) // a) * ((m + a - 1) // a)

print(result)
