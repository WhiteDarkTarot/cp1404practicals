def main():
    number_items = int(input("Number of items: "))

    if number_items >= 0:
        total_price = 0
        for i in range(number_items):
            price = float(input("Price of item: "))
            total_price += price

        if total_price > 100:
            total_price *= 0.9

        print(f"Total price for {number_items} items is ${total_price:.2f}")
    else:
        print("Invalid number of items!")


if __name__ == "__main__":
    main()

