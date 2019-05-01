arr = [[1,2,3,4,5],[6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20],[21,22,23,24,25]];
arr1 = []
for i in range(len(arr)):
    if i == 0:
        for i1 in range(len(arr[0])):
            print arr[0][i1]
    elif i == len(arr):
        i2 = len(arr[len(arr) - 1])
        while (i2 > 0):
            print arr[len(arr) - 1][i2]
            i2 = i2 - 1
    else:
        print arr[i][len(arr[i]) - 1]
        arr1.append(arr[i][0])
i3 = len(arr1) - 1;
while (i3 >= 0):
    print arr1[i3];
    i3 = i3 -1;
