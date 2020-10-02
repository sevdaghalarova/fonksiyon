def toplama(): #toplama fonksiyonun bir parametre gondere de biliriz
    s=int(input("sayi1: "))
    f = int(input("sayi2: "))
    toplam=s+f
    return toplam
# return fonksiyonumuz baska fonksiyon icinde kullanmamiz icindir
#print(toplama()) #toplama fonksiyonun parametre vermis olsaydik burada arguman yazmamiz gerekirdi

def carp(a): #fonksiyon parametre alicak
    return a*2
# fonksiyon icinde return'den sonra yazilan kodlar calismaz
print(carp(toplama()))
