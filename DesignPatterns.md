# Design patterns

## 1. Singleton pattern
ensures a class is instantiated only once.

#### Application:
The InventoryManager class is implemented as a singleton class. This ensures that only one instance of the InventoryManager class is created to avoid conflicts in the inventory management system.

#### Before Singleton pattern:
Multiple instances of the InventoryManager class could be instansiated, which can result in conflicts in the inventory management system.

#### After Singleton pattern:
Only one instance of the InventoryManager class is created, which ensures that there are no conflicts in the inventory management system.

#### Code example:
```python
class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

## 2. Factory Method pattern
creates objects without specifying the exact class to create.

#### Application:
The pattern is used to create base pizzas (Margherita and Pepperoni) through MargheritaFactory and PepperoniFactory.

Before creating the pizza, the factory checks through the InventoryManager the availability of the required pizza type.

#### Before Factory Method pattern:
* Pizza creation was done directly in the main code, which results in less maintainable code.
* The complex process of pizza creation was done in the main code, resulting in code duplication.

#### After Factory Method pattern:
* The creation process is encapsulated in the factory classes, which results in more maintainable code.
* If any changes are required in the pizza creation process (a complex process), only the factory classes need to be updated.

#### Code example:
```python
class MargheritaFactory(PizzaFactory):
    def create_pizza(self):
        if self.inventory_manager.check_and_decrement("Margherita"):
            return MargheritaPizza()
        raise ValueError("Margherita pizza is out of stock")
```

## 3. Decorator Pattern
dynamically adds new functionality to an object.

#### Application:
used to add toppings (Cheese, Olives, or Mushrooms) to a pizza dynamically.

#### Before Decorator pattern:
The pizza class had multiple subclasses for each pizza type with different toppings. This resulted in a large number of subclasses and code duplication.

#### After Decorator pattern:
The additional toppings are added dynamically to the pizza object without the need for multiple subclasses.

#### Code example:
```python
class CheeseTopping(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()} + Cheese"

    def get_cost(self):
        return self._pizza.get_cost() + 1.0
```

## 4. Strategy Pattern
using different encapsulated algorithms interchangeably.

#### Application:
used to implement different payment methods (Credit Card or PayPal) interchangeably.

#### Before Strategy pattern:
payment methods were hardcoded using if-else statements, which resulted in code duplication and less maintainable code.

#### After Strategy pattern:
adding a new payment method is easier as it only requires creating a new payment strategy class.

#### Code example:
```python
class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount} using PayPal")

class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        self.payment_strategy.pay(amount)
```

## Overengineering
when the design of the system is more complex than necessary by adding unnecessary abstractions or functionality.

We tried to avoid overengineering by keeping the design simple and only adding design patterns where necessary.

#### Example:
adding a ToopingFactory class to create toppings for pizzas would be an example of overengineering as the toppings can be directly created in the Decorator pattern.

```python
class ToppingFactory:
    def add(self, topping_type):
        if topping_type == "Cheese":
            return CheeseTopping()
        elif topping_type == "Olives":
            return OlivesTopping()
        elif topping_type == "Mushrooms":
            return MushroomsTopping()
        else:
            raise ValueError("Invalid topping type")
```

This factory class adds unnecessary complexity to the system without providing any additional value.