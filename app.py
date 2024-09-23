from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    product_name = request.args.get('product_name')
    url = f'https://shopee.com.br/search?keyword={product_name}'
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.shopee-search-item-result__item'):
        title = item.select_one('.yQmmFK._1POlWt').text
        price = item.select_one('._1w9jLI.QbH7Ig').text.replace('R$', '').replace('.', '').replace(',', '.')
        products.append({'name': title, 'price': float(price)})

    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
