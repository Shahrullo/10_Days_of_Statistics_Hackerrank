import math

def cumulative_distribution(mean, std, amount):
    return 0.5 * (1 + math.erf((amount - mean) / (std * (math.sqrt(2)))))

variable = list(map(int, input().split()))

mean = variable[0]
std  = variable[1]

less_part = float(input())
between_part = list(map(float, input().split()))

less_solution = cumulative_distribution(mean, std, less_part)
between_solution = cumulative_distribution(mean, std, between_part[1]) - cumulative_distribution(mean, std, between_part[0])



print(round(less_solution, 3))
print(round(between_solution, 3))
