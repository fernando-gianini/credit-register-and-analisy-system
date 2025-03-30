# Sistema de Cadastro e Verificação de Empréstimos - Teminal

# 1. ** Cadastrar e Armazenar Usuários **
#     Permite que o usuário insira seu nome, renda mensal e histórico de crédito e armazene em um diciário.
def cadastro_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    renda = float(input("Digite sua renda mensal: "))
    historico = input("Possui historico de crédito? (s/n): ")

    print("Usuario cadastrado com sucesso")

    return {"nome": nome, "idade": idade, "renda": renda, "historico": historico}

# usuario = cadastro_usuario()
# print(usuario)
# # 2. ** Verificar Elegibilidade de Empréstimo **
#   Usa operadores relacionais e lógicos para verificar se o usuário é elegivel para um emprestimo.
#   Condições para ser elegivel: estar cadastrado, idade maior de 18, renda maior que 1000 e historico de credito existente.
# 
def elegibilidade():
    usuario_cadastro = input(f"Digite seu nome para verificar a elegibilidade: ")
    for usuario in usuarios:

        if usuario_cadastro == usuario["nome"]:
            if usuario["idade"] >= 18 and usuario["renda"] > 1000 and usuario["historico"] == "s":
                print("Você é elegível para um empréstimo")
                
            else:
                print("Você não é elegível para um empréstimo")
            break    
    else:
        print("Usuario não cadastrado")
     
# 3. ** Exibição do Usuario **
#  Retona todas as informações cadastradas de um único usuário.
# Condicinal se esta cadastrado
        #Se V Devolver a info
        #Se F Retornar "Usuario não cadastrado"

def exibir_usuario():
    mostrar_usuario = input(f"Digite seu nome para verificar o cadastro: ")
    for usuario in usuarios:

        if mostrar_usuario == usuario["nome"]:
            print(usuario)
            break
    else:
        print("Usuario não cadastrado")

 

# 4. ** Exibição da base de Usuários **
#  Exibe o número total de usuarios e os nomes dos usuarios.

##def exibir_usuarios():
    # usuarios = []
    # usuarios.append(usuario)
    # for i in usuarios:
    #     print(i)
    #For iterar/percorrer o dicionario e devolver o total de usuarios e todos os nomes cadastrados
        # * funcao len() para contar o total de usuarios

usuarios = []

while True:
    opcao = input(""" Digite a opção desejada: 
1 - Cadastrar Usuário,
2 - Verificar Elegibilidade
3 - Exibir Usuário
4 - Exibir Usuários
5 - Sair: 
""")

    match opcao:
        case "1":
            usuario = cadastro_usuario()
            usuarios.append(usuario)
        case "2":
            elegibilidade()
        case "3":
            exibir_usuario()
        case "4":
            print(usuarios)
        case "5":
            break
    


