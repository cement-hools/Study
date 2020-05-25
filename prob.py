from math import atan, pi
# test comment
def arcctan(x):
    return (pi / 2) - atan(x)
def compute_population(y):
    C = 172
    T = 2000
    t = 45
    at_v = (T - y) / t
    at = arcctan(at_v)
    N = (C / t) * at
    return N
   #вычислить численность населения для года t по формуле

#ввести строку с перечисленными через пробел годами
line = '1220 2369 2636 1032 2657 198 1118'
# преобразовать строку в список из строковых значений годов
years_str_list = line.split()
# вычислить количество элементов в списке
n = len(years_str_list)
# сформировать список years_list на основе years_str_list,
#преобразовав строковые значения в целые
years_list = [int(i) for i in years_str_list]
print(years_list)
# создать список population_list, каждый элемент которого вычисляется
# функцией compute_population от соответсвующего года из списка years_list
population_list = [compute_population(i) for i in years_list]
print(population_list)

# в цикле для каждого года вывести численность населения, для вывода использовать
# формат "%5d - %6.3f миллиард(ов)"
for i in range(n):
    print("%5d - %6.3f миллиард(ов)" % (years_list[i], population_list[i]))
