#Definição da função Gnome Sort

def GnomeOrd(lista):
    tam_lista = len(lista)
    for i in range(tam_lista-1):
        j = i + 1
        Condicao = True
        if lista[i] > lista[j]:
            lista[i],lista[j] = lista[j],lista[i]
            while i >= 1 and Condicao: 
                if lista[i] < lista[i - 1]:
                    lista[i],lista[i - 1] = lista[i - 1],lista[i]
                else: 
                    Condicao = False
                i -= 1
        i = j
    return lista