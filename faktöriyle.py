# -*- coding: utf-8 -*-

num = int(input("Faktöriyelini Hesaplamak İstediğiniz Sayıyı Giriniz : "))
say = 1

for x in range(1,num+1):
        
    say = say * x
    
    
print(say)