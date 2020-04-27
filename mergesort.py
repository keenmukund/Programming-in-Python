a = [5, 4, 3, 1, 2]
def mergeSort(a, left, right):
    if right - left <= 1:
        return (a[left:right])
    else:			
    	size = right - left
        mid = (left + right) // 2
        l = mergeSort(a, left, mid)
        r = mergeSort(a, mid, right)
        return (merge(l, r))
def merge(a, b):
    (c, m, n) = ([], len(a), len(b))
    (i, j) = (0, 0)
    while i + j < m + n:
        if i == m:
            c.append(b[j])
            j = j + 1
        elif j == n:
            c.append(a[i])
            i = i + 1
        elif a[i] <= b[j]:
            c.append(a[i])
            i = i + 1
        elif a[i] > b[j]:
            c.append(b[j])
            j = j + 1
    return (c)
mergeSort(a, 0, 5)
print(a)
