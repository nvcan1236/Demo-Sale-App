function addToCart(id, name, price) {
    fetch('/api/cart', {
        method: 'post',
        body: JSON.stringify({
            id,
            name,
            price
        }),
        headers: {
            'Content-Type': 'application/json'
        }

    }).then(function (res) {
        return res.json()
    }).then(function (data) {
        amount = document.querySelector('.cart-amount')
        amount.innerText = data['total_quantity']
    })


}
