def CountSplitInv(B, C, D):
    i = 0
    j = 0
    k = 0
    count = 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            D[k] = (B[i])
            i += 1
            k += 1
        else:
            D[k] = C[j]
            j += 1
            k += 1
            count += len(B) - i

    if i < len(B):
        while i < len(B):
            D[k] = B[i]
            i += 1
            k += 1
    elif j < len(C):
        while j < len(C):
            D[k] = C[j]
            j += 1
            k += 1

    return count


def SortAndCount(A):

    if len(A) == 0 or len(A) == 1:
        return 0

    B = A[:len(A)/2]
    C = A[len(A)/2:]

    X = SortAndCount(B)
    Y = SortAndCount(C)
    Z = CountSplitInv(B, C, A)

    return X + Y + Z
