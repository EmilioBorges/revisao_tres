# def imprimir_nomes():
#     nome = ['João', "Maria","Fulano","Ana"]

#     print(f'1 - {nome[0]}\n2 - {nome[1]}\n3 - {nome[2]}\n4 - {nome[3]}')
#     print(f'1 - {nome[0]} 2 - {nome[1]}3 - {nome[2]}4 - {nome[3]}')

    

# imprimir_nomes()


# def primeiro_ultimo_nome():
#     nome = ['Emilio','Ana','Thor','Bia']

#     print(f'1 - {nome[0]}\n4 - {nome[3]}')

# primeiro_ultimo_nome()

# def segundo_terceiro_nome():
#     nome = ['Carlos','Ana','Thor','Bia']

#     print(f'2 - {nome[1]}\n3 - {nome[2]}')

# segundo_terceiro_nome()

def substitui_elemento(alim_1, alim_2, alim_3):
    alimentos= ['Arroz','Batata','Feijão']

    alimentos[0] = alim_1
    alimentos[1] = alim_2
    alimentos[2] = alim_3

    print(f'Lista de Alimentos atualizada: {alimentos}')

alimento_1 = input("Dgite o primeiro elemento: ")
alimento_2 = input("Dgite o segundo elemento: ")
alimento_3 = input("Dgite o terceiro elemento: ")

substitui_elemento(alimento_1, alimento_2, alimento_3)



