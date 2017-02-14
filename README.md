# Teste-de-Selecao
**Instrução**

- Para rodar em ambiente linux:
    - Salve o código com nome de sua preferência e a extensão .py (teste.py)
    - Abra o terminal
    - Vá até o diretório do arquivo salvo
   
   - Digite: 
        - python nomedoarquivo.py


**Código**



```
# -*- coding: utf-8 -*-
import urllib, json
import datetime
###############################################################################
def get_cotacoes(inicio, fim):
    step = datetime.timedelta(days = 1)
    valores = []

    while inicio <= fim:
        print '1'
        url = 'http://api.fixer.io/'
        url += str(inicio.date())
        url += '?base=USD&symbols=BRL'
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        valores.append([data['date'], data['rates']['BRL']])
        inicio += step

    return valores
###############################################################################
data_inicio = '2009-08-07'
data_fim = '2011-11-17'

inicio = datetime.datetime.strptime(data_inicio, '%Y-%m-%d')
fim = datetime.datetime.strptime(data_fim, '%Y-%m-%d')
valores = get_cotacoes(inicio, fim)

maior, menor = valores[0], valores[0]
total = 0

for dia, valor in valores:
    print '2'
    if dia != '2009-08-07' and dia != '2011-11-17':
        total += valor
    if valor > maior[1]:
        maior = [dia, valor]
    if valor < menor[1]:
        menor = [dia, valor]

print 'Maior valor foi: R$' + str(maior[1]) + ' no dia: ' + datetime.datetime.strptime(maior[0], '%Y-%m-%d').strftime('%d/%m/%y')
print 'Menor valor foi: R$' + str(menor[1]) + ' no dia: ' + datetime.datetime.strptime(menor[0], '%Y-%m-%d').strftime('%d/%m/%y')
print 'A Média é: R$' + str(total/(len(valores) - 2))

```
