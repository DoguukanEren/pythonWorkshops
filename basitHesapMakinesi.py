# -*- coding: utf-8 -*-

op = input("Hangi İşlemi Yapmak İstiyorsunuz ? (Lütfen '+' , '-' , '*', '-' formatında giriniz. = ")

if op == "+" or op == "-" or op == "*" or op == "/":
    
    a = True

    while (a == True) :

        num1 = float(input("1. Sayıyı Giriniz : "))
        num2 = float(input("2. Sayıyı Giriniz : "))

        if op == "+" :
            print("Sayıların Toplamı = " , (num1 + num2) )
        elif op == "-" :
            print("Sayıların Çıkarılması = " , (num1 - num2) )
        elif op == "*" :
            print("Sayıların Çarpımı = " , (num1 * num2) )
        elif op == "-" :
            print("Sayıların Bölümü = " , (num1 - num2) )
            
        ex = input("Hesap Makinesini Kapatmak İçin exit Yazmanız Yeterlidir.")
        if ex == "exit":
            a = False
        else:
            continue
        
    else:
        print("Lütfen Geçerli Bir Operatör Giriniz!")