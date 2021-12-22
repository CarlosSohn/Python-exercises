x = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7".split("\n")
claus = x[0].split(";") # Se almacenan les claus como lista
del x[0] #Borra claus
del claus[0]
dic = {}
prov = {})
for i in range(len(x)):
    nif = x[i].split(";")[0]
    for e in range(len(x)):
        prov.update({claus[e] : x[i].split(";")[e+1]})
    dic[nif] = prov
    prov = {}
print(dic)
