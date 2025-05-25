#Projeto de AV2 | Lógica de Programação UNINASSAU 2025.1 | 
#Um jogo de dados onde você é um(a) aventureiro(a) que irá derrotar um dragão para proteger CodeVille!

#Importando a Biblioteca Random! 
import random

#Definindo Funções: Exibir Menu, Rolagem de dados aleatória e Iniciar o jogo.
def exibeMenu():
    print("\n###### MENU - Salve CodeVille! - ######")
    print('1 - Iniciar jogo')
    print('2 - História do mundo')
    print('3 - Fechar jogo')
    opcaomenu = input('Digite sua opção: ')
    return opcaomenu
def rolar_dado():
    return random.randint(1, 20)
def iniciarJogo():
    nome = input("Digite seu nome: ")


    # Laço de repetição para só iniciar se o usuário digitar 1
    while True:
        percepcao = input(f"{nome}, seus passos ecoam nos seus ouvidos. Você chegou na caverna. O frio da floresta sumiu ao descer, começou a esquentar.\nDigite 1 para Rolar Percepção: ")
        if percepcao == "1":
            break
        print("Opção inválida. Tente novamente.")

    teste_percepcao = rolar_dado()
    print(f"Você rolou: {teste_percepcao}!")

    if teste_percepcao == 20:
        # Laço de repetição para retornar ao teste.
        while True:
            ataque_crit = input("Acerto crítico! Você vê o dragão no fundo da caverna, estava quase perfeitamente camuflado... mas está dormindo, você tem a vantagem.\n Digite 1 para Rolar Ataque: ")
            if ataque_crit == "1":
                break
            print("Opção inválida. Tente novamente.")

        resultado_AC = rolar_dado()
        print(f"Você rolou: {resultado_AC}!")
        if resultado_AC >= 10:
            print(f"Um ataque preciso! Você empala o dragão, que se debate de dor e se debate, iniciando um voo rápido para fora da caverna, fugindo e deixando CodeVille em paz! Parabéns, {nome}!")
        elif resultado_AC == 20:
            print(f"Um ataque LENDÁRIO! Você salta pelas escamas do dragão, desviando do hálito flamejante. Com o fio da lâmina de sua espada, você arranca a cabeça do dragão e volta para CodeVille como um herói que será lembrado para sempre! Parabéns, {nome}!")
        else:
            print("Você erra o golpe e o dragão acorda furioso! Ele finca suas garras no seu peito, perfurando sua armadura e seu coração! Fim de Jogo!")

    elif teste_percepcao >= 10:
        # Laço de repetição para retornar ao teste.
        while True:
            esquiva = input("Você escuta sons de algo se movendo no fundo da caverna, a luz vinda de uma fenda parece anormal... é a boca do dragão, pronta para cuspir fogo em você! Digite 1 para Rolar Esquiva!: ")
            if esquiva == "1":
                break
            print("Opção inválida. Tente novamente.")

        teste_esquiva = rolar_dado()
        print(f"Você rolou: {teste_esquiva}!")
        if teste_esquiva >= 10:
            # Laço de repetição para retornar ao teste
            while True:
                ataque = input("Com uma reação rápida, você desviou do ataque do dragão! Agora é hora de se vingar!\nDigite 1 para Rolar Ataque e derrotar o Dragão!: ")
                if ataque == "1":
                    break
                print("Opção inválida. Tente novamente.")

            teste_ataque = rolar_dado()
            print(f"Você rolou: {teste_ataque}!")
            if teste_ataque >= 10:
                print(f"Um ataque preciso! Você empala o dragão, que se debate de dor e sente medo, iniciando um voo rápido para fora da caverna, fugindo e deixando CodeVille em paz! Parabéns, {nome}!")
            elif teste_ataque == 20:
                print(f"Um ataque LENDÁRIO! Você salta pelas escamas do dragão, desviando do hálito flamejante. Com o fio da lâmina de sua espada, você arranca a cabeça do dragão e volta para CodeVille como um herói que será lembrado para sempre! Parabéns, {nome}!")
            else:
                print("Seu ataque foi fraco, a área escamosa que você tentou perfurar é mais resistente que a melhor de suas armaduras. O dragão te atinge logo depois com um ataque flamejante, você se torna cinzas ao vento. Fim de Jogo.")
        else:
            print(f"Você não conseguiu desviar, {nome}. O dragão te incinera com uma bola de fogo. Fim de Jogo.")
    else:
        print("Nada parece anormal, você suspeita que os moradores mentiram para você - Mas é tarde demais, o Dragão aparece atrás de você, é impossível se defender. Você é alvejado por uma grande labareda da boca do dragão e incendiado a cinzas. Fim de Jogo!")

# Definir função de mostrar a lore de CodeVille.
def mostrarHistoria():
    print("\nCodeVille é um vilarejo num reino distante. E você, aventureiro(a), acaba de chegar neste lugar a procura de suprimentos para continuar sua jornada. A hospitalidade dos moradores lhe agrada, te deram água e abrigo quando você contou dos seus feitos e mostrou seu acervo de itens colecionados nas missões passadas. A empatia que teve com o povoado é tão grande, que seu coração arde de coragem ao saber que aquele lugar é atormentado por um terrível Dragão de Fogo. Você se equipa com sua espada, armadura e coragem para ir até a caverna do dragão e salvar CodeVille dessa ameaça!")


#Loop de repetição do jogo, para só finalizar se escolherem a opção 3.
while True:
    opcaomenu = exibeMenu()

    if opcaomenu == "1":
        iniciarJogo()

    elif opcaomenu == "2":
        mostrarHistoria()

    elif opcaomenu == "3":
        print("Saindo do jogo. O Dragão continuará aterrorizando CodeVille...")
        break

    else:
        print("Opção inválida! Tente novamente.")
