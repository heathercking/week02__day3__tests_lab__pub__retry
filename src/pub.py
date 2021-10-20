class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
    
    def drink_count(self):
        return len(self.drinks)
    
    def add_drink(self, drink):
        self.drinks.append(drink)
    
    def serve_drink(self, drink, customer):
        if self.customer_is_old_enough(customer) == True and self.customer_is_too_drunk == True:
            customer.buy_drink(drink)
            self.till += drink.price
    
    def customer_is_old_enough(self, customer):
        return customer.age >= 18
    
    def customer_is_too_drunk(self, customer):
        return customer.drunkenness >= 30
