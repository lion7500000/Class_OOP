from functools import reduce
# def decorator_function(func):
#     def wrapper(*args):
#         print('Wrapper function')
#         print(f'Calling function: {func.__name__}')
#         print(f'With arguments: {args}')
#         print('Wrapped function in process')
#         print(func(*args))
#         print('Exiting wrapper')
#     return wrapper
#
# @decorator_function
# def hello(item):
#     return f'{item} is wrapped!'
# hello('Candy')
# result = reduce(lambda x,y: x+y, [2,3,4]) #работает с двумя значениями
# print((result))
# result2 =list(map(lambda x: x**2, [1,2,3])) #для обного значения последовательно
# print(result2)

# import math
# l = [1,2,3,4]
# print(math.prod(l))
# from math import *
# l = [1,2,3,4]
# print(prod(l))
# import datetime
# birth_year = 1975
# current_date = datetime.date.today()
# print(current_date)
# current_age = current_date.year - birth_year
# print(current_age)
# lst = ['10', '34', '45']
# print(list(map(int,lst)))

# lst_1 = [1,2,3,4]
# lst2 = [10,20,30,40]
# result = list(map(lambda x,y: x+y, lst2, lst_1))
# print(result)
# result2 = list(filter(lambda x: lst2, lst_1))
# print(result2)

# list_ages = [['user1', 90], ['user2', 78], ['user3', 40], ['user4', 3]]
# result_sum = list(filter(lambda current_user: current_user[1] > 50, list_ages))
# print(result_sum)

