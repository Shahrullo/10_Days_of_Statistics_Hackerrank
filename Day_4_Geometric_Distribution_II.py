x = list(map(int, input().split()))

n = int(input())

p = x[0] / x[1]

q = 1 - p

prob = 1 - q**n

print(round(prob, 3))
