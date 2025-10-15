# regular expression-lar üçün kitabxana(modul)
import re



# e-poçtların təyin olunması
text = "Əlaqə: rzayev_a@gmail.com, allahverdiyev_a@gmail.com"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print("e-poçtlar:", emails)



# telefon nömrəsinin yoxlanması
phone = "+994-70-217-10-75"
pattern = r'^\+\d{3}-?\d{2}-?\d{3}-?\d{2}-?\d{2}'
print("telefon nömrəsinin statusu:", bool(re.match(pattern, phone)))



# bütün rəqəmləri "#" işarəsi ilə əvəz etmək
text = "məndə 2 pişik və 3 it var"
pattern = r'\d+'
print(re.sub(pattern, '#', text))