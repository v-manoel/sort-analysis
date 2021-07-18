import csv

#Leitura do arquivo e criação de listas
def lerArquivoTeste():
    with open("dados.csv") as csvfile:
        arquivo_dados = csv.reader(csvfile,delimiter =';')
        coluna_access = []
        coluna_data = []
    
        next(arquivo_dados)
        for line in arquivo_dados:
            coluna_access.append(line[0])
            if line[4] != 'N/A':
                coluna_data.append(int(line[4]))
            else:
                coluna_data.append(0)
        coluna_accessDec = coluna_access.copy()
        coluna_accessDec.sort(reverse =True)
    return [coluna_access,coluna_accessDec,coluna_data]

#Criar copia de listas para testes
def getCamposTestes(campos):
    copia = campos.copy()
    return copia

#Criar arquivo de log com cabeçalho
def setArqLog(*cabecalho):
    with open("LogOrdenadores.csv",'w', newline ='') as logfile:
        gravar_dados = csv.writer(logfile, delimiter =';')
        gravar_dados.writerow([campo for campo in cabecalho])
        
#Gravar resultados parciais
def apendArqLog(algoritmo, resultados_parciais):
    linha = resultados_parciais.copy()
    linha.insert(0,algoritmo)
    with open("LogOrdenadores.csv",'a+', newline ='') as logfile:
        gravar_dados = csv.writer(logfile, delimiter =';')
        gravar_dados.writerow([campo for campo in linha])
        
#Calcular resultado médio
def getMediaLog(algoritmos,n_testes):
    resultados_finais = {}
    for algoritmo in algoritmos.keys():
        resultados_finais[algoritmo] = [0.0,0.0,0.0]
            
    with open("LogOrdenadores.csv",'r', newline ='') as logfile:
        ler_dados = csv.reader(logfile, delimiter =';')
        next(ler_dados)
            
        for linha in ler_dados:
            resultados_finais[linha[0]] = [i + float(j) for i,j in zip(resultados_finais[linha[0]],linha[1:])]
        
    for algoritmo in resultados_finais.keys():
        resultados_finais[algoritmo] = [f'{j/n_testes:.8f}' for j in resultados_finais[algoritmo]]
    return resultados_finais
                