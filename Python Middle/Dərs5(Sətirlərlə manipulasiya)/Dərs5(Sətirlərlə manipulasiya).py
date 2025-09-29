#  dəyişəm yaradırıq
name = "Nicat"
surname = "Eminli"
age = 15





"""konkatenasiya"""

# "," özündən sonra vergül qoyur, "+" isə qoymur
print("Salam, mənim adım " + name, surname + ". Mənim " + str(age) + " yaşım var")





""".format() funksiyasi"""

# №1 sadəcə ardıcıllıq
print("Salam, mənim adım {} {}. Mənim {} yaşım var".format(name, surname, str(age)))

# №2 indeksləri rəqəmlə göstərərək
print("Salam, mənim adım {1} {2}. Mənim {0} yaşım var".format(str(age), name, surname))

# №3 dəyişənləri göstərərək
print("Salam, mənim adım {b} {c}. Mənim {a} yaşım var".format(a = str(age), b = name, c = surname))





"""f funksiyası"""

# mətndən əvvəl "f" yazılmasa işləmir
print(f"Salam, mənim adım {name} {surname}. Mənim {str(age)} yaşım var")





"""% operatoru"""

# "%s" - string(sətir)
# "%d" - decimal(tam ədəd) - yəni int
# "%f" - float(kəsrli ədədlər)
print("Salam, mənim adım %s %s. Mənim %d yaşım var" % (name, surname, age))