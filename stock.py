import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 320,
    "AMZN": 3300
}

total_investment = 0
portfolio_data = []

print("📈 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name in stock_prices:
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment
        
        portfolio_data.append([stock_name, price, quantity, investment])
        
        print(f"Added {stock_name} - Investment: Rs.{investment}")
    else:
        print("❌ Stock not available.")

print("\n💰 Total Investment Value: ", total_investment)

save = input("Do you want to save result to file? (yes/no): ").lower()

if save == "yes":
    
    # 🔹 Save CSV file
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Name", "Price", "Quantity", "Investment"])
        writer.writerows(portfolio_data)
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_investment])

    # 🔹 Save TXT file
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for data in portfolio_data:
            file.write(f"Stock: {data[0]}, Price: {data[1]}, Quantity: {data[2]}, Investment: {data[3]}\n")
        file.write("\n")
        file.write(f"Total Investment: Rs.{total_investment}")

    print("✅ Data saved to portfolio.csv and portfolio.txt")

print("📊 Program Finished!")
