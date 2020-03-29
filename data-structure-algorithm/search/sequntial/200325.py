def seq_search(arr, ele):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos += 1

    return found


def ordered_seq_search(arr, ele):
    """Input array must be ordered/sorted"""
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1

    return found


def iterative_binary_search(arr, ele):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first+last) / 2
        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


def recursive_binary_search(arr, ele):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) / 2

        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return recursive_binary_search(arr[:mid], ele)
            else:
                return recursive_binary_search(arr[mid+1:], ele)
