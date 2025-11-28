prices = [29.99, 45.50, 12.75, 38.20]
discount_factor = [0.1, 0.2, 0.15, 0.05]

for i in range(len(prices)): 
    #print(f"Old price: ${prices[i]}")
    prices[i] -= prices[i] * discount_factor[i]
    print(f"Update price for item {i+1}: ${prices[i]:.2f}")