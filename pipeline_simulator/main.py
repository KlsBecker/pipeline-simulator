
aDados=[] #array que ira guardar as linhas do arquivo de texto

#Função que executa leitura do arquivo txt e guarda linhas no array
def leituraArquivo():

    arquivo = open("teste.txt")
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha)
        aDados.append(linha)
    arquivo.close()

# Class used to control the pipeline of the processor
class pipeline:
    def __init__(self) -> None:
        pass

    def fetch(self) -> None:
        pass
    
    def decode(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def memory(self) -> None:
        pass

    def writeBack(self) -> None:
        pass

print('Imprimindo linhas do arquivo \n') #executa leitura do arquivo de texto 

leituraArquivo()

print('Imprimindo linhas do array \n') #executa leitura do arquivo de texto 



