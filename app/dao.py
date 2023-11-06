def get_categories():
    return [
        {id: 1,
         'name': 'Mobile'
         },
        {id: 2,
         'name': 'Tablet'
         },
        {id: 3,
         'name': 'Laptop'
         },
    ]


def get_products(kw):
    products = [{
        'id': 1,
        'price': 32000000,
        'name': 'Z Flip5',
        'image': 'https://images.samsung.com/is/image/samsung/assets/vn/2307/pcd/PCD_B5_Whats-new_684X684_pc_alt.jpg?$684_684_JPG$'
    },
        {
            'id': 2,
            'name': 'Galaxy Z Fold5',
            'price': 32000000,
            'image': 'https://images.samsung.com/is/image/samsung/assets/vn/2307/pcd/PCD_Q5_Whats-new_330x330_pc_alt.png?$330_330_PNG$'
        },
        {
            'id': 3,
            'name': 'Galaxy S23 FE',
            'price': 32000000,
            'image': 'https://images.samsung.com/is/image/samsung/assets/vn/mobile/s23-fe/PCD_R11_Merchandising_376x376_pc.png?$160_160_PNG$'
        },
        {
            'id': 4,
            'name': 'Galaxy S23 Ultra',
            'price': 32000000,
            'image': 'https://images.samsung.com/is/image/samsung/assets/vn/2307/pcd/PCD_DM3_KV_Whats-new_160x160_pc.png?$160_160_PNG$'
        },
        {
            'id': 5,
            'name': 'Galaxy S23/ S23+',
            'price': 32000000,
            'image': 'https://images.samsung.com/is/image/samsung/assets/vn/2307/pcd/PCD_DM1_DM2_KV_Whats-new_160x160_pc.png?$160_160_PNG$'
        },
        {
            'id': 6,
            'name': 'iPhone 15',
            'price': 32000000,
            'image': 'https://mobileleb.com/cdn/shop/files/apple-mobile-phone-apple-iphone-15-pro-max-512gb-33291439046788_1024x1024.jpg?v=1694771068'
        },
    ]

    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]

    return products
