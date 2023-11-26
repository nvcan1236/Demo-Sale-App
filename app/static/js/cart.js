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


function updateCart(e, id) {
    quantity = e.target.value
    console.log('sedsdfsv')
    fetch('/api/cart', {
        method: 'patch',
        body: JSON.stringify({
            id,
            quantity
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

function deleteFromCart(id) {
    fetch('/api/cart', {
        method: 'delete',
        body: JSON.stringify({
            id
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
