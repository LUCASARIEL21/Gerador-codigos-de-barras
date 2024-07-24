import barcode
from barcode import EAN13
from barcode.writer import ImageWriter
import os
import PySimpleGUI as sg

# Função para criar os códigos de barras
def criar_codigos_de_barras(num_codigos):
    # Pasta de destino para salvar os códigos de barras
    pasta_destino = 'C:/'

    # Verifique se a pasta de destino existe; se não existir, crie-a
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Gere os códigos de barras sequencialmente
    for i in range(1, num_codigos + 1):
        # Crie um código de barras EAN-13 com base no número sequencial
        dado = str(i).zfill(12)  # Transforma o número em uma string de 12 dígitos com preenchimento de zeros à esquerda
        codigo_de_barras = EAN13(dado, writer=ImageWriter())

        # Gere o código de barras com o dado
        codigo = codigo_de_barras.save(os.path.join(pasta_destino, f'codigo_de_barras_{i}'))
        print(f'Código de barras {i} gerado e salvo com sucesso na pasta {pasta_destino}!')

# Layout da interface gráfica
layout = [
    [sg.Text('Quantos códigos de barras você deseja criar?')],
    [sg.InputText(key='num_codigos')],
    [sg.Button('Criar'), sg.Button('Sair')],
]

# Crie a janela
janela = sg.Window('Gerador de Códigos de Barras').Layout(layout)

# Loop de evento
while True:
    evento, valores = janela.Read()

    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Criar':
        num_codigos = int(valores['num_codigos'])
        criar_codigos_de_barras(num_codigos)
        sg.Popup(f'{num_codigos} códigos de barras criados com sucesso!')

# Feche a janela
janela.close()
