# datetime kitabxanasından lazımlı funksiya və klassları import edirik
from datetime import date, time, datetime, timedelta



# bugünki tarix
bugun = date.today()
print("Bugün:", bugun)



# öz tariximizi yaratmaq
ad_gunu_Emil = date(2010, 11, 14)
ad_gunu_Turan = date(2012, 5, 16)
ad_gunu_Nicat = date(2010, 9, 10)
print("Emilin ad günü:", ad_gunu_Emil)



# ayrı-ayrı tarix haqqında məlumat
print("Emil", ad_gunu_Emil.year, "təvəllüdlüdür")
print("Turan ayın", str(ad_gunu_Turan.day) + "-si anadan olub")
print("Nicat", str(ad_gunu_Nicat.month) + "-cu ay anadan olub")



# tarix fərqi(arasında olan vaxt)
print("Emil indiyə qədər", date.today() - ad_gunu_Emil, "ömür sürüb")



# vaxt obyektləri
saat = time(16, 55, 24)
print("Saat:", saat)
print("Saat:", saat.hour, "Dəqiqə:", saat.minute, "Saniyə:", saat.second)



# tarix və vaxt birlikdə 
indi = datetime.now()
print("İndiki tarix və vaxt:", indi)



# öz datetime-mızı yaratmaq
# il, ay, gün, saat, dəqiqə, saniyə, mikrosaniyə
imtahan_datetime = datetime(2025, 10, 22, 16, 30, 0, 0)
print("Emilin ad günü:", ad_gunu_Emil)



# string -> datetime
mətn = "2025-10-06 20:30:15"
dt = datetime.strptime(mətn, "%Y-%m-%d %H:%M:%S")
print("string -> datetime:")



# formatlaşdırılmış
print("Avropa təqvimi:", dt.strftime("%d/%m/%Y %H:%M"))
print("Amerika təqvimi:", dt.strftime("%m/%d/%Y %H:%M"))



# gələcək və keçmiş tarixlər 
bir_hefte_sonra = bugun + timedelta(days = 7)
print("Ev işi deadline:", bir_hefte_sonra)
bir_ay_evvel = bugun - timedelta(days = 30)
print("Bir ay əvvəl:", bir_ay_evvel)