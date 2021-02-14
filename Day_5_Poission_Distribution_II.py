variables = list(map(float, input().split()))

A = variables[0]
B = variables[1]

print(round(160 + 40 *(A + A**2), 3))
print(round(128 + 40 *(B + B**2), 3))