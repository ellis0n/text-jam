from Vendors import vendor, vendorpool


class GameState:
    def __init__(self, week, day, vendor_pool, booked):
        self.week = 1
        self.day = 1
        self.vendor_pool = vendorpool.VendorPool(10)
        self.bookings = vendorpool.VendorPool(5)

    def increment_day(self):
        if self.day == 7:
            self.day = 1
            self.week += 1
        else:
            self.day += 1

    def increment_week(self):
        self.week += 1
        self.day = 1

    def get_week(self):
        return self.week

    def get_day(self):
        return self.day

    def get_vendor_pool(self):
        return self.vendor_pool


    def get_bookings(self):
        return self.bookings

    def increase_vendor_pool(self, amount):
        self.vendor_pool.change_limit(amount)

    def get_week_and_day(self):
        print(f"\nweek {self.week}, day {self.day}")