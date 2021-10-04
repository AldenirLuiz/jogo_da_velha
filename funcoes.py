from random import choice
import numerador

comb = {"123": [1,2,3], "456": [4,5,6], "789": [7,8,9], 
        "159": [1,5,9], "357": [3,5,7], "147": [1,4,7], 
        "258": [2,5,8], "369": [3,6,9]}
numeros = {1,2,3,4,5,6,7,8,9}

set_player = set()
set_comptd = set()
escolha = []
player = list()
computador = list()
comb_News = list()



def clear() -> None: # Limpa as variaveis para um novo jogo.
    global lista00, lista01, player, computador, set_player, set_comptd, opcao
    lista00 = []
    lista01 = []
    player = []
    computador = []
    set_player = set()
    set_comptd = set()
    opcao = set()

    print("limpo")


def verify(num, play=None): # Verifica a origem da jogada, nome do jogador.
    global jogador, player
    if play == 'pl':
        jogador = player
        set_player.add(num)
    else:
        jogador = computador
        set_comptd.add(num)
    return hasher(play, num)
    

def hasher(nome, val) -> str: # Busca nas combinacoes se ha correspondencia com as escolhas do jogador.
    jogador.append(val)
    lista00 = []
    lista01 = []
    while len(jogador) ** 3 != len(lista01):
        lista00.append(choice(jogador))
        if len(lista00) == 3:
            if lista00 in comb.values():
                print("!!!MATCH!!!", lista00)
                return nome
            if lista00 in lista01:
                lista00 = []
                continue
            elif lista00 not in lista01:
                lista01.append(lista00)
                lista00 = []
                continue
            else:
                return False

def intelit() -> int:

    opc = list(numeros - set_player - set_comptd)
    if len(opc) == 0:
        return 0
    if len(set_comptd) == 0:
        return choice(opc)
    escolha = list()
    try:
        for x in comb.values():
            setter = {num for num in x}
            print(f"SETTER:{setter}")
            numeric = setter - set_comptd
            print(f"NERIC:{numeric}")
            if len(numeric) == 1:
                print(f"NUMERIC")
                if numerador.discovery(numeric, set_comptd):
                    print(f"Encontrado!:{numeric}")
                    return numeric[0]
                elif numerador.discovery(numeric, set_player):
                    print(f"Encontrado!:{numeric}")
                    return numeric[0]
                escolha.extend(numeric)
                print(f"ESCOLHA:{escolha}")
                for x in set_player:
                    try:
                        print(f"VALOR DE X:{x}")
                        escolha.remove(x)
                    except ValueError:
                        if numerador.discovery(numeric, set_comptd):
                            print(f"Encontrado!:{numeric}")
                            return numeric[0]
                        else:
                            continue
        for x in comb.values():
            setter = {num for num in x}
            print(f"SETTER:{setter}")
            numeric = setter - set_player
            print(f"NERIC:{numeric}")
            if len(numeric) == 1:
                print(f"NUMERIC")
                if numerador.discovery(numeric, set_player):
                    print(f"Encontrado!:{numeric}")
                    return numeric[0]
                elif numerador.discovery(numeric, set_comptd):
                    print(f"Encontrado!:{numeric}")
                    return numeric[0]
                escolha.extend(numeric)
                print(f"ESCOLHA:{escolha}")
                for x in set_comptd:
                    try:
                        print(f"VALOR DE X:{x} valor de escolha:{escolha}")
                        escolha.remove(x)
                    except ValueError:
                        if numerador.discovery(numeric, set_player):
                            print(f"Encontrado!:{numeric}")
                            return numeric[0]
                        else:
                            continue
        return escolha[0]
    except IndexError:
        try:
            tentativa = choice(opc)
            return tentativa
        except IndexError:
            return 0
