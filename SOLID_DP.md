# Relation between SOLID principles and Design patterns

## Design Patterns with SOLID Principles

### 1. Singleton pattern

#### Single Responsibility Principle:
ensures single responsibility of inventory management.

### 2. Factory Method pattern

#### Single Responsibility Principle:
each factory class is responsible for creating a specific type of pizza.

#### Open Closed Principle:
to add new pizza types, new factory classes can be added without modifying existing code.

### 3. Decorator Pattern

#### Open Closed Principle:
allows adding new toppings to a pizza dynamically without modifying the pizza class.

#### Liskov Substitution Principle:
decorator classes can be substituted for the base pizza class.

### 4. Strategy Pattern

#### Open Closed Principle:
add new payment methods by creating new strategy classes without modifying existing code.

#### Dependency Inversion Principle:
decoupling the payment methods from specific method implementations using an paymentmethod interface.