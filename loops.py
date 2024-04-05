# def conta_ate_20():
#     for i in range(1, 21):
#         print(i)

# conta_ate_20()

def limitar_contador(valor_usuario):
    num = 0
    while num <= valor_usuario:
        print(num)
        num+= 1

num_do_usuario = int(input("Digite o numero final: "))

limitar_contador(num_do_usuario)