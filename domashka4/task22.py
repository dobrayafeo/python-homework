# Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующией
# строке второй список.
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
set1 = set(list1)
set2 = set(list2)
result_set = set1 & set2
result_str = sorted(map(str, result_set))
print(" ".join(result_str))







