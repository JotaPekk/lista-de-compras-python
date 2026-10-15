from item import Item
import json
import os


def carregar_itens():
    if not os.path.exists('itens.json'):
        with open('itens.json', 'w') as f:
            json.dump([], f)
    with open('itens.json', 'r') as f:
        dados = json.load(f)
        return [Item(i['nome'], i['quantidade']) for i in dados]

def salvar_itens(itens):
    dados = [{'nome': i.nome, 'quantidade': i.quantidade} for i in itens]
    with open('itens.json', 'w') as f:
        json.dump(dados, f)