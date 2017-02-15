# -*- coding: utf-8 -*-
import json
import urllib
from datetime import datetime, timedelta


def get_cotacoes(inicio, fim):
    step = timedelta(days=1)
    valores = []

    while inicio <= fim:
        url = 'http://api.fixer.io/'
        url += str(inicio.date())
        url += '?base=USD&symbols=BRL'
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        valores.append([data['date'], data['rates']['BRL']])
        inicio += step

    return valores

if __name__ == "__main__":
    data_inicio, data_fim = '2009-08-07', '2011-11-17'

    inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
    fim = datetime.strptime(data_fim, '%Y-%m-%d')
    valores = get_cotacoes(inicio, fim)

    maior, menor, total = valores[0], valores[0], 0

    for dia, valor in valores:
        if dia != '2009-08-07' and dia != '2011-11-17':
            total += valor
        if valor > maior[1]:
            maior = [dia, valor]
        if valor < menor[1]:
            menor = [dia, valor]

    print 'Maior valor foi: R$' + str(maior[1]) + ' no dia: ' + datetime.strptime(maior[0], '%Y-%m-%d').strftime('%d/%m/%y')
    print 'Menor valor foi: R$' + str(menor[1]) + ' no dia: ' + datetime.strptime(menor[0], '%Y-%m-%d').strftime('%d/%m/%y')
    print 'A Média é: R$' + str(total/(len(valores) - 2))
