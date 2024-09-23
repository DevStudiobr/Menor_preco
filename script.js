document.getElementById('priceForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const productName = document.getElementById('productName').value;
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = 'Buscando...';

    try {
        const response = await fetch(`/search?product_name=${encodeURIComponent(productName)}`);
        const products = await response.json();

        resultsDiv.innerHTML = '';
        if (products.length > 0) {
            products.forEach(product => {
                resultsDiv.innerHTML += `<p>${product.name}: R$${product.price.toFixed(2)}</p>`;
            });
        } else {
            resultsDiv.innerHTML = 'Nenhum produto encontrado.';
        }
    } catch (error) {
        resultsDiv.innerHTML = 'Erro ao buscar produtos.';
    }
});
