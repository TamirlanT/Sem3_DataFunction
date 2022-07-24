#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:[2, 3, 4, 5, 6] => [12, 15, 16];
# -     [2, 3, 5, 6]    => [12, 15]

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
print (list1)
print (list2)
def proizved(lst):
    result = []
    for i in range(0, len(lst)//2 if len(lst) % 2 == 0 else len(lst)//2 + 1):
        result.append(lst[i] * lst[-i-1])
    return result
print (proizved(list1))
print (proizved(list2))