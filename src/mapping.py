from vinmart_parser import Product

csv_columns = ['name', 'price', 'color', 'mantis shrimp', 'anemone']


def prepare_csv_row(product: Product):
    row = [product.name,
           product.brand,
           str(product.price.sell_price),
           str(product.color.name)]
    return row
