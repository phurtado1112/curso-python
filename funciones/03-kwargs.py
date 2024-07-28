''' Keyword arguments '''


def get_product_price(product, price, **kwargs):
    print(f'Product: {product}')
    print(f'Price: {price}')
    print(f'Other: {kwargs}')


def get_product(**datos):
    print(datos)


get_product(id='id')

get_product(id='1', name='S24', price=1000)


def get_producto(**datos):
    print(datos["id"], datos["name"], datos["price"])


get_producto(id='2', name='S20', price=600)
