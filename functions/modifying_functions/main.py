def apply_discount(price, discount=0.05):
    return price * (1 - discount)

def apply_tax(price, tax=0.07):
    return price * (1 + tax)

def calculate_total(price, discount=0.05, tax=0.07):
    total = apply_tax(price, tax) + (apply_discount(price, discount))
    return total

print(f"Total cost with the default discount and tax: ${calculate_total(120)}")