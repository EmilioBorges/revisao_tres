import random

def jokenpo():

    print('Ben-vindo ao Kokenpo!\n')
    print('Escolha uma opção para jogar: \n')
    print('[0] Pedra\n[1] Papel\n[2] Tesoura\n')    

    opcoes_do_jogo = ['Pedra','Papel','Tesoura']

    while True:
        numeros = random.randint(0,2)   

        opcao_jogador = int(input('Digite sua escolha: '))
        print('\n')
        print('JO KEN POHH!!!\n')
        print('=-----=------=-----=----=----=')

   
        print(f'O computador escolheu: {opcoes_do_jogo[numeros]}')
        print(f'O jogador escolheu: {opcoes_do_jogo[opcao_jogador]}')
        print('=-----=------=-----=----=----=')

        if numeros == 0 and opcao_jogador == 2:
            print('Computador venceu!\n')
        elif numeros == 0 and opcao_jogador == 1:
            print('Jogador venceu!\n')
        elif numeros == 1 and opcao_jogador == 0:
            print('Computador venceu!\n')
        elif numeros == 1 and opcao_jogador == 2:
            print('Jogador venceu!\n')
        elif numeros == 2 and opcao_jogador == 1:
            print('Computador venceu!\n')
        elif numeros == 2 and opcao_jogador == 0:
            print('Jogador venceu!\n')
        else:
            print('Tivemos um empate\n')
        
        sair = input('Deseja jogar novamente? (s/n): ').lower().startswith('s')
        if sair is False:
            break


jokenpo()