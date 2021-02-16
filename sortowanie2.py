import random
import os
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


def partitionLast2(input_list, low, high):
    i = (low - 1)
    pivot = input_list[high]
    for j in range(low, high):
        if input_list[j] >= pivot:
            i = i + 1
            input_list[i], input_list[j] = input_list[j], input_list[i]
    input_list[i + 1], input_list[high] = input_list[high], input_list[i + 1]
    return (i + 1)


def quickSortLast2(input_list, low, high):
    if low < high:
        partition_index = partitionLast2(input_list, low, high)
        quickSortLast2(input_list, low, partition_index - 1)
        quickSortLast2(input_list, partition_index + 1, high)

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


tablica = [random.randint(-10000, 10000) for i in range(1000000)]  # Tutaj w eksperymencie następywało manualne zmienianie ilości elementów w zależności od badanego elementu pomiarowego
tablica1 = list(tablica)
tablica2 = list(tablica)
tablica3 = list(tablica)
dl = len(tablica)

t1 = datetime.now()
quickSortLast1(tablica1, 0, dl - 1)
print(tablica1)
quickSortLast2(tablica1, 0, dl - 1)
print(tablica1)
t2 = datetime.now()
t3 = t2 - t1
# print(tablica1)
print(t3)



t1 = datetime.now()
quickSortMid1(tablica2, 0, dl - 1)
print(tablica2)
quickSortMid2(tablica2, 0, dl - 1)
print(tablica2)
t2 = datetime.now()
t3 = t2 - t1
print(t3)
# print(tablica2)

t1 = datetime.now()
quickSortRand1(tablica3, 0, dl - 1)
print(tablica3)
quickSortRand2(tablica3, 0, dl - 1)
print(tablica3)
t2 = datetime.now()
t3 = t2 - t1
print(t3)
# print(tablica3)

os.system("PAUSE")
