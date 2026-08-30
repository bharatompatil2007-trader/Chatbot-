# Simple Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:")
print(", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Price per share:", stock_prices[stock])
        print("Investment:", investment)

    except ValueError:
        print("Please enter a valid quantity.")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment: $", total_investment)
print("Thank you!")