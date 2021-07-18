#Definição da função Merge Sort
'''
def MesclaOrd(lista):
    fundir(lista, 0, (len(lista) -1))

def fundir(lista, inicio, fim):
    if inicio >= fim:
        return lista
     
    miolo = (inicio + fim) //2
    fundir(lista, inicio, miolo)
    fundir(lista, (miolo +1), fim)

    unir(lista, inicio, fim)


def unir(lista, inicio, fim):
    lista[inicio: fim +1] = sorted(lista[inicio: fim +1])
'''

def MesclaOrd(lista):
    if len(lista)>1:
        mid = len(lista)//2
        lefthalf = lista[:mid]
        righthalf = lista[mid:]

        #recursion
        MesclaOrd(lefthalf)
        MesclaOrd(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lista[k]=lefthalf[i]
                i=i+1
            else:
                lista[k]=righthalf[j]
                j=j+1
            k=k+1

            while i < len(lefthalf):
                lista[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                lista[k]=righthalf[j]
                j=j+1
                k=k+1