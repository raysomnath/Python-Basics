import sys

class Tab:
    
    # Class attribute
    menu = {
        'wine' : 5,
        'beer' : 3,
        'soft_drink' : 2,
        'chicken' : 10,
        'beef' : 15,
        'veggie' : 12,
        'dessert' : 6
    }

    # Instance attributes initialization
    def __init__(self):
        self.total = 0
        self.items = []

    # Instance method
    def add(self,item):
        self.items.append(item)
        self.total += self.menu[item]

    # Instance method
    def print_bill(self,tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20} ${self.menu[item]}')

        print(f'{"Total":20} ${total:.2f}')