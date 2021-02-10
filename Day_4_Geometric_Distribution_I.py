x = list(map(int, input().split()))
n = int(input())
prob = x[0] / x[1]

g = ((1-prob)**(n-1)) * prob

print(round(g,3))