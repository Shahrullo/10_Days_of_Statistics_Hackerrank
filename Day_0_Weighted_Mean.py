N = int(input())

arr = input()

weight = input()

list_arr = []

list_weight = []

for i in arr.split(' '):
    list_arr.append(int(i))
    
    
for j in weight.split(' '):
    list_weight.append(int(j))
    
# calculating the weighted mean
def weighted_mean(arr, weight):
    w_avg = sum(weight[x] * arr[x] for x in range(len(arr))) / sum(weight)
    return round(w_avg, 1) 


print(weighted_mean(list_arr, list_weight))