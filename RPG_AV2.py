#Projeto de AV2 | Lógica de Programação - Ciência da Computação - UNINASSAU 2025.1 | Docente: Josivan
#Discentes: Marcelo Justino, Pedro Canto, Jonathan Gustavo, Carlos Henrique, Livia Moreno e Micaías Alexandre.
#Um jogo de dados onde você é um(a) aventureiro(a) que irá derrotar um dragão para proteger CodeVille!

#Importando a biblioteca random para os testes de dados, time para ter delay nas mensagens e climage para exibir o dragão
import random
import time 
import climage

#variável do dragão, função de parâmetro unicode para a imagem ser exibida mais vertical, width limita uma largura para existirem mais pixel na tela e melhorar a qualidade do dragão
#arte por Justino
dragao = climage.convert('dragao.jpg', is_unicode=True, width=150)


#Função Menu, primeiro chamamos ela no terminal
def exibeMenu():
    print("\n###### MENU - Salve CodeVille! ######")
    print("1 - Iniciar jogo")
    print("2 - Fechar jogo")
    print("3 - Alunos criadores")
    return input("Digite sua opção: ")

#Definindo parâmetros das variáveis da vida do jogador e do dragão (serão alterados conforme o resultado do teste de percepção)
def combateDragao(jogador_hp, dragao_hp, nome):


    print(f"\nFinalmente você encontrou o dragão, {nome}! Prepare-se para enfrentá-lo e salvar CodeVille!\n")

#Loop principal do jogo, ele acontecerá enquanto a vida do jogador e do dragão forem maiores que 0 (foram definidas nas variáveis acima e alterarão durante o combate)
    while jogador_hp > 0 and dragao_hp > 0:
        print(f"\n{nome}: {jogador_hp} | Dragão de Fogo: {dragao_hp}")

        # Loop para garantir que o jogador digite "1" para atacar
        while True:
            acao_ataque = input("Digite 1 para atacar o Dragão: ")
            if acao_ataque == "1":
                break
            print("Opção inválida. Digite 1 para atacar!")

        # Ataque do jogador (usuário), possibilidades de falha (<10), sucesso (>10) e sucesso crítico (20) - dano dobrado
        rolagem_ataque = rolar_dado()
        print(f"\nVocê rolou: {rolagem_ataque} para atacar!")

        if rolagem_ataque == 20:
            dano_jogador = random.randint(10, 25) * 2
            dragao_hp = dragao_hp - dano_jogador
            print(f"Um acerto CRÍTICO! DANO DOBRADO!\n Sua lâmina ultrapassa a armadura de escamas e você causou {dano_jogador} de dano ao dragão!")

        elif rolagem_ataque >= 10:
            dano_jogador = random.randint(10, 25)
            dragao_hp = dragao_hp - dano_jogador
            print(f"Você acerta sua lâmina no dragão! Causou {dano_jogador} de dano!")
        else:
            print("Você errou o ataque!")

        if dragao_hp <= 0:
            print(". . .")
            time.sleep(3)
            print(f"\nOs limites do impossível não existem quando se trada de você, {nome}!\n Alcance o inalcançável com ponta de sua espada!\n Você atravessa o peito do dragão em um último ataque heróico, perfurando seu coração e derrubando o dragão sem vida no chão quente da caverna. A poeira abaixa, o dragão morre e você trouxe um legado de paz e prosperidade para CodeVille! Parabéns!\n Fim de Jogo!")
            return

        # Ataque do dragão (terminal), possibilidades de falha (<10) e sucesso (>10)
        print("\nO Dragão prepara um contra-ataque!")
        rolagem_dragao = rolar_dado()
        print(f"\nDragão rolou: {rolagem_dragao} para atacar!")

        if rolagem_dragao >= 10:
            dano_dragao = random.randint(12, 20)
            jogador_hp = jogador_hp - dano_dragao
            print(f"O dragão acerta com uma bola de fogo! E causa {dano_dragao} de dano!")
        else:
            print("O dragão não conseguiu te atacar desta vez!")

        if jogador_hp <= 0:
            print(". . .")
            time.sleep(3)
            print(f"\nRelembre de suas aventuras, {nome}... esta foi sua jornada. Nem sempre os heróis terminam em finais felizes.\n Sua última visão em vida foi um poderoso ataque de chamas do dragão, que penetrou sua armadura, carne e osso... reduzindo seu corpo e suas memórias a cinzas... CodeVille perecerá igualmente.\n Fim de Jogo!")
            return
        
# Função do desafio do pântano, caso este caminho seja escolhido! É um aleatório
def desafioPantano():
    global vida_atual
    while vida_atual > 0:
        print(f"""  
                    Você encontra um rio de lama espessa. Para atravessar, precisa pular por pedras parcialmente submersas.
                    Algumas afundam sob o peso. Você deve escolher a pedra correta em três etapas. Um erro pode te afundar.
                                     
              """)

        pedras_certas = [random.randint(1, 3) for i_ in range(3)]
        sucesso = True

        for etapa in range(3):
            while True:
                escolha = input(f"\nEtapa {etapa + 1} - Escolha uma pedra (1, 2 ou 3):\n>> ")
                if escolha in ["1", "2", "3"]:
                    escolha = int(escolha)  # Evitando outras alternativas do usuário
                    break
                else:
                    print("Escolha inválida. Digite apenas 1, 2 ou 3.")


            if escolha == pedras_certas[etapa]:
                print("Pedra firme! Você avançou com sucesso.")
            else:
                print("Pedra falsa! Você afunda na lama pegajosa!")
                vida_atual = vida_atual - 1
                print(f"Você perde 1 ponto de vida. Vida atual: {vida_atual}")
                sucesso = False
                break  # Sai do loop das etapas para reiniciar o desafio

             

        if sucesso:
            print(dragao)
            print(f"\nVocê cruzou o pântano com sucesso! Sua vida atual é {vida_atual}")
            combateDragao(vida_atual, 120, nome)
        elif vida_atual <= 0:
            print("\nVocê pereceu ao Pântano Nebuloso, seu espírito afundará na lama pela eternidade. \nCodeVille continuará assombrada pelo Dragão....")
            time.sleep(2)
            print("Fim de Jogo. Retornando ao menu principal.")
            return
        else:
            print("\nVocê falhou no desafio. Tente novamente!")


#Desafio do Silêncio - Testes de avanço para passar a Coruja do Ártico
def desafio_silencio(vida_atual):
    print("""
    Após você ter escalado as montanhas geladas dos ventos
    você se depara com uma criatura imensa dormindo à frente, uma Coruja do Ártico Gigante!
    Você consegue ver que o terreno no qual ela descansa é muito irregular e cheio 
    de galhos, pedras e restos de animais, um passo em falso pode custar sua vida...

    Esse desafio funcionará da seguinte forma:
    Você terá essas opções por turno:
    -  Furtividade: anda com cuidado (+1 ruído caso não passe no teste)
    -  Atletismo: mais rápido, mas arriscado (+1 a 3 ruído aleatório caso não passe)   
    -  Parar: espera em silêncio (pode reduzir o ruído em -1)

    Acumule 10 avanços para escapar. Se ruído exceder 6... o monstro irá acordar!
    """)

# variáveis do avanço e ruído, retornarão com os testes do jogador
    avancos = 0
    ruido = 0

#loop dos avanços
    while avancos < 10:
        print(f"\nAvanços: {avancos}/10 | Ruído atual: {ruido}")
        escolha = input("Sua ação (Furtividade / Atletismo / Parar): ").strip().lower()

        if escolha == "furtividade":
            teste_furtividade = rolar_dado()
            print(f"Você rolou: {teste_furtividade + 1}")
            if teste_furtividade >= 10:
                avancos = avancos + 1
                print("🦶 Você anda com cuidado... sem problemas.")
            else:
                ruido = ruido + 1
                print("🦶 Você anda com cuidado... mas faz um pouco de barulho.")

        elif escolha == "atletismo":
            teste_atletismo = rolar_dado()
            print(f"O resultado do seu teste foi: {teste_atletismo - 3}")
            if teste_atletismo >= 10:
                barulho = random.randint(1, 3)
                ruido = ruido + barulho
                avancos = avancos + 3
                print(f"🏃 Você corre! Mas faz {barulho} de barulho.")
            else:
                barulho = random.randint(1, 3)
                ruido += barulho
                print(f"🏃 Você tenta correr, mas tropeça! Faz {barulho} de barulho.")

        elif escolha == "parar":
            if ruido > 0:
                ruido = ruido - 1
                print("🤫 Você respira fundo e espera... o ambiente silencia.")
            else:
                print("⏳ Já está silencioso. Esperar mais não ajuda.")
        else:
            print("⚠️ Ação inválida. Tente de novo.")
            continue

        if ruido >= 6:
            print(dragao)
            print("""
                  💀 O monstro se ergue, olhos brilhando de ódio! Com um urro que ecoa pelo Pantano!
                  sem te dar tempo para reagir ele começa avançando e te da um golpe desprevenido
                 """)
            
            vida_atual = vida_atual - 20
                
            print(f"☠️ Você perdeu 20 de vida! Vida atual: {vida_atual}")
            print("""
                  Golpe que você recebeu foi tão forte mais tão forte que você foi 
                  lançado até a entrada da caverna do dragão! É seu dia de sorte 
                  (talvez nem tanto...)!  """)
            combateDragao(vida_atual, 120, nome)
            return

    print("\n✅ Você passou sorrateiramente... sem acordar a criatura.")
    print(dragao)
    combateDragao(vida_atual, 120, nome)
    return


# essa função irá pegar o nome do jogador após ele dizer que quer jogar e chamar a função escolher caminho
def iniciarJogo():
    global nome
    global vida_atual
    nome =input("Diga-me seu nome, aventureiro(a): ").capitalize()
    vida_atual = 100  #Define a vida aqui (caso morra no pântano nebuloso)
    mostrarHistoria()
    escolherCaminho()


def rolar_dado():
    return random.randint(1, 20)

# Após selecionar que quer jogar, será chamado a função que mostra a historia
def mostrarHistoria():
    print(f"""
CodeVille é um vilarejo num reino distante.
E você, {nome}, acaba de chegar neste lugar à procura de suprimentos para continuar sua jornada.

A hospitalidade dos moradores lhe agrada — te deram água e abrigo quando você contou dos seus feitos
e mostrou seu acervo de itens colecionados nas missões passadas.

A empatia que teve com o povoado é tão grande que seu coração arde de coragem ao saber que aquele lugar
é atormentado por um terrível Dragão de Fogo.

Você se equipa com sua espada, armadura e coragem para ir até a caverna do dragão e salvar CodeVille dessa ameaça!
""")
# Após chamar a função da historia será chamado a de caminho, na qual será decidido o rumo do jogador
def escolherCaminho():
    print("\nVocê tem três caminhos possíveis para chegar até a caverna do Dragão:")
    print("1 - Floresta Sombria (atalho perigoso)")
    print("2 - Montanha dos Ventos (trilha longa e fria)")
    print("3 - Pântano Nebuloso (terreno traiçoeiro)")
    
#aqui temos um loop de repetição que retornará para a VARIAVEL CAMINHO quando não ser selecionado um valor válido

    while True:
        caminho = input("Escolha seu caminho (1, 2 ou 3): ")
        if caminho == "1":
         floresta_sombria()
         break
    
        elif caminho == "2":
            montanha_dos_ventos()
            break

        elif caminho == "3":
            pantano_nebuloso()
            break

        else:
            print("Opção inválida. Tente novamente.")
               


# ESCOLHA DA FLORESTA SOMBRIA
def floresta_sombria():
    print("""
          \/\/\/\/\/\/\/\/\/\[VOCÊ ESCOLHEU IR PELA FLORESTA SOMBRIA]/\/\/\/\/\/\/\/\/\/


          Você deixa para trás os muros protetores de CodeVille e adentra a Floresta sombria. A névoa é espessa
          como algodão molhado, e os galhos retorcidos parecem se mover quando você não está olhando. Cada passo  
          ecoa como um sussurro na floresta viva, como se ela estivesse te observando.
          
          Após caminhar por quase uma hora, você chega a uma clareira onde o caminho se divide em três trilhas.
          No centro, uma pedra com inscrições quase apagadas diz: 


        "Eis tríade da escolha: grite para o que há em frente,
          Apegue-se na essência da sua voz, somente...
          Seguir o reflexo é a verdadeira opção,
          Se a sua missão é derrotar o terrível dragão."

          Você decide testar os caminhos, um por um, fazendo um som forte
        """)
    
    print("Você decide testar os caminhos, um por um, fazendo um som forte.")


    print("\n[Testando a Trilha 1...]")
    time.sleep(6)
    print("""
          Você grita em direção à Trilha 1. Sua voz retorna com um ligeiro atraso e uma nota mais baixa
          como se a própria floresta tivesse engolido parte da energia. Há um sussurro etéreo que parece 
          seguir seu próprio som, murmurando algo indistinto.
          """)


    print("\n[Testando a Trilha 2...]")
    time.sleep(6)
    print("""
          Você grita em direção à Trilha 2. O som não ecoa. Em vez disso, a luz etérea no chão da clareira 
          pisca mais intensamente na entrada da trilha, e você sente um calor repentino, como se algo fosse 
          absorvido ali
          .""")

    print("\n[Testando a Trilha 3...]")
    time.sleep(6)
    print("""
          Você grita em direção à Trilha 3. Sua voz retorna instantaneamente, nítida e idêntica, como se
          você tivesse gritado para um espelho. É um reflexo perfeito, sem distorção ou perda
          """)  

    print("\nCom base nas inscrições da pedra, qual trilha você escolhe?")
    print("1 - A trilha do eco atrasado e sussurrante")
    print("2 - A trilha da luz intensa e do calor (sem eco)")
    print("3 - A trilha do reflexo perfeito do seu som")

#Loop para o jogador escolher o caminho da floresta
    while True:
        floresta_caminho = input("Qual caminho deseja seguir? (1, 2 ou 3): ")

        if floresta_caminho == "3": # RESPOSTA CERTA
            # Aqui chamará a próxima etapa da aventura após o enigma
            print(dragao)
            print(""" 
                  Você escolheu a trilha do reflexo perfeito, aventureiro! A luz na clareira se intensifica 
                  ao redor de seus pés e um caminho antes invisível se revela. Você desvendou o enigma!
                  
                  você avança pela floresta sem grandes problemas
                  """) 
            combateDragao(100, 120, nome)
            break
            
        elif floresta_caminho == "2":
            print("""
                  Assim que pisa na trilha, a névoa se fecha atrás de você. 
                  O chão desaparece e você cai num abismo sem fim.
                  Era uma armadilha mortal da floresta...
                    
                    """)
            break
        elif floresta_caminho == "1":
            
            print(dragao)
            print("""
                  
                  Você entra na trilha errada... raízes vivas agarram suas pernas e espinhos rasgam sua pele.
                  Você consegue escapar, mas está ferido.

                    Você recebeu 15 de dano das raízes.
                    """)
            combateDragao(85, 120, nome)
            break
        else:
            print("Opção invalida por favor, escreva novamente")
             

#Definindo função do caminho da montanha dos ventos
def montanha_dos_ventos():
    global vida_atual
    print("""
    \/\/\/\/\/\/\/\/\/\[Você decide enfrentar a Montanha dos Ventos.]/\/\/\/\/\/\/\/\/\/

    O ar se torna rarefeito à medida que você sobe. A trilha, esculpida entre rochas geladas e estreitas
    serpenteia entre abismos e penhascos cobertos de neve. Rajadas cortantes de vento uivam como lobos famintos
    tentando empurrá-lo de volta. Cada passo exige esforço. Seu corpo treme, mas sua vontade se mantém firme.

    O frio e o vento chicoteiam a Montanha dos Ventos, onde a trilha se torna traiçoeira. Em um platô rochoso
    um corvo de penas negras como a noite se empoleira, imóvel, seus olhos fixos em você. Ele não se move
    nem um pio, apenas observa em meio à nevasca. Uma placa quebrada na neve pouco ajuda.
     O corvo é a única coisa que se destaca nesta paisagem desoladora

    Você sente que a montanha testa não apenas sua força, mas também sua paciência... algo dorme ali.
    """)
       

    while True:
        escolha_montanha = input("O que você deseja fazer? (1 - Rolar intuição / 2 - Ignorar e seguir caminho): ")

        if escolha_montanha == "1":
            teste_intuicao = rolar_dado() + 2
            print(f"Você conseguiu: {teste_intuicao}!")
            if teste_intuicao >= 14:
                print("""
                        Você se aproxima do corvo e ele grasna alto, revelando com o olhar uma poção esverdeada.
                        Você bebe e se sente revigorado, seus pontos de vida aumentaram em 20!
                    """)
                vida_atual = vida_atual + 20
                return
            else:
                print("Nada pareceu interessante vindo dessa corvo... você segue o caminho normalmente. A caverna lhe aguarda.")
                desafio_silencio(vida_atual)

        elif escolha_montanha == "2":
            print("Você ignora o corvo e continua... mas uma tempestade te força a recuar e tentar outra rota.")
            desafio_silencio(vida_atual)

        else:
            print("Escolha inválida. Tente novamente.")


#Definindo função do caminho do pantano nebuloso
def pantano_nebuloso():
    print("""
        \/\/\/\/\/\/\/\/\/\[Você decide atravessar o Pântano Nebuloso.]/\/\/\/\/\/\/\/\/\/

        O solo mole suga seus pés a cada passo. A névoa é espessa, tingida de verde-claro, e parece viva. O ar tem um cheiro pútrido de coisas que apodrecem sob a superfície.
        Galhos secos estalam mesmo sem serem tocados. Você vê olhos se abrirem por um instante sob as águas paradas e lamacentas... e então desaparecem.

        O caminho desaparece em meio à neblina. Você está dentro de um labirinto natural — um quebra-cabeça de árvores retorcidas, pedras cobertas de musgo e poças traiçoeiras.

        Sombras sussurram direções contraditórias. Você precisa confiar em sua intuição… ou pagar o preço.
    """)
    desafioPantano()
     

# Loop principal para o jogo sair apenas se escolher fechar
while True:
    opcao = exibeMenu()
    if opcao == "1":
        iniciarJogo()
    elif opcao == "2":
        print("\nSaindo do jogo. O Dragão continuará aterrorizando CodeVille...")
        break
    elif opcao == "3":
        print("""  Alunos:
              Carlos Henrique
              Jonathan Gustavo
              Lívia Moreno
              Marcelo Justino
              Micaías Alexandre
              Pedro Canto \n""")
    else:
        print("Opção inválida! Tente novamente.")