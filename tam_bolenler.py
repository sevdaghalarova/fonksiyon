# Tam bolenleri bulma
"""
Tam bolenleri bulma
Cikmak icin q-e basin
"""
def tambolen(x):
    liste=[]
    for i in range(1,x+1):
        if x%i==0:
            liste.append(i)
    return liste

while True:
    sayi=input("Sayi: ")
    if sayi=="q":
        break
    else:
        sayi=int(sayi)
        print(tambolen(sayi))
