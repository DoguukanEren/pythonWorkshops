# -*- coding: utf-8 -*-

sayi1 = int(input("1. Sayıyı Giriniz "))
sayi2 = int(input("2. Sayıyı Giriniz "))
sayi3 = int(input("3. Sayıyı Giriniz "))

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
    enBuyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3
    
print(enBuyuk)

