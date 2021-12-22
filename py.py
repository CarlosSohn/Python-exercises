"""
#EXERCICI---------------------------------
dic = {}
num_alum = int(input("Quants?: "))
count = 0
nota = 0
notas = []
while count < num_alum:
    x = input("Nombre: ")
    if x in dic:
        print("ERROR: Nombre ya existente")
        nota = -1
    while nota >= 0:
        nota = int(input("Nota: "))
        if nota >= 0:
            notas.append(nota)
    dic[x] = notas
    notas = []
    count = count + 1
    nota = 0
print("NOTAS MEDIAS")
suma = 0
for i in dic:
    x = dic[i]
    for e in x:
        suma = suma + e
    total = suma/len(dic[i])
    print(i, total)
    suma = 0

#EXERCICI------------------------------------
x = int(input("Tamaño de listas: "))
count = 0
lista = []
len_lis = []
while count < x:
    nom = input("Nombre: ")
    lista.append(nom)
    len_lis.append(len(nom))
    count = count + 1
print("Nombres", lista)
print("Longitudes", len_lis)

#EXERCICI-----------------------------------
lista = [1, 5, 8, 3, 30, 9, 13]
for i in lista:
    if i%2 != 0 and i > 3:
        print(i)

#EXERCICI---------------------------------- 
stop = ""
dic = {}
while stop != True:
    nom = input("Nom: ")
    if nom == "*":
        stop = True
    else:
        edat = int(input("Edat: "))
        dic.update({nom : edat})
print("Majores d'edat")
for i in dic:
    if dic[i] >= 18:
        print(i, "-->", dic[i])
maxi = 0
maj = {}
for i in dic:
    if dic[i] > maxi:
        maxi = dic[i]
        nomx = i
print("Alumne con más edat:")
print(nomx, maxi)

# EXERCICI------------------------------------
stop = ""
lista = []
while stop != True:
    x = int(input("Afageix un número: "))
    if x < 0:
        stop = True
#    elif x in lista:
#        continue
    else:
        lista.append(x)
print(lista)
def borra():
    for i in range(cont-1):
        lista.remove(rep)
for i in lista:
    cont = lista.count(i)
    rep = i
    if cont > 1:
        borra()
    else:
        continue
print(lista)
"""



