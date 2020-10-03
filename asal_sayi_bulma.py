# asal sayi 1'e ve kendisine bolunen sayidir
"""
Asal sayi bulma
cikmak icin q-e basin
"""
def asalmi(x):
    if x==1:
        return False
    elif x==2:
        return True
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True

while True:
    asal=input("Sayi: ")
    if asal=="q":
        break
    else:
        asal=int(asal)
        print(asalmi(asal))




