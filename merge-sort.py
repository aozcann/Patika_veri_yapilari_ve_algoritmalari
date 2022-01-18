
def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        print(left)
        print(right)
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        m = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[m] = left[i]
                i += 1
            else :
                lst[m] = right[j]
                j += 1
            m += 1

        while i < len(left):
            lst[m] = left[i]
            i += 1
            m += 1
        while j < len(right):
            lst[m] = right[j]
            j += 1
            m += 1
        
lst = [16,21,11,8,12,22]
print(lst)
mergeSort(lst)
print(lst)