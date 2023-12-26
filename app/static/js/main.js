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
        location.reload()
    })
}

function pay() {
    if(confirm('Bạn có chắc muốn thanh toán?') === true) {
        fetch('/api/pay', {
            method: 'post'
        })
        .then(res => res.json())
        .then(data => {
            if(data.statusCode == 200) {
                location.reload()
            }
            else if (data.statusCode == 400) {
                alert(data.message)
            }
        })
    }
}

const login = document.querySelector('.login-form')
const register= document.querySelector('.register-form')
  function switchForm() {
    login.classList.toggle('hide')
    register.classList.toggle('hide')
  }