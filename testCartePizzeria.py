from cartePizzeria import CartePizzeria
from mock import Mock 


cp = CartePizzeria()
   
def test_is_empty():
   
   cp.pizzas = {}
   assert cp.is_empty()
   

def test_is_not_empty():
   pizza = Mock()
   
   cp.pizzas = {pizza}
   assert not cp.is_empty()
   
def test_nb_pizzas():
   pizza1 = Mock()
   pizza2 = Mock()
   pizza3 = Mock()
   
   cp.pizzas = {pizza1, pizza2, pizza3}
   assert cp.nb_pizzas() == 3
   
def test_add_pizza():
   cp.pizzas = {}
   cp.add_pizza("Margherita", 8.50)
   assert "Margherita" in cp.pizzas
   assert cp.pizzas["Margherita"] == 8.50
   
def test_remove_pizza_with_name():
   cp.pizzas = {}
   pizza = Mock()
   pizza.nom = "Margherita"
   pizza.price = 8.50
   cp.add_pizza(pizza.nom, pizza.price)
   cp.remove_pizza(pizza.nom)
   assert pizza.nom not in cp.pizzas
   
   