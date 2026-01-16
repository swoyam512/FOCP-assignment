# Beckett Pizza Plaza 4-for-3 Offer Program
# Author: Your Name
# Date: 2026-01-16

import sys
import os

def get_valid_price(prompt):
    """
    Function to get a valid price.
    Ensures price is numeric, positive, and realistic (<£5000).
    """
    while True:
        price_input = input(prompt)
        try:
            price = float(price_input)
            if price <= 0:
                print("Please enter a valid price greater than 0!")
            elif price > 5000:
                print("Please enter a realistic price (less than £5000)!")
            else:
                return round(price, 2)
        except ValueError:
            print("Please enter a valid numeric price!")

def read_order_from_user():
    """
    Prompts the user to enter prices for 4 pizzas.
    Returns a list of four prices.
    """
    pizza_prices = []
    for i in range(1, 5):
        price = get_valid_price(f"Enter Price of Pizza #{i}: ")
        pizza_prices.append(price)
    return pizza_prices

def read_orders_from_file(filename):
    """
    Reads pizza orders from a file.
    Each line should contain four comma-separated prices.
    Returns a list of orders (list of lists).
    """
    orders = []
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found!")
        return orders

    with open(filename, "r") as file:
        line_number = 0
        for line in file:
            line_number += 1
            parts = line.strip().split(",")
            if len(parts) != 4:
                print(f"Skipping line {line_number}: Must contain 4 prices.")
                continue
            try:
                prices = [round(float(p), 2) for p in parts]
                if any(p <= 0 or p > 5000 for p in prices):
                    print(f"Skipping line {line_number}: Prices must be >0 and <5000.")
                    continue
                orders.append(prices)
            except ValueError:
                print(f"Skipping line {line_number}: Non-numeric values found.")
    return orders

def calculate_total(prices):
    """
    Calculates total cost applying the 4-for-3 offer.
    Returns total price and discount percentage.
    """
    cheapest = min(prices)
    total_without_discount = sum(prices)
    total_price = total_without_discount - cheapest
    discount_percentage = (cheapest / total_without_discount) * 100
    return total_price, discount_percentage

def print_receipt(prices):
    """
    Prints a formatted receipt for a single order.
    """
    total_price, discount_percentage = calculate_total(prices)
    cheapest = min(prices)

    print("\n--- Order Summary ---")
    free_marked = False  # Mark only one pizza as free
    for idx, price in enumerate(prices, 1):
        free_marker = ""
        if price == cheapest and not free_marked:
            free_marker = " (free!)"
            free_marked = True
        print(f"Pizza #{idx}: £{price:.2f}{free_marker}")
    print(f"Subtotal: £{sum(prices):.2f}")
    print(f"Discount: {discount_percentage:.0f}%")
    print(f"Total: £{total_price:.2f}")
    print("---------------------\n")

def process_interactive_mode():
    """
    Runs the program in interactive mode (user input).
    """
    while True:
        prices = read_order_from_user()
        print_receipt(prices)

        repeat = input("Do you want to enter another order? (yes/no): ").strip().lower()
        while repeat not in ["yes", "no"]:
            repeat = input("Please type 'yes' or 'no': ").strip().lower()

        if repeat == "no":
            print("\nThank you for using Beckett Pizza Plaza 4-for-3 Offer Program!")
            break

def process_file_mode(filename):
    """
    Processes orders from a file.
    """
    orders = read_orders_from_file(filename)
    if not orders:
        print("No valid orders found in the file.")
        return

    for order_number, prices in enumerate(orders, 1):
        print(f"\nOrder #{order_number}:")
        print_receipt(prices)

def main():
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================")

    if len(sys.argv) > 1:
        # File input mode
        filename = sys.argv[1]
        process_file_mode(filename)
    else:
        # Interactive mode
        process_interactive_mode()

if __name__ == "__main__":
    main()