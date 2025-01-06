# my_list = [-2,41,-26,-3,4,2,-2,1,3,4,24,2,5,2,43,13,4,32,-121]
from functools import reduce

my_list = [1,2,3,5,8,4]
def nonnegative(lst):
    return lst>=0


def square(lst):
    return lst**2


def sum(key, lst):

    return key+lst
a = list(filter(nonnegative,my_list))
print(a)
print(list(map(square,a)))
square1= list(map(square,a))
print(list(zip(my_list , square1)))
print(reduce(sum, my_list , 0))


