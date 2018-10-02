def slowslicesum(L):
    return max((sum(L[i:j]), i, j) for j in range(len(L)+1) for i in range(j))

def quadraticslicesum(L):
    P = [sum(L[:i]) for i in range(len(L) + 1)]
    sums = []
    for j in range(len(L) + 1):
        for i in range(j+1):
            sums.append((P[j] - P[i], i, j))
    return max(sums)

# find largest suffix, prefix, and sequence, then combine going up
# at the bottom, you will have one
# moving up you will have all three

def prefix(L):
    if len(L) == 1:
        return (sum(L), 0)
    elif len(L) == 2:
        if L[1] >= 0:
            return (L[0] + L[1], 1)
        else:
            return (L[0], 0)
    elif len(L) > 2:
        sum_array = []
        for x in L:
            if len(sum_array) == 0:
                sum_array.append(x)
            else:
                sum_array.append(x + sum_array[-1])
        prev_value = 0
        j = -1
        for i, value in enumerate(sum_array):
            # if len(sum_array) < 11:
                # print(sum_array, i, j, value, prev_value)

            if value >= prev_value:
                # print(value, prev_value)
                prev_value = value
                j = i
        return (prev_value, j + 1)

def suffix(L):
    L.reverse()
    if len(L) == 1 and L[0] >= 0:
        return (sum(L), 1)
    elif len(L) == 1 and L[0] < 0:
        return (0, 1)
    elif len(L) >= 2:
        sum_array = []
        for x in L:
            if len(sum_array) == 0:
                sum_array.append(x)
            else:
                sum_array.append(x + sum_array[-1])
        prev_value = 0
        j = -1
        # print(sum_array)
        for i, value in enumerate(sum_array):
            # print(i, value)
            if value >= prev_value:
                prev_value = value
                j = i
        return (prev_value, len(L) - j - 1)

def slicesum(L):
    # returns (sum, begin_index, end_index)

    length = len(L)

    # print("L", L, L[0])

    if length == 1 and L[0] >= 0:
        # print("len 1, if", L[0])
        return (L[0], 0, 1)
    elif length == 1:
        # print("len 1, elif", L[0])
        # print("returning", "(0,0,0)")
        return (0, 0, 0)

    slice_index = length // 2

    left = suffix(L[:slice_index])
    right = prefix(L[slice_index:])

    left_slice = slicesum(L[:slice_index])
    right_slice = slicesum(L[slice_index:])
    right_slice = (right_slice[0], right_slice[1] + slice_index, right_slice[2] + slice_index)
    # print("before middle_slice", left, right, slice_index)
    middle_slice = (left[0] + right[0], left[1], right[1] + slice_index) # this is wrong



    largest = (0, 0, 0)
    largest_len = 0

    slice_array = (largest, right_slice, middle_slice, left_slice)
    prev = (0, 0, 0)

    # print("L", L)
    for slices in slice_array:
        if slices[0] > prev[0]:
            prev = slices
        elif slices[0] == prev[0] and slices[2] - slices[1] > prev[2] - prev[1]:
            prev = slices
        elif slices[0] == prev[0] and slices[2] - slices[1] == prev[2] - prev[1] and slices[1] < prev[1]:
            prev = slices
    return prev



if __name__=="__main__":
    # print(prefix([1,2,3,4,5]))
    # print(suffix([1,2,3,4,5]))
    # print(prefix([1,-100,2,3,4]))
    # print(prefix([1,-100,2,3,4,100]))
    # print(suffix([-100,1,2,3,4]))
    # print(suffix([100,-100,1,2,3,4]))
    # print(suffix([1,-100,2,3,4,100]))

    # print(slicesum([1,2,3,4,5,6]))
    # print("TEST ONE")
    # print(slicesum([-1,-1,-1,-1,5,-1]))
    # print("TEST TWO")
    print(slicesum([3, -100, 1, 1, 1]))
    # print("TEST THREE")
    # print(slicesum([-10, 1, 1, 1, -100, 1, 1, 1, -10]))
