N = int(input())

X = list(map(float, input().split()))
Y = list(map(float, input().split()))

def rank(l):
    r = sorted(set(l))
    return [r.index(x)+1 for x in l]

def spearmanCC(x, y):
    squared = [(rx - ry) ** 2 for rx, ry in zip(rank(x), rank(y))]
    n = len(x)
    return 1 - (sum(squared) * 6 / (n * (n**2 - 1)))

res = spearmanCC(X, Y)
print(round(res, 3))