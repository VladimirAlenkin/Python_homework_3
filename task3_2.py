# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.  
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно 
# содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

x = int(input('Введите число: '))
lst = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
lst.sort()
print(lst)
#print(len(lst))
if x <= lst [0]: result = lst[0]
if x >= lst[len(lst)-1]: result = lst[len(lst)-1]
min = 2
if x > lst [0] and x < lst[len(lst)-1]:
    for i in lst:
        temp = abs(x - i)
        if temp < min: 
            min = temp
            result = i
print (result)

# решено