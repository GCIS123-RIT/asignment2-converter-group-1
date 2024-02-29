def aed_to_euro(amount):
    """
    Convert AED to Euro.
    """
    return amount / 4.12 

def aed_to_british_pound(amount):
    """
    Convert AED to British Pound.
    """
    return amount / 4.79

def aed_to_dollar(amount):
    """
    Convert AED to US Dollar.
    """
    return amount / 3.67

def euro_to_aed(amount):
    """
    Convert Euro to AED.
    """
    return amount * 4.12

def british_pound_to_aed(amount):
    """
    Convert British Pound to AED.
    """
    return amount * 4.79

def dollar_to_aed(amount):
    """
    Convert US Dollar to AED.
    """
    return amount * 3.67

def display_conversion_options():
    """
    Display conversion options to the user.
    """
    print("Select conversion direction:")
    print("1. AED to other currencies")
    print("2. Other currencies to AED")

def aed_to_other_currencies():
    """
    Convert AED to other currencies.
    """
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

def other_currencies_to_aed():
    """
    Convert other currencies to AED.
    """
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

def main():
    """
    Main function of the currency converter.
    """
    print("-"*30)
    print("\"\tMain Menu\"")
    print("Welcome to Currency Converter")
    print("-"*30)
    print("\n")
    while True:
        display_conversion_options()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            aed_to_other_currencies()
        elif choice == 2:
            other_currencies_to_aed()
        else:
            print("Invalid choice")

        another_conversion = input("Do you want to make another conversion? (yes/no): ")
        if another_conversion.lower() != 'yes': 
            break

if __name__ == "__main__":
    main()
