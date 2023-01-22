
def priceCheck(products, productPrices, productSold, soldPrice):
    product_price_dict = dict(zip(products, productPrices))
    errors = 0
    for i in range(len(productSold)):
        expected_price = product_price_dict[productSold[i]]
        if expected_price != soldPrice[i]:
            errors += 1
    return errors


if __name__ == '__main__':
    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]
    print(priceCheck(products, productPrices, productSold, soldPrice))

    print(priceCheck(
        products=['rice', 'sugar', 'wheat', 'cheese'],
        productPrices=[16.89, 56.92, 20.89, 345.99],
        productSold=['rice', 'cheese'],
        soldPrice=[18.99, 400.89]
    ))
