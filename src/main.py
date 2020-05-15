import json
import unicodecsv as csv
import requests

from mapping import csv_columns, prepare_csv_row
from vinmart_parser import vinmart_product_from_dict


def read_category_list():
    with open('vinmart_category.csv', mode='rb') as product_category_file:
        category_reader = csv.reader(product_category_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in category_reader:
            print(str(row[0]) + '. getting products in ' + row[1])
            page = 1
            while True:
                file_name = str(row[0]) + '_' + clean_name(row[1])
                has_more_product = do_hard_work(page, file_name, row[2])
                page += 1
                if not has_more_product:
                    break


def clean_name(name: str):
    return name.replace('\"', '') \
        .replace('-', '') \
        .replace(',', '_')


def do_hard_work(page: int, name: str, url: str):
    url = url.replace('&_page=1', '&_page=' + str(page))
    print('url: ' + url)
    data = get_json_by_url(url)
    doc = json.loads(data.text)
    if doc['code'] == 'SUCCESS':
        print(doc['extra']['totalItems'])
        json_to_csv(name, data)
        return doc['extra']['page'] * doc['extra']['pageSize'] < doc['extra']['totalItems']
    else:
        return False


def get_json_by_url(url):
    product_category_url = url
    json_data = requests.get(product_category_url)
    return json_data


def json_to_csv(name: str, json_data: requests.Response):
    result = vinmart_product_from_dict(json.loads(json_data.text))
    print(result.code)
    with open('products\\' + name + '.csv', mode='ab') as product_file:
        product_writer = csv.writer(product_file, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_NONNUMERIC, encoding='utf-8')
        product_writer.writerow(csv_columns)
        for product in result.result.products:
            print(product.name)
            row = prepare_csv_row(product)
            product_writer.writerow(row)
    product_file.close()


def main():
    print("Hello, World!")
    read_category_list()


if __name__ == "__main__":
    main()
