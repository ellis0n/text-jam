from Util.input import system as sys
class Computer:
    def __init__(self, state):
        self.state = state
        self.emails = []

    def run(self):
        while True:
            print("\n1. open email client")
            print("2. open calendar")
            print("3. check bank account")
            print("4. open myMarket")
            print("5. leave computer")

            choice = input("\n> ")
            sys(choice)
            if choice == "1":
                self.check_email()
            elif choice == "2":
                self.check_calendar()
            elif choice == "3":
                self.check_bank()
            elif choice == "4":
                self.open_my_market()
            elif choice == "5":
                break
            else:
                print("invalid selection")

    def check_email(self):
        while True:
            print("\n1. check new emails")
            print("2. see all emails")
            print("3. send email")
            print("4. return to computer")

            choice = input("\n> ")
            sys(choice)
            if choice == "1":
                print("\nyou scan for new emails, but find none")
            elif choice == "2":
                print("\nyou open up your inbox. you have no emails")
            elif choice == "3":
                self.send_email()
            elif choice == "4":
                break
            else:
                print("invalid selection\n")

    # TODO: this needs events to have any gameplay value i think
    def check_calendar(self):
        while True:
            print("\n1. view calendar")
            print("2. return to computer")

            choice = input("\n> ")
            sys(choice)
            if choice == "1":
                print("\n" + ("=" * 20) + "\n")
                print("CALENDAR")
                print("\n" + ("=" * 20) + "\n")
            elif choice == "2":
                break
            else:
                print("invalid selection")

    # TODO: Need to create a bank class
    def check_bank(self):
        while True:
            print("1. view bank account")
            print("2. return to computer")

            choice = input("\n> ")
            sys(choice)
            if choice == "1":
                print("you view your bank account")
            elif choice == "2":
                break
            else:
                print("invalid selection")

    #
    def open_my_market(self):
        while True:

            print("\n1. view vendors")
            print("2. view bookings")
            print("3. book vendor")
            print("4. go back")

            choice = input("\n> ")
            sys(choice)
            if choice == "1":
                self.view_vendors()
            elif choice == "2":
                self.view_bookings()
            elif choice == "3":
                self.book_vendor()
            elif choice == "4":
                break
            else:
                print("invalid selection")

    def view_vendors(self):
        print("\ntotal vendor pool")
        print("\n" + ("=" * 20) + "\n")
        for vendor in self.state.vendor_pool.vendors:
            print(vendor.get_stats())

    def view_bookings(self):
        print("\ncurrent bookings")
        if len(self.state.bookings.vendors) == 0:
            print("\nno bookings yet...")
        else:
            for vendor in self.state.bookings.vendors:
                print(vendor.get_stats())


    def send_email(self):
        print("\nyou've sent an email. hooray")

    def book_vendor(self):
        print("\nbook a vendor")
        print("\n" + ("=" * 20) + "\n")
        print("1. select from available vendors")
        print("2. search for vendor by name")
        print("3. return to myMarket")

        choice = input("\n> ")
        sys(choice)
        if choice == "1":
            print("\navailable vendors")
            print("\n" + ("=" * 20) + "\n")
            available_vendors = [vendor for vendor in self.state.vendor_pool.vendors if not vendor.booked]
            for i, vendor in enumerate(available_vendors):
                print(f"{i + 1}. {vendor.get_stats()}")
            while True:
                choice = input("select vendor: ")
                sys(choice)
                if not choice.isdigit() or choice == "":
                    print("invalid selection")
                    continue
                index = int(choice)
                if index > len(available_vendors) or index < 1:
                    print("invalid selection")
                    continue
                vendor = available_vendors[index - 1]
                if not vendor.booked:
                    self.state.bookings.add_vendor(vendor)
                    vendor.booked = True
                    print("vendor booked")
                    break
                else:
                    print("vendor already booked")


        elif choice == "2":
            choice = input("enter vendor name: ")
            sys(choice)
            if choice not in self.state.vendor_pool.vendors:
                print("vendor not found")
            else:
                print("vendor found")
                print(self.state.vendor_pool.vendors[choice].get_stats())


        elif choice == "3":
            self.state.bookings.book_vendor()

        else:
            print("invalid selection")

