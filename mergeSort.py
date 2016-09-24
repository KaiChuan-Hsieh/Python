def merge(listA, listB):
    i = 0
    j = 0
    c = []
    while i < len(listA) and j < len(listB):
        if listA[i] <= listB[j]:
            c.append(listA[i])
            i += 1
        else:
            c.append(listB[j])
            j += 1

    if i < len(listA):
       while i < len(listA):
           c.append(listA[i])
           i += 1
    elif j < len(listB):
       while j < len(listB):
           c.append(listB[j])
           j += 1

    return c


def mergeSort(myList):
    """Sorting an array of numbers by merge sort"""
    if len(myList) == 1:
        return myList

    A = mergeSort(myList[:len(myList)/2])
    B = mergeSort(myList[len(myList)/2:])

    return merge(A, B)
