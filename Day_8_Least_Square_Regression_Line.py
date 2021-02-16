X, Y = [], []

for i in range(5):
    i = input().split()
    X.append(int(i[0]))
    Y.append(int(i[1]))
    

x_sum = 0
y_sum = 0
x_sum_sq = 0
x_y_mul = 0

for i, j in zip(X, Y):
    x_sum += i
    y_sum += j
    x_sum_sq += i ** 2
    x_y_mul += i * j
    
N = 5
x_mean = x_sum / N
y_mean = y_sum / N

b = (N * x_y_mul - x_sum * y_sum) / (N * x_sum_sq - (x_sum**2))

a = y_mean - b * x_mean

X_test = 80

Y_test = a + b * X_test

print(round(Y_test, 3))
