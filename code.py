from abc import ABC, abstractmethod


# =================== Pizza ===================== #
# Abstract pizza class
class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass
    @abstractmethod
    def get_cost(self):
        pass

class MargheritaPizza(Pizza):
    def get_description(self):
        return "Margherita pizza"
    def get_cost(self):
        return 5.0

class PepperoniPizza(Pizza):
    def get_description(self):
        return "Pepperoni pizza"
    def get_cost(self):
        return 6.0

# =================== Pizza Factory ===================== #
# Factory mathod pattern
class PizzaFactory(ABC):
    def __init__(self):
        self.inventory_manager = InventoryManager()
    
    @abstractmethod
    def create_pizza(self):
        pass

class MargheritaFactory(PizzaFactory):
    def create_pizza(self):
        if self.inventory_manager.check_and_decrement("Margherita"):
            return MargheritaPizza()
        raise ValueError("Margherita pizza is out of stock")

class PepperoniFactory(PizzaFactory):
    def create_pizza(self):
        if self.inventory_manager.check_and_decrement("Pepperoni"):
            return PepperoniPizza()
        raise ValueError("Pepperoni pizza is out of stock")

# =================== Toppings Decorators ===================== #
# Decorator pattern
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza
        self.inventory_manager = InventoryManager()
        self.added = False

    def get_description(self):
        pass
    def get_cost(self):
        pass

class CheeseTopping(ToppingDecorator):   
    def __init__(self, pizza):
        super().__init__(pizza)
        if not self.inventory_manager.check_and_decrement("Cheese"):
            print("Cheese topping is out of stock!")
        else:
            self.added = True

    def get_description(self):
        if not self.added:
            return self._pizza.get_description()
        return f"{self._pizza.get_description()} + Cheese"

    def get_cost(self):
        if not self.added:
            return self._pizza.get_cost()
        return self._pizza.get_cost() + 1.0

class OlivesTopping(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        if not self.inventory_manager.check_and_decrement("Olives"):
            print("Olives topping is out of stock!")
        else:
            self.added = True
    
    def get_description(self):
        if not self.added:
            return self._pizza.get_description()
        return f"{self._pizza.get_description()} + Olives"

    def get_cost(self):
        if not self.added:
            return self._pizza.get_cost()
        return self._pizza.get_cost() + 0.5

class MushroomsTopping(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        if not self.inventory_manager.check_and_decrement("Mushrooms"):
            print("Mushrooms topping is out of stock!")
        else:
            self.added = True
    
    def get_description(self):
        if not self.added:
            return self._pizza.get_description()
        return f"{self._pizza.get_description()} + Mushrooms"

    def get_cost(self):
        if not self.added:
            return self._pizza.get_cost()
        return self._pizza.get_cost() + 0.7

# ============== Payment ============== #
# Strategy pattern

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount} using PayPal")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount} using Credit Card")

# payment processor
class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        self.payment_strategy.pay(amount)
        return True

# Singleton Inventory Manager
class InventoryManager:
    _instance = None

    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory


# ============== Main Function ============== #
def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        pizza_factory = None

        if pizza_choice == '0':
            break
        elif pizza_choice == "1":
            pizza_factory = MargheritaFactory()
        elif pizza_choice == "2":
            pizza_factory = PepperoniFactory()
        else:
            print("\nInvalid choice!")
            continue
        

        # Create pizza
        try:
            pizza = pizza_factory.create_pizza()
        except ValueError as e:
            print(e)
            continue


        # Add toppings
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")
            # Cheese
            if topping_choice == "1" :
                pizza = CheeseTopping(pizza)
            # Olive
            elif topping_choice == "2":
                pizza = OlivesTopping(pizza)
            # Mushrooms
            elif topping_choice == "3":
                pizza = MushroomsTopping(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        # Display final pizza details
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        # Payment
        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == "1":
            payment_strategy = PayPalPayment()
        elif payment_choice == "2":
            payment_strategy = CreditCardPayment()
        else:
            print("Invalid payment method! Pay cash.")

        payment_processor = PaymentProcessor(payment_strategy)
        payment_success = payment_processor.pay(pizza.get_cost())

        if payment_success:
            print("Payment processed successfully")
        # Show final inventory
        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()