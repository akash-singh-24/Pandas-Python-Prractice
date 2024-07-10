# from Girlfriend import gf
#
# gf1 = gf('Shatakshi',25)
#
# gf2 = gf('Sudeshna',27)
#
# print(gf1.name)
# print(gf1.age)
# print(gf2.name)
# print(gf2.age)

# BUBBLE SORT
# arr = [5, 1, 2, 3, 7, 8, 1, 7, 8, 10,12,0,15]
# cnt = 0
# for i in range(len(arr) - 1):
#     for j in range(i+1, len(arr)):
#         if arr[i] < arr[j]:
#             z = arr[i]
#             arr[i] = arr[j]
#             arr[j] = z
#         cnt += 1
#
# print(cnt)
# print(arr)
# #
# # # LINEAR SORT
# arr1 = [5, 1, 2, 3, 7, 8, 1, 7, 8, 10,12,0,15]
# cnt1 = 0
# for i in range(len(arr1)):
#     for j in range(len(arr1)):
#         if arr1[i] > arr1[j]:
#             z = arr1[i]
#             arr1[i] = arr1[j]
#             arr1[j] = z
#         cnt1 += 1
# print(cnt1)
# print(arr1)
#
# # SELECTION SORT
#
# arr2 = [5, 1, 2, 3, 7, 8, 1, 7, 8, 10,12,0,15]
# cnt2 = 0
# for i in range(len(arr2)):
#     z = i
#     z1 = arr2[i]
#     for j in range(i+1,len(arr2)):
#         if arr2[j] < arr2[z] :
#             z = j
#         cnt2 += 1
#     k = arr2[i]
#     arr2[i] = arr2[z]
#     arr2[z] = k
# print(cnt2)
# print(arr2)
#
# #
# arr3 = [5, 1, 2, 3, 7, 8, 1, 7, 8, 10,12,0,15]
# cnt3 = 0
#
# def mergesort(arr):
#     global cnt3
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#         mergesort(left_half)
#         mergesort(right_half)
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
#             cnt3 += 1
#
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#             cnt3 += 1
#
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#             cnt3 += 1
#     return arr,cnt3
# arr3,cnt3 = mergesort(arr3)
# print(arr3)
# print(cnt3)

# Quick Sort

# cnt4 = 0
# arr4 = [5, 1, 2, 3, 7, 8, 1, 7, 8, 10,12,0,15]
#
# def quicksort(arr,low,high):
#     size = len(arr)
#     if low < high :
#         pi = partitions(arr,low,high)
#         quicksort(arr,low,pi - 1)
#         quicksort(arr,pi + 1,high)
#
# def partitions(arr, low,high):
#     pivot = arr[high]
#     i = low - 1
#     global cnt4
#     for j in range(low,high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j],arr[i]
#             cnt4 += 1
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1
#
# quicksort(arr4,0,len(arr4) - 1)
# print(arr4)
# print(cnt4)

# Heap Sort

cnt5 = 0
arr5 = [5, 1, 2, 3, 7, 8, 1, 7, 8, 10,12,0,15]

def heapify(arr,n,i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[i] < arr [right]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        print('Recursive Heapify')
        print(arr,n,largest)
        heapify(arr,n,largest)
    print('Heapify')
    print(largest,left,right,arr)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)
        print("heap_sort First i")
        print(n,i,arr)
    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i],arr[0]
        print("heap_sort Second i")
        print(n, i, arr)
        heapify(arr,i,0)

heap_sort(arr5)
print(arr5)







