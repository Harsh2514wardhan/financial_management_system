class Portfolio:
    def __init__(self, owner):
        self.owner = owner
        self.stocks = {}
        self.fixed_deposits = []
        self.cryptocurrencies = {}
        self.insurance_policies = []

    def add_stock(self, symbol, quantity, price):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
        else:
            self.stocks[symbol] = {'quantity': quantity, 'price': price}
        print(f"✅ Added {quantity} of {symbol} at ₹{price} each.")

    def view_stocks(self):
        print("\n📈 Stocks:")
        if not self.stocks:
            print("No stocks added yet.")
        for symbol, data in self.stocks.items():
            print(f"{symbol}: {data['quantity']} shares @ ₹{data['price']}")

    def add_fd(self, amount, interest_rate, tenure_years):
        self.fixed_deposits.append({'amount': amount, 'rate': interest_rate, 'tenure': tenure_years})
        print(f"✅ FD added: ₹{amount} @ {interest_rate}% for {tenure_years} years.")

    def view_fds(self):
        print("\n🏦 Fixed Deposits:")
        if not self.fixed_deposits:
            print("No FDs yet.")
        else:
            for i, fd in enumerate(self.fixed_deposits, 1):
                print(f"{i}. ₹{fd['amount']} @ {fd['rate']}% for {fd['tenure']} years")

    def add_crypto(self, name, units, price):
        if name in self.cryptocurrencies:
            self.cryptocurrencies[name]['units'] += units
        else:
            self.cryptocurrencies[name] = {'units': units, 'price': price}
        print(f"✅ Added {units} units of {name} @ ₹{price} each.")

    def view_cryptos(self):
        print("\n💰 Cryptocurrencies:")
        if not self.cryptocurrencies:
            print("No crypto holdings yet.")
        else:
            for name, data in self.cryptocurrencies.items():
                print(f"{name}: {data['units']} units @ ₹{data['price']}")

    def add_insurance(self, name, amount, premium, duration):
        self.insurance_policies.append({'name': name, 'amount': amount, 'premium': premium, 'duration': duration})
        print(f"✅ Insurance added: {name}, ₹{amount}, premium ₹{premium}/yr for {duration} yrs")

    def view_insurance(self):
        print("\n🛡️ Insurance Policies:")
        if not self.insurance_policies:
            print("No insurance policies yet.")
        else:
            for i, policy in enumerate(self.insurance_policies, 1):
                print(f"{i}. {policy['name']} - ₹{policy['amount']} (₹{policy['premium']}/yr for {policy['duration']} yrs)")

    def view_summary(self):
        self.view_stocks()
        self.view_fds()
        self.view_cryptos()
        self.view_insurance()


def main():
    user = input("Enter your name: ")
    portfolio = Portfolio(user)

    while True:
        print("\n=== Financial Management System ===")
        print("1. Add Stock")
        print("2. View Stocks")
        print("3. Add Fixed Deposit")
        print("4. View Fixed Deposits")
        print("5. Add Cryptocurrency")
        print("6. View Cryptocurrencies")
        print("7. Add Insurance")
        print("8. View Insurance Policies")
        print("9. View Portfolio Summary")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Stock symbol: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price per share: "))
            portfolio.add_stock(symbol, quantity, price)

        elif choice == '2':
            portfolio.view_stocks()

        elif choice == '3':
            amount = float(input("FD Amount (₹): "))
            rate = float(input("Interest rate (%): "))
            years = int(input("Tenure (years): "))
            portfolio.add_fd(amount, rate, years)

        elif choice == '4':
            portfolio.view_fds()

        elif choice == '5':
            name = input("Crypto name: ")
            units = float(input("Units: "))
            price = float(input("Price per unit (₹): "))
            portfolio.add_crypto(name, units, price)

        elif choice == '6':
            portfolio.view_cryptos()

        elif choice == '7':
            name = input("Insurance Name: ")
            amount = float(input("Coverage Amount (₹): "))
            premium = float(input("Annual Premium (₹): "))
            years = int(input("Duration (years): "))
            portfolio.add_insurance(name, amount, premium, years)

        elif choice == '8':
            portfolio.view_insurance()

        elif choice == '9':
            portfolio.view_summary()

        elif choice == '0':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()


