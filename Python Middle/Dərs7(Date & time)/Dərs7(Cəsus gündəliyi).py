from datetime import datetime
import getpass
import os

# Gündəlik faylının adı
DIARY_FILE = "diary.txt"
PASSWORD = "spy2025"  # sadə nümunə üçün statik parol

# Qeyd əlavə edən funksiya
def add_entry():
    print("\nYeni qeyd əlavə et:")
    text = input("Qeyd mətni daxil et: ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Fayla yazmaq
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {text}\n")
    print("Qeyd uğurla əlavə olundu!\n")

# Bütün qeydləri göstərmək
def show_entries():
    if not os.path.exists(DIARY_FILE):
        print("Hələ qeyd yoxdur.")
        return

    print("\nGündəlik qeydləri:\n")
    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

# Əsas menyu
def menu():
    while True:
        print("\n==== CƏSUS GÜNDƏLİYİ ====")
        print("1. Yeni qeyd əlavə et")
        print("2. Bütün qeydlərə bax")
        print("3. Çıxış")

        secim = input("Seçiminizi daxil edin (1-3): ")
        if secim == "1":
            add_entry()
        elif secim == "2":
            show_entries()
        elif secim == "3":
            print("Gündəliyi bağladınız.")
            break
        else:
            print("Yanlış seçim! Yenidən cəhd edin.")

# Proqramın başlanğıcı
def main():
    print("Cəsus Gündəliyinə xoş gəlmisiniz!")
    parol = getpass.getpass("Girişi üçün parolu daxil edin: ")

    if parol == PASSWORD:
        print("Giriş təsdiqləndi!")
        menu()
    else:
        print("Parol səhvdir! Giriş qadağandır.")

if __name__ == "__main__":
    main()
