x = 3 # global verilən yaradırıq

def calculate():
    y = 5 # local verilən yaradırıq

    # yaradılan scope-un içində manipulasiya etmək olur
    print("x + y =", x + y)
    print("x:", x)
    print("y:", y)

calculate()

print(y) # yalnışdır, "y" öz scope-undan başqa heç yerdə istifadə ola bilməz



"""LEGB: Local-Enclosed-Global-Builtin"""
x = 3 # global

def func(numb:int): # global
    y = 5 # enclosing

    def func2(numb:int): # local
        z = 8 # local
        print("z + y =", z + y) # builtin
    print(z) # yalnışdır, "z" öz scope-undan başqa heç yerdə istifadə ola bilməz
    func2(y)
    print("y + x =", y + x) # builtin

func(x)

print(y) # yalnışdır, "y" öz scope-undan başqa heç yerdə istifadə ola bilməz
