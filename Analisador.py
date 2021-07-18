import csv
import time
from manipuladorCSV import (
    lerArquivoTeste,
    getCamposTestes,
    setArqLog,
    apendArqLog,
    getMediaLog,
)
from OrdAlgoritmos import (
    SelectionSort,
    QuickSort,
    MergeSort,
    CocktailSort,
    BubbleSort,
    InsertionSort,
    PythonSort,
    GnomeSort,
)


Ordenadores = {"Selection": SelectionSort.SelecaoOrd,
                "Quick": QuickSort.RapidaOrd,
                "Merge": MergeSort.MesclaOrd,
                "Cocktail":CocktailSort.CoquetelOrd,
                "Bubble":BubbleSort.BolhaOrd,
                "Insertion":InsertionSort.InsercaoOrd,
                "Python":PythonSort.PythonOrd,
                "Gnome":GnomeSort.GnomeOrd,
                }


def cronometrar(metodo, campos):
    t_parciais = []
    for lista in campos:
        inicio_contagem = time.time()
        metodo(lista)
        fim_contagem = time.time()
        tempo_decorrido = fim_contagem - inicio_contagem
        t_parciais.append(f'{tempo_decorrido:.8f}')
    return t_parciais


#Apresentação de resultados
def testador(campos, n_testes):
    print("=" *40)
    for ordenador, metodo in Ordenadores.items():
        for teste in range(n_testes):
            campos_copia = getCamposTestes(campos)
            resultados_parciais = cronometrar(metodo, campos_copia)
            apendArqLog(ordenador,resultados_parciais)
            


#Realização dos testes e criação do arquivo de logs
setArqLog("Algoritmo","Access Crescente","Access Decrescente","Data Aleatoria")
campos = lerArquivoTeste()
n_testes = int(input('Quantidade da bateria de testes: '))
testador(campos, n_testes)

#Resultados medios
print('\n\nAlgoritmo \t Campo Accession Ordenado \t Campo Accession Desordenado \t Campo Data Embaralhado')
resultados_medios = (getMediaLog(Ordenadores, n_testes))
for ordenador,resultado in resultados_medios.items():
    print(ordenador,resultado[0],resultado[1],resultado[2])

