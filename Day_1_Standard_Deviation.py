from math import sqrt

def mean(x):
    return round((sum(x) / len(x)), 1)
    
N = int(input())

arr = [int(x) for x in input().split()]
arr_mean = mean(arr)

squared_distance = []

for i in range(len(arr)):
    res = (arr[i] - arr_mean)**2
    squared_distance.append(res)

std = round(sqrt(sum(squared_distance) / N), 1)

print(std)