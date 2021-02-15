import statistics as st

N = int(input())

X = list(map(float, input().split()))
Y = list(map(float, input().split()))


def pearson_correlation(n, x, y):
    mean_X = sum(x) / n
    mean_Y = sum(y) / n
    
    std_X = st.pstdev(x)
    std_Y = st.pstdev(y)

    pcc = 0
    for i in range(n):
        pcc += (x[i] - mean_X) * (y[i] - mean_Y)
    return pcc / (n * std_X * std_Y)


res = pearson_correlation(N, X, Y)

print(round(res, 3))
    