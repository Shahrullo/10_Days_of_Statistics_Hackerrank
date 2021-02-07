def median(x):
    x = sorted(x)
    len_list = len(x)
    index = (len_list - 1) // 2
    
    if (len_list % 2):
        return round(x[index], 1)
    else:
        return round((x[index] + x[index + 1]) / 2.0, 1)

N = int(input())

arr = [int(x) for x in input().split()]
arr.sort()

index = int(len(arr)/2)

if len(arr) % 2 == 0:
    Q1 = arr[:index]
    Q3 = arr[index:]

else:
    Q1 = arr[:index]
    Q3 = arr[index+1:]

print(int(median(Q1)))
print(int(median(arr)))
print(int(median(Q3)))

