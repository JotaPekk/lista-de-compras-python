from item import Item
import armazenamento
import json

def main():
    itens = armazenamento.carregar_itens()

    while True:
        nome = input("Digite o nome do item: ")
        quantidade = input("Digite a quantidade do item ou 'sair' para encerrar: ")

        if nome == "sair" or quantidade == "sair":
            break
        itens.append(Item(nome, int(quantidade)))
        armazenamento.salvar_itens(itens)

    print("Itens cadastrados:")

    with open('itens.json', 'r') as f:
        dados = json.load(f)
        for i in dados:
            print(f"{i['nome']} - Quantidade: {i['quantidade']}")
if __name__ == "__main__":
    main()