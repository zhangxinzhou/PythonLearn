verse = [
    [1, 2, 3, 4, 5], [11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]
]

arr = []
for i in range(4):
    arr.append([])
    for j in range(5):
        arr[i].append(j)

print(arr)
print("--------------------------")
arr = [[j for j in range(5)] for i in range(4)]
print(arr)
print([arr[1][1]])
