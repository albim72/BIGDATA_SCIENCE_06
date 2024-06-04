def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f'element listy nr {i+1} => wartość: {j}')

def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f'klucz: {x} -> wartość: {y}')
