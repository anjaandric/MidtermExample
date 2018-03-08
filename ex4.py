def suma_cifara(broj):

    suma = 0
    for i in str(broj):
        cifra = int(i)
        suma = suma + cifra

    return suma

def suma_cifara_matematicari(broj):

    while(broj >0):
        cifra = broj % 10
        broj = broj // 10
        print(cifra)


print(suma_cifara(12345))
print(suma_cifara_matematicari(12345))