def median(x):
    x = sorted(x)
    len_list = len(x)
    index = (len_list - 1) // 2
    
    if (len_list % 2):
        return round(x[index], 1)
    else:
        return round((x[index] + x[index + 1]) / 2.0, 1)

N = int(input())

el = input().split()
freq = input().split()

arr = []

for i in range(len(el)):
    for j in range(int(freq[i])):
        arr.append(int(el[i]))
        
arr.sort()

index = int(len(arr)/2)

if len(arr) % 2 == 0:
    Q1 = arr[:index]
    Q3 = arr[index:]

else:
    Q1 = arr[:index]
    Q3 = arr[index+1:]

print(float(median(Q3) - median(Q1)))


