# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

users_num = (input('Введите любое вещественное число: '))
nums_sum = 0
# for i in str(users_num):
#         if i != '.' and i != ',' and i != '-':
#             nums_sum += int(i)

# print(F'{users_num} -> {nums_sum}')


for num in users_num:
    if num.isdigit(): nums_sum += int(num)
print(F'{users_num} -> {nums_sum}')


