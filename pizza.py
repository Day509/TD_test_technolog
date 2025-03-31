class Pizza:
    def __init__(self, nom, price, toppings):
        self.nom = nom
        self.price = price
        self.toppings = toppings

    def __str__(self):
        return f"{self.nom} ({self.price} €) - Toppings: {', '.join(self.toppings)}"
    
    def __repr__(self):
        return f"Pizza(nom={self.nom}, price={self.price}, toppings={self.toppings})"