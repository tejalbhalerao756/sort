import csv
import os

csv_file = "stocks.csv"
txt_file = "stocks.txt"

# ----------- CSV FILE CREATE -----------
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price"])
        writer.writerow(["RELIANCE", 10, 2500])
        writer.writerow(["TCS", 5, 3800])
        writer.writerow(["INFY", 8, 1500])
        writer.writerow(["HDFCBANK", 6, 1600])
        writer.writerow(["ICICIBANK", 7, 1000])
        writer.writerow(["SBIN", 12, 600])
        writer.writerow(["ITC", 15, 450])

# ----------- TXT FILE CREATE -----------
if not os.path.exists(txt_file):
    with open(txt_file, "w") as file:
        file.write("RELIANCE,10,2500\n")
        file.write("TCS,5,3800\n")
        file.write("INFY,8,1500\n")
        file.write("HDFCBANK,6,1600\n")
        file.write("ICICIBANK,7,1000\n")
        file.write("SBIN,12,600\n")
        file.write("ITC,15,450\n")

# ----------- READ CSV FILE -----------
print("------ Data From CSV File ------")
total_investment_csv = 0

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        stock = row[0]
        quantity = int(row[1])
        price = int(row[2])

        investment = quantity * price
        total_investment_csv += investment

        print(stock, ":", quantity, "shares ×", price, "=", investment)

print("Total Investment (CSV) =", total_investment_csv)

print("\n------ Data From TXT File ------")

# ----------- READ TXT FILE -----------
total_investment_txt = 0

with open(txt_file, "r") as file:
    for line in file:
        stock, quantity, price = line.strip().split(",")

        quantity = int(quantity)
        price = int(price)

        investment = quantity * price
        total_investment_txt += investment

        print(stock, ":", quantity, "shares ×", price, "=", investment)

print("Total Investment (TXT) =", total_investment_txt)