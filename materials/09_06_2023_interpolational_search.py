# Интерполяционный поиск

def inter_search(arr,x):
    low = 0
    high = len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        index = low + int((x - arr[low]) * (high - low) / (arr[high] - arr[low]))
        if arr[index] == x:
            return index
        if arr[index] < x:
            low = index + 1
        else:
           high = index - 1
    return - 1 


testarr = [1,2,3,4,5,7,9,10]
y = int(input("Введи число:"))

if inter_search(testarr,y) != -1:
  print ("Элемен найден под индексом: ", inter_search(testarr,y))
else:
  print ("Элемент не найден в массиве")


  