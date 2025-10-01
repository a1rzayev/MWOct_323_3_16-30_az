# operasiya sisteminin modulunu əlavə edirik
import os



"""oxumaq"""
# file ancaq oxumaq üçündür, dəyişmək olmaz
file1 = open("Telebeler.txt", "r") # "r" - read mode
content1 = file1.read()
print(content1)
file1.close()



"""yazmaq"""
# file yazanda, keçmiş informasiya itir
file2 = open("Telebeler.txt", "w") # "w" - write mode
file2.write("Qiyas\nOmer")
file2.close()



"""əlavə eləmək"""
# file yazanda, keçmiş informasiya itmir
file3 = open("Telebeler.txt", "a") # "a" - append mode
file3.write("\nNicat & Turan")
file3.close()



"""auto-close"""
with open("Telebeler.txt", "r") as file:
    content = file.read()
    print(content)



"""qovluq yaratmaq"""
os.mkdir("Imtahanlar") # mkdir - make directory 



"""qovluq silmək"""
os.rmdir("Imtahanlar") # rmdir - remove directory



"""file silmək"""
os.remove("Telebeler.txt")



"""file adı dəyişmək"""
os.rename("Telebeler.txt", "Telebeler2.txt")