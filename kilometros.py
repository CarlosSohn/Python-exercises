"""
nombre = []
kms = []
x = ""
while x != "sort":
    x = input("Nombre: ")
    print("Kilometres per dia")
    l = int(input("Dilluns: "))
    m = int(input("Dimarts: "))
    mi = int(input("Dimecres: "))
    j = int(input("Dijous: "))
    v = int(input("Divendres: "))
    s = int(input("Dissabte: "))
    d = int(input("Diumenge: "))
    total = l+m+mi+j+v+s+d
    nombre.append(x)
    kms.append(total)
    x = input("Deseas continuar? s/n: ")
    if x == "s":
        continue
    elif x == "n":
        x = "sort"

for i in range(len(nombre)):
    print(nombre[i], "va fer", kms[i], "kilometres")"""
