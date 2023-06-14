# jump_search

import math

def jump_search(arr,x):
    jump = int(math.sqrt(len(arr)))
    print(jump)
    left = 0
    right = 0
    while left < len(arr) and arr[left] <= x:
        right = min(len(arr)-1, left + jump)
        if arr[left] <= x and arr[right] >= x:
            break
        left += jump
    if left >= len(arr) or arr[left] > x:
        return -1
    right = min(len(arr) - 1, right)
    n = left
    while n <= right and arr[n] <= x:
        if arr[n] == x:
            return n
        n += 1
    return -1


testarr = [1,2,3,4,5,7,9,10]
y = int(input("Введи число:"))

if jump_search(testarr,y) != -1:
  print ("Элемен найден под индексом: ", jump_search(testarr,y))
else:
  print ("Элемент не найден в массиве")


