def computer():
    print("1. check email")
    print("2. check calendar")
    print("3. check bank account")
    print("4. open myMarket")
    print("5. leave computer")

    choice = input("> ")
    if choice == "1":
        email()
    elif choice == "2":
        calendar()
    elif choice == "3":
        bank()
    elif choice == "4":
        myMarket()
    elif choice == "5":
        return
    else:
        print("invalid selection")
        computer()

def email():
    print("1. check new emails")
    print("2. see all emails")
    print("3. send email")
    print("3. return to computer")

    choice = input("> ")
    if choice == "1":
        print("you read your email")
        email()
    elif choice == "2":
        print("you send an email")
        email()
    elif choice == "3":
        computer()
    else:
        print("invalid selection")
        email()

def calendar():
    # Flesh this out to include events
    # Add a way to add events
    # Configure
    print("1. view calendar")
    print("2. return to computer")

    choice = input("> ")
    if choice == "1":
        print("you view your calendar")
        calendar()
    elif choice == "2":
        computer()
    else:
        print("invalid selection")
        calendar()


def bank():
    print("1. view bank account")
    print("2. return to computer")

    choice = input("> ")
    if choice == "1":
        print("you view your bank account")
        bank()
    elif choice == "2":
        computer()
    else:
        print("invalid selection")
        bank()

def myMarket():
    print("1. view vendors")
    print("2. view bookings")
    print("3. book vendor")
    print("4. return to computer")

    choice = input("> ")
    if choice == "1":
        print("you view your vendors")
        myMarket()
    elif choice == "2":
        print("you view your bookings")
        myMarket()
    elif choice == "3":
        print("you book a vendor")
        myMarket()
    elif choice == "4":
        computer()
    else:
        print("invalid selection")
        myMarket()

computer()
