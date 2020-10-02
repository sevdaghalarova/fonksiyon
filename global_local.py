l=10 #bu global bir degiskendir, her yerde,fonksiyonun icinde de kullanabiliriz
def toplama(): #toplama fonksiyonun bir parametre gondere de biliriz
    s=int(input("sayi1: ")) #bu ise bu fonksiyona ozgu local degiskendir,sadece bu fonksiyonda kullanilabilir
    f = int(input("sayi2: "))
    toplam=s+f
    return toplam

def carp(a): #fonksiyon parametre alicak
    return a*2

print(carp(toplama()))
