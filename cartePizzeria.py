from cartePizzeriaException import CartePizzeraException
from pizza import Pizza

class CartePizzeria:
    """
    Classe représentant la carte d'une pizzeria.
    """

    def __init__(self):
        """
        Initialise la carte avec des pizzas prédéfinies.
        """
        self.pizzas = {
            Pizza("Margherita", 8.50, ["Tomato", "Mozzarella"]),
            Pizza("Pepperoni", 9.00, ["Tomato", "Mozzarella", "Pepperoni"]),
            Pizza("Hawaiian", 10.00, ["Tomato", "Mozzarella", "Ham", "Pineapple"]),
            Pizza("Vegetarian", 9.50, ["Tomato", "Mozzarella", "Bell Peppers", "Olives"]),
            Pizza("BBQ Chicken", 11.00, ["BBQ Sauce", "Chicken", "Red Onion"]),
        }
            
    def is_empty(self):
        """
        Vérifie si la carte est vide.
        """
        return len(self.pizzas) == 0
    
    def nb_pizzas(self):
        """
        Retourne le nombre de pizzas dans la carte.
        """
        return len(self.pizzas)
    
    def add_pizza(self, nom, prix):
        """
        Ajoute une pizza à la carte.
        :param nom: Nom de la pizza
        :param prix: Prix de la pizza
        """
        if nom in self.pizzas:
            raise ValueError(f"La pizza '{nom}' existe déjà dans la carte.")
        self.pizzas[nom] = prix
        
    def remove_pizza(self, nom):
        """
        Supprime une pizza de la carte.
        :param nom: Nom de la pizza à supprimer
        """
        if nom not in self.pizzas:
            raise CartePizzeraException(f"La pizza '{nom}' n'existe pas dans la carte.")
        del self.pizzas[nom]
        print(f"La pizza '{nom}' a été supprimée de la carte.")
        