# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):  
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

def formatted_output(product_name, revenue):
    revenue_per_product = sorted(list(zip(product_name, revenue)))
    for product in revenue_per_product:
        print(f"{product[0]} has total revenue of ${product[1]}")
    return revenue_per_product


revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = formatted_output(products, revenues)



