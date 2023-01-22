# 1. Price Check
def priceCheck(products, productPrices, productSold, soldPrice):
    product_price_dict = dict(zip(products, productPrices))
    errors = 0
    for i in range(len(productSold)):
        expected_price = product_price_dict[productSold[i]]
        if expected_price != soldPrice[i]:
            errors += 1
    return errors


# 3.Recursive Digit “Summer”
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)




# 4. Recursive Numeric “Sequencer”
def count_max_element(n, max_element=None, count=0):
    if n == 0:
        return "(" + max_element + " ; " + count + ")"
    else:
        if max_element is None:
            max_element = n
        if n == max_element:
            count += 1
        return count_max_element(int(input()), max(max_element, n), count)




# Tests of all tasks
if __name__ == '__main__':
    #--------------------------------------------
    # 1. Price Check
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

    #--------------------------------------------
    # 3.Recursive Digit “Summer”
    print(sum_of_digits(2347623))

    # 2. SQL - Department Summary
    # SELECT d.NAME AS DEPARTMENT, COUNT(e.ID) AS COUNT
    # FROM DEPARTMENT d
    # LEFT JOIN EMPLOYEE e
    # ON d.ID = e.DEPT_ID
    # GROUP BY d.NAME
    # ORDER BY COUNT DESC, d.NAME;

    #--------------------------------------------
    # 4. Recursive Numeric “Sequencer”
    print(count_max_element(int(input())))
