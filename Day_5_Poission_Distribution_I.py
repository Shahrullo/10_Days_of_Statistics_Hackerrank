def factorial(n):
    return 1 if n == 0 else factorial(n-1)*n

mean = float(input())

variable = int(input())

e = 2.71828

poisson_distribution = ((mean**variable) * (e**-mean)) / factorial(variable)

print(round(poisson_distribution, 3))