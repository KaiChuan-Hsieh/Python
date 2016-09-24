def CountSplitInv(B, C):
    i = 0
    j = 0
    count = 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1
            count += len(B) - i

    if i < len(B):
        while i < len(B):
            D.append(B[i])
            i += 1
    elif j < len(C):
        while j < len(C):
            D.append(C[j])
            j += 1

    return count


def SortAndCount(A):

    if len(A) == 0 or len(A) == 1:
        return 0

    B = A[:len(A)/2]
    C = A[len(A)/2:]

    X = SortAndCount(B)
    Y = SortAndCount(C)
    Z = CountSplitInv(B, C)

    return X + Y + Z
    
