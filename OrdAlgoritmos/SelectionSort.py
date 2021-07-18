#Definição da função Selection Sort

def SelecaoOrd(lista):
    tam_lista = len(lista)
    for i in range(0,tam_lista ):
        min_i = i
        for j in range(i+1,tam_lista ):
            if lista[j] < lista[min_i]:
                min_i = j

        lista[i],lista[min_i] = lista[min_i],lista[i]
    return lista