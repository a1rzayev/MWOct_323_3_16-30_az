# modullarэ kodumuza import(daxil) edirik
import random

# coinflip edən funksiya
def coinflip():
    value = random.randint(0, 1)
    if(value == 0):
        return("Yazı") # 0 olsa Yazı cavabın təqdim edirik
    else:
        return("Tura") # 1 olsa Tura cavabэn t?qdim edirik

# funksiyanı çağırıb cavabı təqdim edirik
print("Sizə", coinflip(), "düşdü")