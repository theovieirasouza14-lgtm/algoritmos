#Crie um menu de sistema que só encerra a app quando o usuario escolher

print("_"*25)
print("| .: MENU DE SISTEMA :. |")
print("-"*25)

while (True): #TRUE diz pra ja sair fazendo alguma coisa e depois teste 
    print("Menu")
    print("1 - Cadastrar")
    print("2 - Editas")
    print("3 - Deletar") 
    print("4 - Exibir")
    print("9 - Sair")
    try:   #tratamento de erro/exeção, nao quero que quebre meu codigo se o usuario clicar em algo errado.
        op_menu=int(input("Digite a opçao desejada: ")) #Variavel de OPÇÂO desejada.
    except ValueError:
        print("Erro: opção inválida! Tente novamente!")
        continue
    if op_menu > 4 and op_menu < 9 or op_menu>9 or op_menu<1:
        print("Erro: opção inválida! Tente novamente!")
        
    match op_menu:  # é como se fosse um if, uma escolha - em pseudocodigo, seria o ESCOLHA 
        case 1: 
            print("Iniciar Cadastro")
        case 2:
            print("Iniciat Edição")
        case 3:
            print("Deletar Cadastro")
        case 4:
            print("Listar Cadastro")            
    
    if op_menu != 9     #Pra falar que so sair do menu quando o 9 for digitado.
        continue 
    else:
        print("\nAplicação encerrada pelo usário!\n")
        break
