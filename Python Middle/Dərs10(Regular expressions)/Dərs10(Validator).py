# müntəzəm ifadələr (regular expressions) üçün modulu idxal edirik
import re



# mətnin müntəzəm ifadələrlə (regex) skan edilməsi
def scan_text(text):

    # tapılan nəticələr
    findings = {}

    # mətn üçün nümunələr (şablonlar)
    patterns = {
        "E-poçtlar": r'\b[\w.-]+@[\w.-]+\.\w+\b',
        "Telefon nömrələri": r'\+?\d{1,3}[-\s]?\(?\d{2,3}\)?[-\s]?\d{3}[-\s]?\d{4}',
        "Kredit kartları": r'\b(?:\d[ -]*?){13,16}\b',
        "Şifrələr": r'\b(?:[A-Za-z0-9@#$%^&+=]{8,})\b',
        "URL-lər": r'https?://[^\s]+'
    }

    # hər bir şablonu açar və dəyər olaraq ayırırıq
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if matches:
            findings[name] = matches

    return findings



# əsas funksiya
def main():
    print("Kiber Müdafiəçiyə xoş gəlmisiniz!")
    print("Analiz üçün mətni daxil edin (çıxmaq üçün boş buraxın):")

    # istifadəçinin daxil etdiyi mətni yoxlayırıq
    while True:
        user_input = input("\nMətni daxil edin:\n> ")
        if not user_input.strip():
            print("Proqram dayandırıldı")
            break

        results = scan_text(user_input)
        if results:
            print("\n⚠ Şübhəli məlumat tapıldı:")
            for category, items in results.items():
                print(f"\n {category}:")
                for item in items:
                    print(f"   - {item}")
        else:
            print("Hər şey təmizdir. Heç bir pozuntu tapılmadı.")


if __name__ == "__main__":
    main()
