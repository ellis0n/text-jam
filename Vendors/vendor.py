class Vendor:
    def __init__(self, name='name', business_name="business_name", category='category'):
        self.name = name
        self.business_name = business_name
        self.category = category
        self.level = 1
        self.experience = 0
        self.booked = False
    def __str__(self):
        return f"{self.name}"

    def book(self):
        self.booked = True

    def unbook(self):
        self.booked = False

    def level_up(self):
        self.level += 1

    def add_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()
            self.experience = 0

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_level(self):
        return self.level

    def get_experience(self):
        return self.experience

    def get_booked(self):
        return self.booked

    def get_stats(self):
        return f"{self.name} is a level {self.level} {self.category} vendor"

