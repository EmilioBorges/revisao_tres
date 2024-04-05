# def conta_ate_20():
#     for i in range(1, 21):
#         print(i)

# conta_ate_20()

# def limitar_contador(valor_usuario):
#     num = 0
#     while num <= valor_usuario:
#         print(num)
#         num+= 1

# num_do_usuario = int(input("Digite o numero final: "))

# limitar_contador(num_do_usuario)

# def tabuada_2():
#     for i in range(0,11):
#         print(f'{i} + {2} = {i+2}')


# tabuada_2()

def multiplicar(num):
    for i in range(0,11):
        print(f'{num} x {i} = {i*num}')

num_do_usuario = int(input("Digite o numero que deseja multiplicar: "))
multiplicar(num_do_usuario)