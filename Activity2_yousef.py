def aed_to_euro(amount):
    return amount / 4.12

def aed_to_british_pound(amount):
    return amount / 4.79

def aed_to_dollar(amount):
    return amount / 3.67

def aed_to_other_currencies():
    amount = float(input("Enter amount in AED: "))
    print("Select currency to convert to:")
    print("1. Euro")
    print("2. British Pound")
    print("3. US Dollar")
    currency_choice = int(input("Enter your choice: "))
    if currency_choice == 1:
        print("Result:", aed_to_euro(amount), "EUR")
    elif currency_choice == 2:
        print("Result:", aed_to_british_pound(amount), "GBP")
    elif currency_choice == 3:
        print("Result:", aed_to_dollar(amount), "USD")
    else:
        print("Invalid currency choice")