some_list = [1, 2, 3, 4, 5, 6]
for ind in range(0, len(some_list)):
some_list[ind] = str(some_list[ind])
print(some_list)


def square(x):
return x ** 2


new_list = list(map(lambda x: x + 1, some_list))
print(new_list)

def even(x):
return type(x) == int

new_list = list(filter(lambda x: type(x) == int, some_list))
print(new_list)


some_list = [10, 20, 30, 40]
some_dict = {}
print(list(enumerate(some_list)))
for ind, value in enumerate(some_list):
some_dict[ind] = value

print(some_dict)

for ind in range(0, len(some_list)):
print(ind, some_list[ind])


first_list = ('apple', 'orange', 'grape', 'лимон')
second_list = ['яблоко', 'апельсин', 'виноград']
print(list(zip(first_list, second_list)))
for eng, ru in zip(first_list, second_list):
print(eng, ru)


# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
#
# transformation = <???>
#
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
#
# transormed_values = list(map(transformation, values))
#
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
#
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
#
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

transformation = lambda x: x

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(list(map(transformation, values)))


# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из
# пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна.

import math
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

new = list(filter(lambda x: x[0] != x[1], orbits))
new2 = max(map(lambda x: x[0]*x[1]*math.pi, new))
print(new2)
print(list(filter(lambda x: x[0]*x[1]*math.pi == new2, new)))


# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.

def same_by(characteristics, objects):
    if len(objects) == 0:
        return True
    for i in range(len(objects)):
        if characteristics(objects[i]) != characteristics(objects[0]):
            return False
    return True
