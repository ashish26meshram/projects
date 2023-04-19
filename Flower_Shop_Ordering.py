class Flower:
    def __init__(self, name, color, price, quantity):
        self.name = name
        self.color = color
        self.price = price
        self.quantity = quantity

    def display_flower(self):
        print(f"{self.name} ({self.color}): {self.price} - {self.quantity} in stock")

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def display_bouquet(self):
        total_price = 0
        for flower in self.flowers:
            flower.display_flower()
            total_price += flower.price
        print(f"Total price: {total_price}")

class FlowerShop:
    def __init__(self):
        self.inventory = {}

    def add_flower(self, flower):
        if flower.name in self.inventory:
            self.inventory[flower.name].quantity += flower.quantity
        else:
            self.inventory[flower.name] = flower

    def create_bouquet(self, flowers):
        bouquet = Bouquet()
        for flower in flowers:
            if self.inventory[flower.name].quantity == 0:
                print(f"{flower.name} is out of stock")
                return None
            else:
                bouquet.add_flower(flower)
                self.inventory[flower.name].quantity -= 1
        return bouquet

    def display_inventory(self):
        print("Flower Inventory:")
        for flower in self.inventory.values():
            flower.display_flower()

# Sample usage
shop = FlowerShop()
shop.add_flower(Flower("Rose", "Red", 2.99, 10))
shop.add_flower(Flower("Rose", "White", 2.99, 5))
shop.add_flower(Flower("Lily", "Yellow", 3.99, 7))
shop.add_flower(Flower("Tulip", "Pink", 1.99, 3))

shop.display_inventory()

bouquet1 = shop.create_bouquet([Flower("Rose", "Red", 2.99, 3), Flower("Lily", "Yellow", 3.99, 2)])
if bouquet1:
    bouquet1.display_bouquet()

bouquet2 = shop.create_bouquet([Flower("Rose", "White", 2.99, 2), Flower("Tulip", "Pink", 1.99, 2)])
if bouquet2:
    bouquet2.display_bouquet()

shop.display_inventory()
