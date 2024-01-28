def get_order_details():
    while True:
        try:
            num_pizza = int(input("How many pizzas ordered? "))
            if num_pizza < 0:
                raise ValueError("Please enter a positive integer!")
            break
        except ValueError:
            print("Please enter a number!")

    while True:
        delivery_reqd = input("Is delivery required? (Y/N) ").upper()
        if delivery_reqd in ['Y', 'N']:
            break
        else:
            print("Please answer 'Y' or 'N'.")

    while True:
        is_tuesday = input("Is it Tuesday? (Y/N) ").upper()
        if is_tuesday in ['Y', 'N']:
            break
        else:
            print("Please answer 'Y' or 'N'.")

    while True:
        used_app = input("Did the customer use the app? (Y/N) ").upper()
        if used_app in ['Y', 'N']:
            break
        else:
            print("Please answer 'Y' or 'N'.")

    return num_pizza, delivery_reqd, is_tuesday, used_app


def calc_total(num_pizza, delivery_reqd, is_tuesday, used_app):
    pizza_price = 12.0
    delivery_cost = 2.5
    app_discount = 0.25
    tuesday_discount = 0.5

    total_price = num_pizza * pizza_price

    if delivery_reqd == 'Y':
        if num_pizza >= 5:
            total_price += 0  # Free delivery for 5 or more pizzas
        else:
            total_price += delivery_cost

    if is_tuesday == 'Y':
        total_price *= (1 - tuesday_discount)

    if used_app == 'Y':
        total_price *= (1 - app_discount)

    return round(total_price, 2)


def main():
    print("\n/*----------*\BPP Pizza Price Calculator/*----------*\ ")

    num_pizza, delivery_reqd, is_tuesday, used_app = get_order_details()

    total_price = calc_total(num_pizza, delivery_reqd, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")


if __name__ == "__main__":
    main()
