

comb = {"123": [1,2,3], "456": [4,5,6], "789": [7,8,9], 
        "159": [1,5,9], "357": [3,5,7], "147": [1,4,7], 
        "258": [2,5,8], "369": [3,6,9]}
numeros = {1,2,3,4,5,6,7,8,9}

def logico(player, compd):
    escolha = list()
    for x in comb.values():
        setter = {num for num in x}
        numeric = setter - player
        print(f"NERIC:{numeric}")
        if len(numeric) == 1:
            escolha.extend(numeric)
            for x in compd:
                try:
                    escolha.remove(x)
                except ValueError:
                    continue

    return escolha[0]

print(logico({1,3,5,9}, {2,4,6}))