number = [i for i in range(10)]

def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        arr.reverse()
        return
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = list(reversed(arr[i + 1:]))  # <-- Fixed line

if __name__ == "__main__":
    for _ in range(999999):
        next_permutation(number)
    print("".join(map(str, number)))
