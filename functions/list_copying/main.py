def apply_discount(prices):
    prices_copy = prices.copy()
    for i in range(len(prices_copy)):
        price = prices_copy[i]
        if price > 2:
            price *= 0.9
return 


# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)