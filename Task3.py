# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

lst = [1, 2, 3, 6, 4, 3, 2, 1]
print(lst)
# new_lst = []
# for i in lst: 
#      if i not in new_lst:
#         new_lst.append(i) 
# print(f"Cписок неповторяющихся элементов исходной последовательности: {new_lst}")


res = list(filter(lambda x: lst.count(x)==1, lst))
print(res)