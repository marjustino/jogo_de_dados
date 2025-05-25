# Projeto de AV2 - Lógica de Programação | Uninassau | CDC 2025.1 Manhã
# Você é um(a) aventureiro(a) numa caverna escura a procura de um terrível dragão que aterroriza o reino!
# MENU | Caverna - (PERCEPÇÃO) - Encontrar|NãoEncontrar o Dragão | Encontrar -> Lutar | nãoEcontrar -> Dragão executa 
import random

testePerc = random.randint(1, 20)
testeEsq = random.randint(1, 20)
testeAtq = random.randint(1, 20)
dados = random.randint(1, 20)


def exibeMenu():
    print("###### MENU - Salve CodeVille! - ######")
    print('1 - Iniciar jogo')
    print('2 - História do mundo')
    print('3 - Fechar jogo')
    menuoption = int(input('Digite sua opção: '))
    return menuoption

menuoption = exibeMenu() 

if menuoption == 1:   
    def rollPerception():
        nome = str(input("Digite seu nome: "))
        a = int(input(f"{nome}, seus passos ecoam nos seus ouvidos. Você chegou na caverna. O frio da floresta sumiu ao descer, começou a esquentar. Digite 1 para Rolar Percepção: "))
        if a == 1:
            print(f"Você rolou: {testePerc}")
            if testePerc >= 10:
                b = int(input("Você escuta sons de algo se movendo no fundo da caverna, a luz vinda de uma fenda parece anormal... é a boca do dragão, pronta para cuspir fogo em você! Digite 1 para Rolar Esquiva!: "))
                if b == 1:
                    print(f"Você rolou: {testeEsq}")
                if testeEsq >= 10:
                    c = int(input("Você desviou! Agora é hora de se vingar! Digite 1 para Rolar Ataque e derrotar o Dragão!: "))
                    if c == 1:
                        print(f"Você rolou {testeAtq}")
                if testeEsq < 10:
                    print("Você tenta correr, mas o poder de fogo do dragão é maior do que tudo que você já viu. Em um piscar de olhos, sua visão é tomada pela chama do dragão e sua vida esvai em cinzas. Fim de Jogo!")
                    exibeMenu()
            if testePerc == 20:
                a = int(input("Acerto crítico! Você vê o dragão no fundo da caverna, estava quase perfeitamente camuflado... mas está dormindo, você tem a vantagem, Digite 1 para Rolar Ataque!"))
                if a ==1:
                    print(f"Você rolou: {dados}")
                    if dados >= 10:
                        print(f"Um ataque preciso! Você empala o dragão, que se debate de dor e se debate, inicando um voo rápido para fora da caverna, fugindo e deixando CodeVille em paz! Parabéns, {nome}")
                    if dados == 20:
                        print(f"Um ataque LENDÁRIO! Você salta pelas escamas do dragão, desviadno do hálito flamejante. Com o fio da lâmina de sua espada, você arranca a cabeça do dragão e volta para CodeVille como um herói que será lembrado para sempre! Parabéns, {nome}")
            elif testePerc < 10:
                print("Nada parece anormal, você suspeita que os moradores mentiram para você - Mas é tarde demais, o Dragão aparece atrás de você, é impossível se defender. Você é alvejado por uma grande labareda da boca do dragão e incendiado a cinzas. Fim de Jogo!")
                exibeMenu()
        else:
            print("Opção inválida! Tente novamente: ")
            rollPerception()

    rollPerception()

if menuoption == 2:
    print("CodeVille é um vilarejo num reino distante. E você, aventureiro(a), acaba de chegar neste lugar a procura de suprimentos para continuar sua jornada. A hospitalidade dos moradores lhe agrada, te deram água e abrigo quando você contou dos seus feitos e mostrou seu acervo de itens colecionados nas missões passadas. A empatia que teve com o povoado é tão grande, que seu coração arde de coragem ao saber que aquele lugar é atormentado por um terrível Dragão de Fogo. Você se equipa com sua espada, armadura e coragem para ir até a caverna do dragão e salvar CodeVille dessa ameaça!")
    exibeMenu()

if menuoption == 3:
    print("O Dragão continuará aterrorizando CodeVille...")

else:
    print("Opção inválida, tente novamente")
    exibeMenu()