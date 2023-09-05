class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


class Admin(User):
    def change_price(self, item, new_price):
        item.price = new_price


class InternetShop:
    def __init__(self):
        self.items = []
        self.users = []
        self.warehouse = {}

    def add_item(self, item):
        self.items.append(item)

    def add_user(self, user):
        self.users.append(user)

    def login(self, username, password):
        for user in self.users:
            if user.name == username and user.password == password:
                return user
        return None

    def get_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def update_item(self, name, new_price):
        item = self.get_item(name)
        if item:
            item.price = new_price
            return True
        return False

    def delete_item(self, name):
        item = self.get_item(name)
        if item:
            self.items.remove(item)
            return True
        return False

    def add_to_warehouse(self, item_name, amount):
        if item_name in self.warehouse:
            self.warehouse[item_name] += amount
        else:
            self.warehouse[item_name] = amount

    def remove_from_warehouse(self, item_name, amount):
        if item_name in self.warehouse:
            if self.warehouse[item_name] >= amount:
                self.warehouse[item_name] -= amount
                return True
        return False


# Example usage:
shop = InternetShop()

# Register users
user1 = User("User 1", "qwe123")
admin = Admin("Admin", "adminpass")
shop.add_user(user1)
shop.add_user(admin)

# Add items to the shop and warehouse
item1 = Item("Headphones", 50)
item2 = Item("Mouse", 20)
item3 = Item("Keyboard", 30)
item4 = Item("Monitor", 200)
item5 = Item("Laptop", 800)
item6 = Item("Speakers", 40)
item7 = Item("Webcam", 60)
item8 = Item("Router", 70)
item9 = Item("Printer", 100)
item10 = Item("Smartphone", 600)

shop.add_item(item1)
shop.add_item(item2)
shop.add_item(item3)
shop.add_item(item4)
shop.add_item(item5)
shop.add_item(item6)
shop.add_item(item7)
shop.add_item(item8)
shop.add_item(item9)
shop.add_item(item10)

shop.add_to_warehouse(item1.name, 10)
shop.add_to_warehouse(item2.name, 15)
shop.add_to_warehouse(item3.name, 12)
shop.add_to_warehouse(item4.name, 5)
shop.add_to_warehouse(item5.name, 8)
shop.add_to_warehouse(item6.name, 20)
shop.add_to_warehouse(item7.name, 7)
shop.add_to_warehouse(item8.name, 10)
shop.add_to_warehouse(item9.name, 3)
shop.add_to_warehouse(item10.name, 15)

# Login sequence
logged_in_user = None
while not logged_in_user:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    logged_in_user = shop.login(username, password)
    if not logged_in_user:
        print("Invalid username or password. Please try again.")

print(f"Logged in as {logged_in_user.name}")

# Display available items
print("Available Items:")
for item in shop.items:
    print(f"{item.name} - Price: ${item.price}")

# User selects an item to buy
selected_item = None
while not selected_item:
    item_name = input("Enter the name of the item you want to buy: ")
    selected_item = shop.get_item(item_name)
    if not selected_item:
        print("Invalid item name. Please try again.")

# Remove item from warehouse
if shop.remove_from_warehouse(selected_item.name, 1):
    print(f"{selected_item.name} successfully deducted from the warehouse.")
else:
    print(f"Failed to deduct {selected_item.name} from the warehouse. Insufficient quantity.")

# Prompt user to insert money
amount_due = selected_item.price
while amount_due > 0:
    payment = float(input("Please insert money: $"))
    if payment >= amount_due:
        change = payment - amount_due
        print(f"Payment successful! Your change is ${change:.2f}")
        break
    else:
        print("Insufficient payment. Please insert more money.")
        amount_due -= payment

# Finalize the purchase
print("Thank you for your purchase!")

# Display updated warehouse
print("Updated Warehouse:")
for item_name, amount in shop.warehouse.items():
    print(f"{item_name}: {amount}")
