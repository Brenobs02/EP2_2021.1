def lista_movimentos_possiveis(baralho, i):
    movimentos = []
    if extrai_valor(baralho[i]) == extrai_valor(baralho[i - 1]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i - 1]):
        movimentos.append(1)
    if extrai_valor(baralho[i]) == extrai_valor(baralho[i - 3]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i - 3]):
        movimentos.append(3)
    return movimentos