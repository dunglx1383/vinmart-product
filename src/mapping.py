from vinmart_parser import Product

csv_columns = ['Name',  # product name itself
               'Active',  # set 1 for products if they should be active, contrariwise provide 0 in this field
               'Categories',  # category, product should be added to
               'Price',  # indicate tax included or tax excluded product price
               'Tax ID'  # provide ID of tax rule if you need to associate some with product
               'Reference #',  # add product reference (code used for inventory tracking).
                               # This internal number is usually called stock keeping unit,
                               # but PrestaShop calls it Reference
               'Supplier reference #',  # associate supplier reference with merchandise providing it
                                        # in corresponding column of your .csv
               'Supplier',  # assign supplier to products, indicating it in this column
               'Manufacturer',  # add product manufacturer
               'Weight',  # product weight
               'Quantity',  # number of products you have in stock
               'Minimal quantity',  # configure how many items of this
                                    # or that product should customer add to cart for order to be accepted
               'Visibility',  # define whether products should be shown in catalog, search,
                              # both or none of these options
               'Short description',  # provide some details about the products you are going to upload
               'Description',  # specify complete product description so your customers will get maximum details
               'Meta Information (Meta Title, Meta Description)',  # add these details since they are important for SEO
               'Available for order',  # to enable product sale add 1 in this field, contrariwise – 0 value
               'Image URL',  # to create representative product page, you have to upload its image.
                             # Input image URL for each record
               'Condition ',  # configure product condition – new, used, refurbished
               'Out of Stock',  # enable or disable products you import, adding 0 and 1 in this field correspondingly
               ]


def prepare_csv_row(category: str, product: Product):
    row = [product.name,  # Name
           "1",  # Active
           category,  # Categories
           str(product.price.sell_price),  # Price
           '',  # Tax ID
           '',  # Reference #
           '',  # Supplier reference #
           str(product.brand.code),  # Supplier
           product.brand.name,  # Manufacturer
           1,  # Weight
           1,  # Quantity
           0,  # Minimal quantity
           1,  # Visibility
           product.display_name,  # Short description (need re-check)
           '',  # Description (need re-check)
           '',  # Meta Information (Meta Title, Meta Description) (need re-check)
           '',  # Available for order
           '',  # Image URL
           '',  # Condition
           ''  # Out of Stock
           ]
    return row
