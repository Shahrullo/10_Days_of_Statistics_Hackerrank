import math

def cumulative_distribution(mean, std, amount):
    return 0.5 * (1 + math.erf((amount - mean) / (std * (math.sqrt(2)))))

variable = list(map(int, input().split()))

mean = variable[0]
std = variable[1]

high_score = int(input())
pass_score = int(input())

scored_higher = 100 - (cumulative_distribution(mean, std, high_score)*100)
passed = 100 - (cumulative_distribution(mean, std, pass_score) * 100)
failed = cumulative_distribution(mean, std, pass_score) * 100

print(round(scored_higher, 2))
print(round(passed, 2))
print(round(failed, 2))

