total_prices = []

while True:
    product_name = input("Enter product name: ")

    if product_name == "stop" or len(product_name) == 0:
        break

    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total_product_cost = quantity * price
    total_prices.append(total_product_cost)

    print("-" * 15)
    print(f"Product: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    print("-" * 15)
    print(f"Total cost: {total_product_cost}")
    print("-" * 15)



if len(total_prices) == 0:
    print("No products entered")
    exit()


receipt_cost = sum(total_prices)

print("-" * 15)
print(f"Total Receipt Cost: {receipt_cost}")