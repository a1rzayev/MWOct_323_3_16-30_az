# təsadüfi dəyərlər yaratmaq üçün random modulundan/kitabxanasından istifadə edirik
import random

# "doğru" sualları
truths = [
    "Nə vaxtsa ən yaxın dostuna yalan demisən?",
    "Sevimli idman növünü de",
    "Heç imtahanda köçürmüsən?",
    "İndiyə qədər yediyin ən qəribə yemək nə olub?"
]


# "cəsarət" tapşırıqları
dares = [
    "Bir ayağın üstündə 10 dəfə hoppan",
    "Ən qorxulu qorxundan danış",
    "Layihə işini 2 dəqiqəyə yazmağa çalış",
    "Bağır: Asif müəllim, mənə bir qoyun!"
]

# otun gedişatı funksiyası
def play_game():
    print("Doğru və ya Cəsarət oyununa xoş gəlmisiniz")
    name = input("Adınızı daxil edin: ")
    while(True):
        choice = input(f"\n{name}, doğru yoxsa cəsarət?('çıxış' üçün yazın): ").lower()
        if(choice == "doğru"):
            print(f"Doğru: {random.choice(truths)}")
        elif(choice == "cəsarət"):
            print(f"Cəsarət: {random.choice(dares)}")
        elif(choice == "çıxış"):
            print("Görüşənədək!")
            break
        else:
            print("Zəhmət olmasa düzgün daxil edin ('doğru', 'cəsarət', 'çıxış')")

# oyunu qoşuruq
play_game()
