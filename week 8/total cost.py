# Total Cost Calculator Program

def main():
    prices = []

    while True:
        price = input("Enter a product price (or type 'done' to finish): ")
        if price.lower() == 'done':
            break
        try:
            price = float(price)
            if price >= 0:
                prices.append(price)
            else:
                print("Please enter a positive price.")
        except ValueError:
            print("Invalid input. Please enter a numeric price.")

    if prices:
        total_cost = sum(prices)
        print(f"\nThe total cost is: ${total_cost:.2f}")
    else:
        print("No prices entered.")


if __name__ == "__main__":
    main()