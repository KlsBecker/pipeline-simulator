#!/usr/bin/env python3
import array

aDados=[] #array que ira guardar as linhas do arquivo de texto
R = array.array('I', [0] * 32) # banco de registradores

#Função que executa leitura do arquivo txt e guarda linhas no array
def leituraArquivo():

    arquivo = open("teste.ASM")
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha)
        aDados.append(linha)
    arquivo.close()

def PrintRegistradores():
    print("Banco de Registradores -------------------------------------------------------------")
    for i in range(8):
        print(f"|R{i} - {R[i]} ", end="")
    print()
    for i in range(8, 16):
        print(f"|R{i} - {R[i]} ", end="")
    print()
    for i in range(16, 24):
        print(f"|R{i} - {R[i]} ", end="")
    print()
    for i in range(24, 32):
        print(f"|R{i} - {R[i]} ", end="")
    print()
    print("-----------------------------------------------------------------------------------")


class Instruction:
    def __init__(self, line=None):
        self.opCode = None
        self.op1    = None
        self.op2    = None
        self.op3    = None
        self.status = True

        if line:
            self.processInstruction(line)

    def processInstruction(self, line):
        instParts   = line.strip().split()
        self.opCode = instParts[0].lower()

        if self.opCode in ["addi", "subi"]:
            self.op1 = instParts[1]
            self.op2 = instParts[2]
            self.op3 = int(instParts[3])
        elif self.opCode in ["add", "sub"]:
            self.op1 = instParts[1]
            self.op2 = instParts[2]
            self.op3 = instParts[3]
        elif self.opCode == "beq":
            self.op1 = instParts[1]
            self.op2 = instParts[2]
            self.op3 = int(instParts[3])
        elif self.opCode == "b":
            self.op1 = int(instParts[1])
        elif self.opCode == "nop":
            pass
        else:
            raise ValueError(f"Unknown OpCode: {self.opCode}")

# Class used to control the pipeline of the processor
class Pipeline:
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

pipeline = Pipeline()

if __name__ == '__main__':

    # Reads the ASM code
    leituraArquivo()

    # Process the read code
    while True:
        pipeline.fetch()
        pipeline.decode()
        pipeline.execute()
        pipeline.memory()
        pipeline.writeBack()
        PrintRegistradores() # Imprime em tela o valor do banco de registradores




