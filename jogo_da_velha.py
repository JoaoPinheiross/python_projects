#-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-

# Função para colocar o X no tabuleiro.
def jogarX(tabuleiroReal):
    existe = True  # Variável para verificar se o número está no tabuleiro.
    print("Vez do X")

    # Loop para entrada do local aonde vai ser jogado.
    while True:
        l = 0  # Linha do tabuleiro.
        c = 0  # Coluna do tabuleiro.

        # Primeiro tenta rodar o código, caso tenha entrada de um valor errado é informado ao usuário.
        try:
            local = int(input("Digite o local onde quer jogar: "))  # Entrada do local a ser jogado.
            tabuleiro = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]  # Tabuleiro base.

            # Passa por todas as linhas e colunas à procura do local.
            for linha in tabuleiro:
                    for coluna in linha:

                        # Caso seja encontrado é verificado se o valor já está ocupado e retornado o valor se não estiver.
                        if coluna == local:
                            if not verificarOcupado(tabuleiroReal, l, c):
                                tabuleiroReal[l][c] = "X"
                                return tabuleiroReal
                            else:
                                print("Este local está ocupado, tente outro.\n")

                        # define que não tem o local com o valor entrado.
                        else:
                            existe = False
                        c += 1
                    l += 1
                    c = 0
            if not existe:
                print("Local inválido, tente novamente.\n")
        except:
            print("Local inválido, tente novamente.\n")
#-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-

# Função para colocar o O no tabuleiro.
def jogarO(tabuleiroReal):
    existe = True  # Variável para verificar se o número está no tabuleiro.
    print("Vez do O")

    # Loop para entrada do local aonde vai ser jogado.
    while True:
        l = 0  # Linha do tabuleiro.
        c = 0  # Coluna do tabuleiro.

        # Primeiro tenta rodar o código, caso tenha entrada de um valor errado é informado ao usuário.
        try:
            local = int(input("Digite o local onde quer jogar: "))  # Entrada do local a ser jogado.
            tabuleiro = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]  # Tabuleiro base.

            # Passa por todas as linhas e colunas à procura do local.
            for linha in tabuleiro:
                    for coluna in linha:

                        # Caso seja encontrado é verificado se o valor já está ocupado e retornado o valor se não estiver.
                        if coluna == local:
                            if not verificarOcupado(tabuleiroReal, l, c):
                                tabuleiroReal[l][c] = "O"
                                return tabuleiroReal
                            else:
                                print("Este local está ocupado, tente outro.\n")

                        # define que não tem o local com o valor entrado.
                        else:
                            existe = False
                        c += 1
                    l += 1
                    c = 0
            if not existe:
                print("Local inválido, tente novamente.\n")
        except:
            print("Local inválido, tente novamente.\n")
#-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-

# função que verifica se o local já esta ocuapdo.
def verificarOcupado(tabuleiroReal, l, c):
    # Se o local estiver com a string "X" ou "O" é definido como ocupado e esse valor é retornado.
    if tabuleiroReal[l][c] == "X" or tabuleiroReal[l][c] == "O":
        ocupado = True
    else:
        ocupado = False
    return ocupado
#-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-

# Função para definir as condições de vitória e as mensagens.
def condVitoria(tabuleiro, tabuleiroD):
    # Verifica se três casas especificas estão ocupadas com o mesmo valor para definir se o jogo foi ganho. Dependendo de qual o valor é imprimido uma mensagem diferente.
    if tabuleiro[0][0] == tabuleiro[0][1] and tabuleiro[0][0] == tabuleiro[0][2]:
        print(tabuleiroD)
        j = 10
        if tabuleiro[0][0] == "X":
            print("Parabéns! O jogador X ganhou!")
        else:
            print("Parabéns! O jogador O ganhou!")
        return True
    elif tabuleiro[1][0] == tabuleiro[1][1] and tabuleiro[1][0] == tabuleiro[1][2]:
        print(tabuleiroD)
        j = 10
        if tabuleiro[1][0] == "X":
            print("Parabéns! O jogador X ganhou!")
        else:
            print("Parabéns! O jogador O ganhou!")
        return True
    elif tabuleiro[2][0] == tabuleiro[2][1] and tabuleiro[2][0] == tabuleiro[2][2]:
        print(tabuleiroD)
        j = 10
        if tabuleiro[2][0] == "X":
            print("Parabéns! O jogador X ganhou!")
        else:
            print("Parabéns! O jogador O ganhou!")
        return True
    elif tabuleiro[0][0] == tabuleiro[1][0] and tabuleiro[0][0] == tabuleiro[2][0]:
        print(tabuleiroD)
        j = 10
        if tabuleiro[0][0] == "X":
            print("Parabéns! O jogador X ganhou!")
        else:
            print("Parabéns! O jogador O ganhou!")
        return True
    elif tabuleiro[0][1] == tabuleiro[1][1] and tabuleiro[0][1] == tabuleiro[2][1]:
        print(tabuleiroD)
        j = 10
        if tabuleiro[0][1] == "X":
            print("Parabéns! O jogador X ganhou!")
        else:
            print("Parabéns! O jogador O ganhou!")
        return True
    elif tabuleiro[0][2] == tabuleiro[1][2] and tabuleiro[0][2] == tabuleiro[2][2]:
        print(tabuleiroD)
        j = 10
        if tabuleiro[0][2] == "X":
            print("Parabéns! O jogador X ganhou!")
        else:
            print("Parabéns! O jogador O ganhou!")
        return True
    elif tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]:
        print(tabuleiroD)
        j = 10
        if tabuleiro[0][0] == "X":
            print("Parabéns! O jogador X ganhou!")
        else:
            print("Parabéns! O jogador O ganhou!")
        return True
    elif tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][2] == tabuleiro[2][0]:
        print(tabuleiroD)
        j = 10
        if tabuleiro[0][2] == "X":
            print("Parabéns! O jogador X ganhou!")
        else:
            print("Parabéns! O jogador O ganhou!")
        return True
#-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-

# Função que começa e termina o jogo.
def jogo(X, O):
    tabuleiro = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]  # Tabuleiro
    tabuleiroD = f"""  # Desenho do tabuleiro
    +-----------+                                                 
    | {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} | 
    | {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} | 
    | {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} | 
    +-----------+                                                 
    """                                                           
    jogadas = 0  # Jogada atual

    # Laço do funcionamento do jogo
    while jogadas < 9:

        # Se a jogada atual for par, será a vez do X, se for impar é impar
        if jogadas % 2 == 0:
            print(tabuleiroD)
            tabuleiro = X(tabuleiro)
            tabuleiroD = f"""
    +-----------+
    | {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} |
    | {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} |
    | {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} |
    +-----------+
    """
        else:
            print(tabuleiroD)
            tabuleiro = O(tabuleiro)
            tabuleiroD = f"""
    +-----------+
    | {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} |
    | {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} |
    | {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} |
    +-----------+
    """
        jogadas += 1  # Passa a jogada atual

        # Termina o jogo caso a condição de vitória seja atinjida
        if condVitoria(tabuleiro, tabuleiroD):
            jogadas = 10
#-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-

# Chama a função jogo para começar a aplicação
jogo(jogarX, jogarO)
#-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-