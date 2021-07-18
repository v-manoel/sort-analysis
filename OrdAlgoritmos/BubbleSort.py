#Definição da função Bubble Sort

def BolhaOrd(lista):
    tam_lista = len(lista)
    for i in range(tam_lista):
        j = i + 1
        for j in range(tam_lista-1):
            if(lista[i] < lista[j]):
                lista[i],lista[j] = lista[j],lista[i]
    return lista