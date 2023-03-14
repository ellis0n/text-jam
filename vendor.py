class Vendor:
    def __init__(self, name, category, level):
        self.name = name
        self.category = category
        self.level = level
        self.experience = 0
        self.booked = False

    def __str__(self):
        return f"{self.name}"

    def book(self):
        self.booked = True

    def cancel(self):
        self.booked = False

    def level_up(self):
        self.level += 1

    def add_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()
            self.experience = 0


class VendorPool:
    def __init__(self, limit):
        self.vendors = []
        self.limit = limit

    def add_vendor(self, vendor):
        if len(self.vendors) < self.limit:
            self.vendors.append(vendor)
        else:
            print("vendor pool is full")

    def remove_vendor(self, vendor):
        self.vendors.remove(vendor)

    def get_vendor(self, vendor_name):
        for vendor in self.vendors:
            if vendor.name == vendor_name:
                return vendor
        return None

    def change_limit(self, amount):
        self.limit += amount

    def get_vendors(self):
        return self.vendors


