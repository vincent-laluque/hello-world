truc = input("Entrer la valeur du côté a du triangle : ")
a = int(truc)
truc = input("Entrer la valeur du côté b du triangle : ")
b = int(truc)
truc = input("Entrer la valeur du côté c du triangle : ")
c = int(truc)

demiperimetre = a + b + c
demiperimetre = demiperimetre / 2

aire = demiperimetre * (demiperimetre - a) * (demiperimetre - b) * (demiperimetre - c)
aire = aire ** 0.5

print("L'aire du triangle est de", aire)