def rotLeft(a, d):
    n = len(a)
    d = d % n   # handle cases where d > n
    return a[d:] + a[:d]

# Input
n, d = map(int, input().split())
a = list(map(int, input().split()))

# Perform rotation
result = rotLeft(a, d)

# Print output
print(*result)
