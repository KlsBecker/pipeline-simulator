
aDados=[] #array que ira guardar as linhas do arquivo de texto

#Função que executa leitura do arquivo txt e guarda linhas no array
def leituraArquivo():

    arquivo = open("teste.txt")
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha)
        aDados.append(linha)
    arquivo.close()


print('Imprimindo linhas do arquivo \n') #executa leitura do arquivo de texto 

leituraArquivo()

print('Imprimindo linhas do array \n') #executa leitura do arquivo de texto 



