# Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.

class Test:
    def __init__(self, args):
        self.args = args

    def P(self):
        p_s = self.args
        return p_s

    def S(self):
        s_a = self.args ** 2
        return s_a

    def D(self):
        d_a = ((self.args ** 2)/ 2) ** 0.5
        return d_a

    def turp_sq(self):
        turp_s = (self.P(), self.S(), self.D())
        print
        return turp_s

class Result(Test):

    def turp(self):
        terp = (Test.D, Test.P, Test.S)

        return terp
a = 4
print(Result(a))


    # Используя лямбда - выражение, из списка  my_list = [20, -3, 15, 2, -1, -21]
    # создайте новый список, содержащий только положительные числа
# def my_list(arg):
#     print(list(filter(lambda x: isinstance(x, int) and x>=0, arg)))
#     return list(filter(lambda x: isinstance(x, int) and x>=0, arg))
# my_list([20, -3, 15, 2, -1, -21])
# Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# def lst(arg):
#     print(list(map(lambda x: x*2, arg)))
#     return list(map(lambda x: x*2, arg))
# lst([20, -3, 15, 2, -1, -21])
# Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
# class Dic_arg:
#     def __init__(self, **kwargs):
#         self.kwargs = kwargs
#
#     def return_dic(self):
#         for key, value in self.kwargs.items():
#             print(key, value)

# a = {'name' :'John', "last_name" : 'Smith', "age" : 35, "position" :  'web developer'}
# c = Dic_arg(**a)
# c.return_dic()








