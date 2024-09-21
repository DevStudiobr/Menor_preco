import requests
from bs4 import BeautifulSoup

def buscar_preco(id_produto):
    url = f"https://shopee.com.br/product/{id_produto}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Erro ao acessar a página do produto.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    preco = soup.select_one('.shopee-price__current-price')
    if preco:
        preco_valor = float(preco.text.replace('R$', '').replace('.', '').replace(',', '.'))
        print(f"O preço do produto com ID {id_produto} é R$ {preco_valor:.2f}")
    else:
        print("Preço não encontrado.")

def main():
    id_produto = input("Digite o ID do produto que você deseja buscar: ")
    buscar_preco(id_produto)

if __name__ == "__main__":
    main()
