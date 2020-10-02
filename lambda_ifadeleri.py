# lambda ifadeleri bazi fonksyonlari tek satirde yazmamizi sagliyor
def topla(a,b,c):
    return a+b+c
# lambda ile yazma sekli
toplama=lambda a,b,c:a+b+c
print(toplama(1,2,3))

def ciftmi(a):
    if a%2==0:
       return True
    else:
        return False

print(ciftmi(5))


#lambda ile yazarsak
cift=lambda x:x%2==0
print(cift(5))
