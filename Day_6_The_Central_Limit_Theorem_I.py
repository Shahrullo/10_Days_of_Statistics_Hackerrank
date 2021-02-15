import math

max_num = int(input())
num_boxes = int(input())
mean = int(input())
std = int(input())

mean_sum = mean * num_boxes
std_sum = math.sqrt(num_boxes) * std

clt = 0.5 * (1 + math.erf((max_num - mean_sum) / (std_sum * math.sqrt(2))))

print(round(clt, 4))
