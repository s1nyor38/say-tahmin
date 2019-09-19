import random
print("oyunuma hoşgeldiniz")
a = random.randint(0, 100)
tahmin=0
ad = input("lütfen adınızı girin:")
print("girilen ad:", ad)
while True:
    tahmin+=1
    sayı = int(input("lütfen sayı girin:"))
    print("girilen sayı:", sayı)
    if sayı <tahmin:
        print("küçük bir sayı girdin")

    if sayı >tahmin:
        print("büyük bir sayı girdin")
    if sayı ==tahmin:
        print("tebrikler bildiniz.")
        break