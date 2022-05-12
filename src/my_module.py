"""
Desafio Syngenta Digital
Lakewood
 Classificação: 3
 Valores: Dias de semana - 110 clientes normais e 80 fidelidade
          Final de semana - 90 clientes normais e 80 fidelidade
Bridgewood
 Classificação: 4
 Valores: Dias de semana - 160 clientes normais e 110 fidelidade
          Final de semana - 60 clientes normais e 50 fidelidade
 Ridgewood
 Classificação: 5
 Valores: Dias de semana - 220 clientes normais e 100 fidelidade
          Final de semana - 150 clientes normais e 40 fidelidade

Entrada - Regular ou Reward (Ex: Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed))
Saída - Hotel mais barato (Ex: Lakewood)

"""


def get_cheapest_hotel(number):
    valores1 = [110, 90, 80, 80]
    valores2 = [160, 60, 110, 50]
    valores3 = [220, 150, 100, 40]
    total_dsemana = 0
    total_fsemana = 0

    fidelidade, dias = number.split(":")
    if fidelidade == 'Regular':
        posicao = 0
    if fidelidade == 'Rewards':
        posicao = 2

    if 'mon' in dias:
        total_dsemana += 1
    if 'tues' in dias:
        total_dsemana += 1
    if 'wed' in dias:
        total_dsemana += 1
    if 'thu' in dias:
        total_dsemana += 1
    if 'fri' in dias:
        total_dsemana += 1
    if 'sat' in dias:
        total_fsemana += 1
    if 'sun' in dias:
        total_fsemana += 1

    lakewood = valores1[posicao] * total_dsemana + valores1[posicao + 1] * total_fsemana
    bridgewood = valores2[posicao] * total_dsemana + valores2[posicao + 1] * total_fsemana
    ridgewood = valores3[posicao] * total_dsemana + valores3[posicao + 1] * total_fsemana

    if lakewood < bridgewood and lakewood < ridgewood:
        cheapest_hotel = "Lakewood"
    if bridgewood < lakewood and bridgewood < ridgewood or lakewood == bridgewood:
        cheapest_hotel = "Bridgewood"
    if (ridgewood < lakewood and ridgewood < bridgewood) or lakewood == ridgewood or bridgewood == ridgewood:
        cheapest_hotel = "Ridgewood"

    return cheapest_hotel

