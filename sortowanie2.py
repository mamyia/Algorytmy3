import random
from datetime import datetime


def partitionLast1(input_list, low, high):
    i = (low - 1)
    pivot = input_list[high]
    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] = input_list[j], input_list[i]
    input_list[i + 1], input_list[high] = input_list[high], input_list[i + 1]
    return (i + 1)


def quickSortLast1(input_list, low, high):
    if low < high:
        partition_index = partitionLast1(input_list, low, high)
        quickSortLast1(input_list, low, partition_index - 1)
        quickSortLast1(input_list, partition_index + 1, high)



# mid pivot

def partitionMid1(input_list, low, high):
    input_list[low], input_list[(low + high) // 2] = input_list[(low + high) // 2], input_list[low]
    pivot = input_list[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if input_list[j] < pivot:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1
    input_list[i - 1], input_list[low] = input_list[low], input_list[i - 1]
    return i - 1


def quickSortMid1(input_list, low, high):
    if low < high:
        pivot = partitionMid1(input_list, low, high)
        quickSortMid1(input_list, low, pivot - 1)
        quickSortMid1(input_list, pivot + 1, high)


def partitionMid2(input_list, low, high):
    input_list[low], input_list[(low + high) // 2] = input_list[(low + high) // 2], input_list[low]
    pivot = input_list[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if input_list[j] > pivot:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1
    input_list[i - 1], input_list[low] = input_list[low], input_list[i - 1]
    return i - 1


def quickSortMid2(input_list, low, high):
    if low < high:
        pivot = partitionMid2(input_list, low, high)
        quickSortMid2(input_list, low, pivot - 1)
        quickSortMid2(input_list, pivot + 1, high)


# losowy pivot

def partitionRand1(input_list, low, high):
    randomNum = random.randint(low, high)
    input_list[low], input_list[randomNum] = input_list[randomNum], input_list[low]
    pivot = input_list[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if input_list[j] > pivot:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1
    input_list[i - 1], input_list[low] = input_list[low], input_list[i - 1]
    return i - 1


def quickSortRand1(input_list, low, high):
    if low < high:
        pivot = partitionRand1(input_list, low, high)
        quickSortRand1(input_list, low, pivot - 1)
        quickSortRand1(input_list, pivot + 1, high)


def partitionRand2(input_list, low, high):
    randomNum = random.randint(low, high)
    input_list[low], input_list[randomNum] = input_list[randomNum], input_list[low]
    pivot = input_list[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if input_list[j] < pivot:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1
    input_list[i - 1], input_list[low] = input_list[low], input_list[i - 1]
    return i - 1


def quickSortRand2(input_list, low, high):
    if low < high:
        pivot = partitionRand2(input_list, low, high)
        quickSortRand2(input_list, low, pivot - 1)
        quickSortRand2(input_list, pivot + 1, high)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify2(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        (arr[i],
         arr[smallest]) = (arr[smallest],
                           arr[i])

        heapify2(arr, n, smallest)


def heapSort2(arr, n):
    for i in range(int(n / 2) - 1, -1, -1):
        heapify2(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapify2(arr, i, 0)


def mergeSort1(arr3):
    if len(arr3) > 1:

        mid = len(arr3) // 2

        L = arr3[:mid]

        R = arr3[mid:]

        mergeSort1(L)

        mergeSort1(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr3[k] = L[i]
                i += 1
            else:
                arr3[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr3[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr3[k] = R[j]
            j += 1
            k += 1


def mergeSort2(arr3):
    if len(arr3) > 1:

        mid = len(arr3) // 2

        L = arr3[:mid]

        R = arr3[mid:]

        mergeSort2(L)

        mergeSort2(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr3[k] = L[i]
                i += 1
            else:
                arr3[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr3[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr3[k] = R[j]
            j += 1
            k += 1
probadane = 1
probabblad = 1

for p in range(5):
    tablica = [random.randint(-10000, 10000) for i in range(10000)]
    tablica1 = list(tablica)    #QuickSort pivot jako ostatni
    tablica2 = list(tablica)    #QuickSort pivot jako środek
    tablica3 = list(tablica)    #QuickSort pivot losowy
    tablica4 = list(tablica)    #HeapSort
    tablica5 = list(tablica)    #MergeSort
    dl = len(tablica)
    n = len(tablica)
    print('\n Próba na '+str(probadane)+'zestawie  liczb')

    for l in range(5):
        print('\n Pomiar '+str(probabblad)+' na zestawie liczb '+str(probadane))

        print("\n")
        '''
        print("Quick Sort z wskaźnikiem na końcu")
        
        print("sortowanie")
        t1 = datetime.now()
        quickSortLast1(tablica1, 0, dl - 1)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)
        
        print("sortowanie")
        t1 = datetime.now()
        quickSortLast1(tablica1, 0, dl - 1)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)
        
        print("sortowanie odwrotne")
        t1 = datetime.now()
        quickSortMid1(tablica2, 0, dl - 1)
        t2 = datetime.now()
        t3 = t2 - t1
        t1 = datetime.now()
        print(t3)
        print("\n")
        '''
        print("Quick Sort z wskaźnikiem na środku")

        print("sortowanie")
        t1 = datetime.now()
        quickSortMid1(tablica2, 0, dl - 1)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)

        print("sortowanie")
        t1 = datetime.now()
        quickSortMid2(tablica2, 0, dl - 1)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)

        print("sortowanie odwrotne")
        t1 = datetime.now()
        quickSortRand1(tablica3, 0, dl - 1)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)
        print("\n")

        print("Quick Sort z wskaźnikiem losowym")

        print("sortowanie")
        t1 = datetime.now()
        quickSortRand1(tablica3, 0, dl - 1)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)

        print("sortowanie")
        t1 = datetime.now()
        quickSortRand1(tablica3, 0, dl - 1)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)

        print("Sortowanie odwrotne")
        t1 = datetime.now()
        quickSortRand2(tablica3, 0, dl - 1)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)
        print("\n")

        print("sortowanie heapsport")

        print("sortowanie")
        t1 = datetime.now()
        heapSort(tablica4)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)

        print("sortowanie")
        t1 = datetime.now()
        heapSort(tablica4)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)

        print("sortowanie odwrotne")
        t1 = datetime.now()
        heapSort2(tablica4, n)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)
        print("\n")

        print("merge sort")

        print("sortowanie")
        t1 = datetime.now()
        mergeSort1(tablica5)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)

        print("sortowanie")
        t1 = datetime.now()
        mergeSort1(tablica5)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)

        print("sortowanie")
        t1 = datetime.now()
        mergeSort2(tablica5)
        t2 = datetime.now()
        t3 = t2 - t1
        print(t3)
        probabblad += 1

    probabblad = 1
    probadane += 1

