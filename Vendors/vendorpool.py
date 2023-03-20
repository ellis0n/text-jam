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


