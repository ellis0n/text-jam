import vendor
import vendors


class GameState:
    def __init__(self, week, day, vendor_pool, booked):
        self.week = 1
        self.day = 1
        self.vendor_pool = vendor.VendorPool(10)
        self.booked = vendor.VendorPool(5)

    def increment_day(self):
        self.day += 1

    def increment_week(self):
        self.week += 1
        self.day = 1

    def get_week(self):
        return self.week

    def get_day(self):
        return self.day
