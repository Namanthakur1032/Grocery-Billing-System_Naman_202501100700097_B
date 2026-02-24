# Naman Kumar_202501100700097_ECE-B

def calculate_bill():
    items = int(input("Enter the number of items: "))
    print()

    if items == 0:
        print("No items purchased.")
        return

    total_amount = 0

    for i in range(1, items + 1):
        price = float(input(f"Enter the price of item {i}: "))
        quantity = int(input(f"Enter the quantity of item {i}: "))
        print()
        total_amount += price * quantity

    discount = 0
    if total_amount > 100:
        discount = total_amount * 0.10

    final_amount = total_amount - discount

    print(f"Amount = {total_amount}")
    print(f"Discount = {discount}")
    print(f"Final Amount = {final_amount}")


calculate_bill()