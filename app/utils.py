from flask import request

def count_cart(cart):
    total_price, total_quantity = 0, 0

    if cart:
        for c in cart.values():
            total_price += c['quantity'] * c['price']
            total_quantity += c['quantity']

    return {
        'total_price': total_price,
        'total_quantity': total_quantity,
    }


def get_prev_url():
    referer = request.headers.get('Referer')

    if referer and referer != request.url:
        return referer
    else:
        return '/'



