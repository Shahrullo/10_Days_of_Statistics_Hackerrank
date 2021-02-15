import math

sample = int(input())
mean = int(input())
std = int(input())
distribution = float(input())
z = float(input())

A = mean - (std / math.sqrt(sample)) * z
B = mean + (std / math.sqrt(sample)) * z

print(round(A, 2))
print(round(B, 2))