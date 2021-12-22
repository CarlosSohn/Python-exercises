# Si la pers no existe, se agrega al dic con una lista vuida
# Si la pers exist i el gust existe no pasa res
# Si la pers existe i el gust no existe, se agerga a la lista
"""dic = {}
x = ""
def addgus():
    gust = input("Gusto: ")
    if gust in dic.get(x):
        print("El gust ja està en la llista")
        print(dic)
    else:
        dic[x].append(gust)
        print(dic)
while x != "*":
    x = input("Nombre: ")
    if x not in dic and x != "*":
        dic1 = {x : []}
        dic.update(dic1)
        dic1.pop(x)
        print(dic)
    elif x in dic:
        addgus()
    elif x == "*":
        print("Bye!")"""
dic = {}
def add():
    numf = int(input("Número de factura: "))
    if numf in dic:
        print("Aquesta factura ja està registrada")
    else:
        coste = int(input("Coste: $"))
        dic1 = {numf : coste}
        dic.update(dic1)
        dic1.pop(numf)
        print(dic)

def pay():
    numf = int(input("Número de factura: "))
    totalf = []
    neto = 0
    if numf in dic:
        totalf.append(dic.get(numf))
        dic.pop(numf)
        print("Pagado!")
        print(dic)
    else:
        print("Aquesta factura no està registrada")
    for i in totalf:
        neto = neto + i
    print("Total pagat: ", neto)

def total():
    lista = []
    total = 0
    for i in dic:
        x = dic.get(i)
        lista.append(x)
    for i in lista:
        total = total + i
    print("Total a pagar:", total)
opc = 0
while opc != 3:
    opc = int(input("Què vols fer? \n1) Afegir \n2) Pagar \n3) Terminar \n:: "))
    if opc == 1:
        add()
        total()
    elif opc == 2:
        pay()
        total()
    else:
        print("Bye!")
