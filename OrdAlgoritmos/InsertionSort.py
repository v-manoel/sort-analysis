#Definição da função Insertion Sort

def InsercaoOrd(lista):
    tam_lista = len(lista)
    for index_base in range(1,tam_lista):
        index_comp = index_base - 1
        while (index_comp >= 0) and (lista[index_comp] > lista[index_comp + 1]):
            lista[index_comp+1],lista[index_comp] = lista[index_comp],lista[index_comp + 1]
            index_comp -= 1
    return lista