# VARIÁVEIS
palavra = ""      # Palavra escolhida para o jogo
dica = ""         # Dica da palavra
lTentativas = []  # Lista das letras que ja foram tentadas
palavraIndex = [] # Lista dos índices das letras que estão certas
fim = False       # Condição para o fim do jogo
i = 0             # Contador do índice da palavra
erro = 0          # A quantidade de erros cometidos
forca = ""        # A forca

# -//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-

# FUNÇÕES

# Entrada das tentativas
def tentativaU():
    errado = True
    while errado:
        # Entrada de tentativa
        letra = input("\ntente uma letra: ").lower()
        # Verifica se a letra é repetida procurando-a na lista de tentativas
        if letra in lTentativas:
            # Continua o ciclo
            print("Essa letra já foi usada")
            errado = True
        else:
            errado = False  # O ciclo é parado
            lTentativas.append(letra)  # A letra é adicionada à lista de tentativas
            return letra  # Retorna a letra tentada


# Imprime uma barra
def barra():
    print("")
    print("-","//- " * 20)


# Retorna uma string contendo todos as posicões das letras acertadas
def localLetra(i):

    # Verifica se a lista está vazia
    if len(i) != 0:
        index = f"A letra {tentativa} está na posição {i[0]}"  # Define o primeiro índice
        i.pop(0)  # exclui o primero índice
        
        # Adiciona os demais índices caso existam
        while len(i) != 0:
            index = index + f", {i[0]}"
            i.pop(0)  # Sempre é excluido o primeiro índice para adicionar o seguinte
            
        return index  # Retorna todos os índices em uma string
        
# -//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-
     
# CÁLCULO
palavra = input("Digite uma palavra: ")  # Entrada da palavra do jogo
dica = input("Digite a dica para essa palavra: ")  #Entrada da dica da palavra
palavraE = list("_" * len(palavra))  # Criando a palavra escondida
forca = f"""
dica: {dica}
número de letras: {len(palavra)}
 +-------+
 |       |
 |
 |
 |
 |
_+_   {"".join(palavraE)}"""  # O desenho da forca, junto com a dica, número de letras e a palavra escondida

print(" \n" * 20) # Pula linhas para a palavra inserida não seja vista


print(forca)  # Imprime a forca

# O jogo começa aqui
while not fim:
    tentativa = tentativaU() # A variável tentiva chama a função tentativa do usuário e recebe o valor retornado por ela
    print(" \n" * 2) # pula linhas

    # Verifica se a letra tentada está na palavra
    if tentativa in palavra:
        print("") # Pula linhas
        
        for l in palavra:
            if tentativa == l:
                palavraIndex.append(i+1) # Adiciona o índice da letra acertada
                palavraE[i] = l # Troca o underline da posição indicada pela letra
            i += 1 # Contador de índice
        certo = True # Define que acertou a letra
   
    else:
        erro += 1 # Adiciona 1 a quantidade de erros
        certo = False # Define que errou a letra

# Caso não tenha errado nenhuma letra define a forca
    if erro == 0: 
        forca = f"""
dica: {dica}
número de letras: {len(palavra)}
 +-------+
 |       |
 |
 |
 |
 |
_+_   {"".join(palavraE)}"""

# Caso tenha errado uma letra adiciona um pedaço do corpo, e assim po diante...
    elif erro == 1:
        forca = f"""
dica: {dica}
número de letras: {len(palavra)}
 +-------+
 |       |
 |       o
 |
 |
 |
_+_   {"".join(palavraE)}"""
    
    elif erro == 2:
        forca = f"""
dica: {dica}
número de letras: {len(palavra)}
 +-------+
 |       |
 |       o
 |       |
 |
 |
_+_   {"".join(palavraE)}"""
   
    elif erro == 3:
        forca = f"""
dica: {dica}
número de letras: {len(palavra)}
 +-------+
 |       |
 |       o
 |      /|
 | 
 |
_+_   {"".join(palavraE)}"""
    
    elif erro == 4:
        forca = f"""
dica: {dica}
número de letras: {len(palavra)}
 +-------+
 |       |
 |       o
 |      /|\ 
 |
 |
_+_   {"".join(palavraE)}"""
    
    elif erro == 5:
        forca = f"""
dica: {dica}
número de letras: {len(palavra)}
 +-------+
 |       |
 |       o
 |      /|\ 
 |      /
 |
_+_   {"".join(palavraE)}"""
    
    elif erro == 6:
        forca = f"""
dica: {dica}
número de letras: {len(palavra)}
 +-------+
 |       |
 |       o
 |      /|\ 
 |      / \ 
 |
_+_   {palavra}"""
        fim = True # No sexto erro é definido fim de jogo

# RESULTADO
    print(forca) # Imprime a forca
    print("") # Pula linha
    if certo:
        print(localLetra(palavraIndex)) # Imprime cada local da letra encontrada
    else:
        print(f"a palavra não possuí a letra {tentativa}") # Imprime que não há essa letra
    print("")
    
    # Imprime as letras já utilizadas
    print("Letras já utilizadas:")
    for l in lTentativas:
        print(l, end = ", ")

    print("")


    # Caso você tenha ganho imprime isso
    if "".join(palavraE) == palavra:
        print (f"\nA palavra é {palavra}, você ganhou!")
        fim = True
    
    # Caso tenha perdido imprime isso
    elif erro == 6:
        print(f"\nVocê foi enforcado! a palavra era {palavra}.")
        fim = True

    i = 0 # Zera o contador do índice

    barra() # Chama a função barra para imprimir uma barra