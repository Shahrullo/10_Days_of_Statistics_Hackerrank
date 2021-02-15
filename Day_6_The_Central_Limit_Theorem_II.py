import math

tickets = int(input())
students = int(input())
mean = float(input())
std = float(input())

mean_sum = mean * students
std_sum = math.sqrt(students) * std

clt = 0.5 * (1 + math.erf((tickets - mean_sum) / (std_sum * math.sqrt(2))))

print(round(clt, 4))