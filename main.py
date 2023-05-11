#!/usr/bin/env python3
import array



aDados=[] #array que ira guardar as linhas do arquivo de texto
R = array.array('I', [0] * 32) # banco de registradores
predicao =array.array('I', [0] * 32)  # Inicializa a tabela com 32 bits em zero
#predicao = bytearray(32) # tabela de predicao
PC = 0 # Program Counter 
txt =''
predicao_ativa=False

#Função que executa leitura do arquivo txt e guarda linhas no array
def leituraArquivo():

    arquivo = open("teste.txt")
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha)
        aDados.append(linha)
    arquivo.close()

def PrintRegistradores():
    print("Banco de Registradores -------------------------------------------------------------")
    for i in range(8):
        print(f"|R{i} -  {R[i]} ", end="")
    print()
    for i in range(8, 10):
        print(f"|R{i} -  {R[i]} ", end="")
    for i in range(10, 16):
        print(f"|R{i} - {R[i]} ", end="")
    print()
    for i in range(16, 24):
        print(f"|R{i} - {R[i]} ", end="")
    print()
    for i in range(24, 32):
        print(f"|R{i} - {R[i]} ", end="")
    print()
    print("-----------------------------------------------------------------------------------")
    return R
   


class Instrucao:
    def __init__(self):
        self.Opcode = ""
        self.Op1    = ""
        self.Op2    = ""
        self.Op3    = ""
        self.valorTemp1  = ""
        self.valorTemp2  = ""
        self.valorTemp3  = ""
        self.status = True

# Instruções nos estágios do pipeline
instBusca = Instrucao()
instDecod = Instrucao()
instExec = Instrucao()
instMem = Instrucao()
instWb = Instrucao()


def busca():  
    global PC
    global txt 
    global predicao
    print("Etapa de Busca --------------------------------------------------------------------- \n\r")
    instBusca.Opcode = 'NOP'
    instParts = aDados[PC].strip().split()
    instBusca.Opcode = instParts[0].lower()

    if predicao_ativa:
        # Adiciona predição bimodal
        pred_idx = PC % 32
        pred_value = predicao[pred_idx]

        if pred_value == 0:
            # Predição "Não Tomado"
            PC += 1
        else:
            # Predição "Tomado"
            inst_type = instBusca.Opcode.upper()
            if inst_type in ["B", "BEQ"]:
                PC += int(instParts[-1])
            else:
                PC += 1

        # Atualiza a tabela de predição bimodal
        if inst_type in ["B", "BEQ"]:
            target_pc = PC - 1 + int(instParts[-1])
            target_idx = target_pc % 32
            if target_pc == PC:
                predicao[pred_idx] = min(predicao[pred_idx] + 1, 3)
            else:
                predicao[target_idx] = max(predicao[target_idx] - 1, 0)
                predicao[pred_idx] = max(predicao[pred_idx] - 1, 0)


    if instBusca.Opcode.upper() in ["ADDI", "SUBI"]:
        instBusca.Op1 = int(instParts[1][2:5].replace(",",""))
        instBusca.Op2 = int(instParts[2][2:5].replace(",",""))
        instBusca.Op3 = int(instParts[3])
    elif instBusca.Opcode.upper() in ["ADD", "SUB"]:
        instBusca.Op1 = int(instParts[1][2:5].replace(",",""))
        instBusca.Op2 = int(instParts[2][2:5].replace(",",""))
        instBusca.Op3 = instParts[3]
    elif instBusca.Opcode.upper() == "BEQ":
        instBusca.Op1 = int(instParts[1][2:5].replace(",",""))
        instBusca.Op2 = int(instParts[2][2:5].replace(",",""))
        instBusca.Op3 = int(instParts[3])
    elif instBusca.Opcode.upper() == "B":
        instBusca.Op1 = int(instParts[1])
    elif instBusca.Opcode.upper() == "NOP":
         instBusca.Op1 =0
         instBusca.Op2 =0
         instBusca.Op3 =0 
    pass
    print("Memoria ", aDados[PC])
    print("PC \n", PC)
    print("Opcode \n", instBusca.Opcode.upper())
    print("Operando 1  \n", instBusca.Op1)
    print("Operando 2  \n", instBusca.Op2)
    print("Operando 3  \n", instBusca.Op3)
    txt ="Memoria: " + aDados[PC] + '\n' + 'PC: ' + str(PC) + '\n'+'Operando 1 : ' + str(instBusca.Op1) +'\nOperando 2 : ' +str(instBusca.Op2) +'\nOperando 3 : '+str(instBusca.Op3)
    PC += 1
    print("------------------------------------------------------------------------------------ \n\r")
    pass

def decodifica():
    print("Etapa de Decodificação ------------------------------------------------------------- \n\r")
    global instDecod 
    global PC
    instDecod = instBusca
    if instDecod.Opcode != '':
        if instDecod.Opcode.upper() == 'B':
            instDecod.valorTemp1 = abs(instDecod.Op1)-1
        else:
            instDecod.valorTemp2 = R[instDecod.Op2]
            if instDecod.Opcode.upper() == 'ADDI' or instDecod.Opcode.upper() == 'SUBI':
                instDecod.valorTemp3 = instDecod.Op3
            else:
                instDecod.valorTemp3 = instDecod.Op3
                instDecod.valorTemp1 = R[instDecod.Op1]
                instDecod.valorTemp2 = R[instDecod.Op2]
    print("------------------------------------------------------------------------------------ \n\r")
    pass

def executa():
    global instExec
    global PC 
    instExec = instDecod
    if (instExec.Opcode.upper() == 'ADDI') or (instExec.Opcode.upper() == 'ADD'):
        instExec.valorTemp1 = instExec.valorTemp2 + instExec.valorTemp3

    if (instExec.Opcode.upper() == 'SUBI') or (instExec.Opcode.upper() == 'SUB'):
        instExec.valorTemp1 = instExec.valorTemp2 - instExec.valorTemp3

    #Instruções de desvio
    if (instExec.Opcode.upper() == 'BEQ' ):
        if (instExec.valorTemp1 == instExec.valorTemp2):
            PC = int((2**instExec.valorTemp3/4))
            print(PC)
    if (instExec.Opcode.upper() == 'B'):
        PC = instExec.valorTemp1

def memoria():
    global instMem
    print("Etapa de Acesso Memória ------------------------------------------------------------ \n")
    instMem = instExec 
    print("------------------------------------------------------------------------------------ \n\r")
    pass


def writeBack():
    global instWb
    print("Etapa de Escrita Resultados -------------------------------------------------------- \n\r")
    instWb = instMem
    # Permito apenas instruções que  escrevem o resultado no registrador 
    if ((instWb.Opcode.upper() == 'ADDI') or (instWb.Opcode.upper() == 'ADD') or  (instWb.Opcode.upper() == 'SUBI') or (instWb.Opcode.upper() == 'SUB')):
        R[instWb.Op1] = instWb.valorTemp1
    print("------------------------------------------------------------------------------------ \n\r")
    pass



    # Realiza a Leitura do arquivo txt
leituraArquivo()

#while True:

def principal(predicao_on):
    global predicao_ativa 
    predicao_ativa = predicao_on
    
    busca()   # busca 
    decodifica()  # Decodifica Instrução 
    executa() # Executa instrução 
    memoria() # Acessa Memoria 
    writeBack() #escrita Nos registradores 
    return PrintRegistradores() # Imprime em tela o valor do banco de registradores
   
def mensagem():
    return txt