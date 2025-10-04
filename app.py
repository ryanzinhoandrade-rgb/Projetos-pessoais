nome = input("Digite seu nome para começar o jogo: ")
idade = int(input("Qual sua idade para jogar:"))

idade >= 18
    

if idade >= 18:
    print(f"Bem vindo, {nome}! Você é maior de idade, pode jogar!")
    import random
    while True:
        print("\nVamos jogar pedra, papel e tesoura!")
        print("Escolha uma opção: ")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        opcao = int(input("Digite o número da sua escolha:"))
        opcoes = ["pedra", "papel", "tesoura"]
        computador = random.choice(opcoes)
        if opcao == 1:
            jogador = "pedra"
        elif opcao == 2:
            jogador = "papel"
        elif opcao == 3:
            jogador = "tesoura"
        else:
            jogador = "inválido"
            print("Opção inválida! Tente novamente.")
            continue
        print(f"Você escolheu: {jogador}")
        print(f"O computador escolheu: {computador}")
        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or (jogador == "papel" and computador == "pedra") or (jogador == "tesoura" and computador == "papel"):
            print("Você ganhou!")
        else:
            print("O computador ganhou!")
        sair = input("Deseja sair do jogo? (s/n): ").lower()
        if sair == 's':
            break
    print("Obrigado por jogar!")
else:
    print(f"Você é menor de idade, {nome}. Você não pode jogar!")

