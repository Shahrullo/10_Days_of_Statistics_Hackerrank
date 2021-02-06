N = int(input())

arr = input()

list_arr = []

for i in arr.split(' '):
    list_arr.append(int(i))

def mean(x):
    return round((sum(x) / len(x)), 1)


def median(x):
    x = sorted(x)
    len_list = len(x)
    index = (len_list - 1) // 2
    
    if (len_list % 2):
        return round(x[index], 1)
    else:
        return round((x[index] + x[index + 1]) / 2.0, 1)
    
def mode(x):
    x.sort()
    counts = dict()
    for i in x:
        counts[i] = counts.get(i, 0) + 1
    return max(counts, key=counts.get) 

print(mean(list_arr))
print(median(list_arr))
print(mode(list_arr))