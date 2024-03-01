def euro_to_aed(amount):
    return amount * 4.12

def british_pound_to_aed(amount):
    return amount * 4.79

def dollar_to_aed(amount):
    return amount * 3.67

def other_currencies_to_aed():
    amount = float(input("Enter amount: "))
    print("Select currency to convert from:")
    print("1. Euro")
    print("2. British Pound")
    print("3. US Dollar")
    currency_choice = int(input("Enter your choice: "))
    if currency_choice == 1:
        print("Result:", euro_to_aed(amount), "AED")
    elif currency_choice == 2:
        print("Result:", british_pound_to_aed(amount), "AED")
    elif currency_choice == 3:
        print("Result:", dollar_to_aed(amount), "AED")
    else:
        print("Invalid currency choice")
