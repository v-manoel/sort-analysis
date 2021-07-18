#Definição da função Quick Sort

def RapidaOrd(lista):
    VelozOrd(lista, 0, (len(lista) - 1))

def VelozOrd(lista, inicio, fim):
    pivo = SubLista(lista,inicio,fim)
    if(inicio < pivo-1):
        VelozOrd(lista,inicio,(pivo-1))
    if(fim > pivo):
        VelozOrd(lista,pivo,fim)
        
def SubLista(lista,inicio,fim):
    #O pivo pode ser a posição ou elemento da lista - lembrando de por a opcao nao escolhida como comparador do while 
    pivo = (inicio + fim)//2
    #Não são necessarias o uso de variáveis auxiliares
    index_i = inicio
    index_f = fim           
    while(index_i <= index_f):
        while(lista[index_i] < lista[pivo]):   
            index_i += 1
        while(lista[index_f] > lista[pivo]):
            index_f -= 1
        #Antes de sair do laço verificar se i e j não se cruzaram, caso não lista[index_i] é maior que lista[index_j]
        if(index_i <= index_f):
            lista[index_i],lista[index_f] = lista[index_f],lista[index_i]
            index_i+=1
            index_f-=1
         #print para observar todas as trocas do quick
    return index_i

def QuickEOrd(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) - 1]
    equal = [x for x in lista if x == pivot]
    lesser = [x for x in lista if x < pivot]
    greater = [x for x in lista if x > pivot]
    return QuickEOrd(lesser) + equal + QuickEOrd(greater)