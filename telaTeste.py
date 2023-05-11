import tkinter as tk
import array
import copy
import main

def proximo():
    global root 
    global Mensagem
    global predicao_on
    R = main.principal(predicao_on)
    Mensagem = main.mensagem()
    # Atualize os valores na tela novamente
    atualizar_tela(R, root)

def atualizar_tela(R, root):
    # Atualize os valores nos retângulos
    for i in range(len(R)):
        label = root.grid_slaves(row=i // 8, column=i % 8)[0]
        label.config(text="|R" + str(i) + " - " + str(R[i]) + "|")
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, Mensagem)


def toggle_predicao():
    global predicao_on
    predicao_on = not predicao_on
    if predicao_on:
        predicao_button.config(text="Predição: ON", bg="green")
    else:
        predicao_button.config(text="Predição: OFF", bg="red")

def create_window_with_values(values):
    # Crie a janela principal
    global root
    global text_area
    global predicao_on
    global predicao_button
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Banco de Registradores")

    # Crie uma grade de retângulos
    for i in range(4):
        for j in range(8):
            # Cada retângulo é um label com fundo branco e borda preta
            label = tk.Label(root, text="", width=10, height=5, bg="white", bd=1, relief="solid")
            # Coloque o label na grade
            label.grid(row=i, column=j, padx=5, pady=5)
            # Insira a numeração de cada registrador
            reg_num = (i * 8) + j
            label.config(text="|R" + str(reg_num)+" ")

    # Adicione os valores aos retângulos
    for i in range(len(values)):
        label = root.grid_slaves(row=i // 8, column=i % 8)[0]
        label.config(text="|R" + str(i) + " - " + str(values[i])+"|")


    #Adicionando caixa de texto
    text_area = tk.Text(root, height=6, width=80)
    text_area.grid(row=6, column=0, columnspan=8, padx=5, pady=5)
    text_area.insert(tk.END,'Bem vindo ! Aperte Continue para iniciar o processo')

    # Adicione os botões de confirmar e sair
    confirm_button = tk.Button(root, text="Continue", bg="green", fg="white", width=10, height=2,command=proximo)
    confirm_button.grid(row=4, column=6, padx=5, pady=5)
    quit_button = tk.Button(root, text="Sair", bg="red", fg="white", width=10, height=2, command=root.destroy)
    quit_button.grid(row=4, column=7, padx=5, pady=5)

    # Adicione o botão predição 
    predicao_on = False
    predicao_button = tk.Button(root, text="Predição: OFF", bg="red", fg="white", width=10, height=2, command=toggle_predicao)
    predicao_button.grid(row=4, column=5, padx=5, pady=5)
    

    # Execute a janela principal
    root.mainloop()


# Defina o array de valores
global text_area 
global root
R = array.array('I', [0] * 32) # banco de registradores
aAux=array.array('I', [0] * 32) 
create_window_with_values(R)