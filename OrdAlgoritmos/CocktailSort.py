#Definição da função cocktail Sort

def CoquetelOrd(lista):
    tam_lista = len(lista)
    for index in range(tam_lista):
        for i in range(tam_lista-1):
            if lista[tam_lista-1-i] < lista[tam_lista-2-i]:
                lista[tam_lista-1-i],lista[tam_lista-2-i] = lista[tam_lista-2-i],lista[tam_lista-1-i]
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
    return lista
                