"""Positional arqumentlər"""

# ədədin ikinci qüvvəsini tapmaq
def power_of_two(number): # number - positional arqument(məcburi, tək)
    return number * number

# iki ədədin vurmasın tapmaq
def multiplication_of_two(number1, number2): # number1, number2 - positional arqumentlər(məcburi)
    return number1 * number2

# iki ədədin çıxmasını tapmaq
def distraction_of_two(number1, number2): # number1, number2 - positional arqumentlər(məcburi)
    return number1 - number2

print("5 ^ 2 =", power_of_two(5))
print("5 * 10 =", multiplication_of_two(5, 10))
print("5 - 10 =", distraction_of_two(5, 10))



"""İxtiyari sayda arqumentlər(birölçülü - hər element = bir variable)"""
# məsələn: [1, 2, 3, 4, 5, 6]

# ixtiyari sayda ədədlərin summası
def summ_all(*args):
    summ = 0
    for elem in args:
        summ += elem
    return summ

print("1 + 2 + 3 =", summ_all(1, 2, 3))
print("1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 =", summ_all(1, 2, 3, 4, 5, 6, 7, 8))



"""İxtiyari sayda arqumentlər(ikiölçülü - hər element = iki variable)"""
# məsələn: [Əkbər=15, Nəriman=15, Nicat=15, Zülfüqar=13, Turan=13, Emil=15]
def students_ages_all(**kwargs):
    for key, value in kwargs.items():
        print("Tələbə:", key, "\tYaş:", value)

students_ages_all(Əkbər=15, Nəriman=15, Nicat=15, Zülfüqar=13, Turan=13, Emil=15)