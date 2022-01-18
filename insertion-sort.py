def insertionSort(arr):
    for i in range (1, len(arr)):
        answer = arr[i]

        j = i-1
        while j >= 0 and answer < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = answer

arr = [22,27,16,2,18,6]

insertionSort(arr)

print(arr)