from app.retail_customer import RetailCustomer

def main():

    # Get user input
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    # Object Init
    product = RetailCustomer(product_id, name, price, quantity)
    product.display_info();

    # Save
    with open("product_info.txt", "w") as file:
        file.write(f"Product ID: {product.product_id}\n")
        file.write(f"Name: {product.name}\n")
        file.write(f"Price: {product.price}\n")
        file.write(f"Quantity: {product.quantity}\n")

if __name__ == "__main__":
    main()