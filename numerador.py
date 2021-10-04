from random import choice

comb = {"123": [1,2,3], "456": [4,5,6], "789": [7,8,9], 
        "159": [1,5,9], "357": [3,5,7], "147": [1,4,7], 
        "258": [2,5,8], "369": [3,6,9]}

def discovery(val, lista) -> bool: # Busca nas combinacoes se ha correspondencia com as escolhas do jogador.
    jogador = list(lista)
    jogador.append(val)
    lista00 = []
    lista01 = []
    while len(jogador) ** 3 != len(lista01):
        lista00.append(choice(jogador))
        if len(lista00) == 3:
            if lista00 in comb.values():
                print("!!!MATCH!!!", lista00)
                return True
            if lista00 in lista01:
                lista00 = []
                continue
            elif lista00 not in lista01:
                lista01.append(lista00)
                lista00 = []
                continue
            else:
                return False