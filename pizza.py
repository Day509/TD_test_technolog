class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def __str__(self):
        return f"Pizza(size={self.size}, toppings={self.toppings})"

    def __repr__(self):
        return f"Pizza(size={self.size}, toppings={self.toppings})"