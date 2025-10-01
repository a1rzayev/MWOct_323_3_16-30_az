# random modulunu təsadüfi dəyərlər yaratmaq üçün istifadə edirik
import random

variants = ["daş", "qayçı", "kağız"]  # seçim variantları (qlobal)

# istifadəçinin seçimini öyrənirik
def get_user_choiсe():
    choise = input("\n\nSeçin (daş, qayçı, kağız): ").lower()  # istifadəçidən seçimini soruşuruq
    while(choise not in variants):
        print("Yanlış daxil etmə. Yenidən cəhd edin.")
        choise = input("Seçin (daş, qayçı, kağız): ").lower()  # səhv daxil etdikdə yenidən soruşuruq
    return choise  # istifadəçinin seçimini string kimi qaytarırıq

# kompüterin seçimini yaradırıq
def get_computer_choiсe():
    return random.choice(variants)  # təsadüfi seçim qaytarırıq

# qalibi müəyyən edirik
def determine_winner(user_choiсe:str, computer_choiсe:str):
    if(user_choiсe == computer_choiсe):
        return "Heç-heçə!"
    elif((user_choiсe == "daş" and computer_choiсe == "qayçı") or 
         (user_choiсe == "qayçı" and computer_choiсe == "kağız") or 
         (user_choiсe == "kağız" and computer_choiсe == "daş")):
        return "İstifadəçi qazandı!"
    else:
        return "Kompüter qazandı!"
    
# oyunu işə salmaq üçün funksiya
def play_game():
    user_choiсe = get_user_choiсe()
    computer_choiсe = get_computer_choiсe()
    print(f"\nSiz seçdiniz: {user_choiсe}")
    print(f"\nKompüter seçdi: {computer_choiсe}")
    print(determine_winner(user_choiсe, computer_choiсe))

# proqramı konsoldan çıxana qədər işlək vəziyyətdə saxlayırıq
while(True):
    play_game()
