def Main():
    print("--- Welcome to the Billing System ---")
    customer_name = input("Enter customer name: ")

    items = []  # List to store item details

    while True:
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: Rs. "))
        item_quantity = int(input("Enter item quantity: "))

        # Add item details to the list
        items.append({
            'name': item_name,
            'price': item_price,
            'quantity': item_quantity
        })

        # Ask if the customer wants to add another item
        another_item = input("Do you want to add another item? (y/n): ").lower()
        if another_item != 'y':
            break

    # Calculate total bill
    total_bill = sum(item['price'] * item['quantity'] for item in items)

    # Display bill details
    print("\n--- Bill Summary ---")
    print(f"Customer Name: {customer_name}")
    print("Items Purchased:")
    for item in items:
        print(f"  {item['name']} - Rs. {item['price']} x {item['quantity']} = Rs. {item['price'] * item['quantity']}")
    print(f"Total Bill: Rs. {total_bill}")

# Run the function
if __name__ == "__main__":
    Main()