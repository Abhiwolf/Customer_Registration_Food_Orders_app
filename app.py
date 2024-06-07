class User:
    # build a constructor depending on the requirements of different parameters
    def __init__(self, username, password, membership):
        self.username = username
        self.password = password
        self.membership = membership
        self.cart = []

    # create a method to add food items with quantity to the cart
    def add_to_cart(self, food_item, quantity):
        item_with_quantity = {"food": food_item, "quantity": quantity}
        self.cart.append(item_with_quantity)

    # create a method to see food items in the cart
    def view_cart(self):
        if self.cart:
            total_price = 0
            print('Cart Items:')
            for item_with_quantity in self.cart:
                food_item = item_with_quantity["food"]
                quantity = item_with_quantity["quantity"]
                price = food_item.price * quantity
                total_price += price
                print(f"-{food_item.name}: ${food_item.price} * {quantity} = ${price}")

            discount_percentage = self.get_discount_percentage()
            discount_amount = total_price * (discount_percentage / 100)
            payable_amount = total_price - discount_amount

            print(f"total Price: ${total_price}")
            print(f"discount: {discount_percentage}%")
            print(f"Payable amount: ${payable_amount}")
        else:
            print("Cart is empty")

    # Add a method of discount to apply for different users with different memberships
    def get_discount_percentage(self):
        if self.membership == "gold":
            return 20
        elif self.membership == "platinum":
            return 30
        elif self.membership == "silver":
            return 10
        else:
            return 0


# create a class of food items
class FoodItem:
    # create a constructor to add food item names and their prices to the food list in a hotel
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


# food items list
food_items = [
    FoodItem(1, 'Pizza', 80.00),
    FoodItem(2, 'Biryani', 200.00),
    FoodItem(3, 'Veg Rice', 150.00),
    FoodItem(4, 'Dosa', 50.00)
]

# Register a new user
username = input("Enter a username: ")
password = input("Enter a password: ")
membership = input("Enter membership level (gold, platinum, silver, or None): ")
user = User(username, password, membership)
print('Registration successful')

# Adding items to the cart by using the above methods and the class since the user has to go to the hotel and order some food 
# Therefore user has to do some functions like adding some food items to the cart by ordering them to eat
while True:
    item_id = input("Enter the ID of the food item to add to cart (press Enter to exit): ")
    if not item_id:
        break
    item_id = int(item_id)
    food_item = next((item for item in food_items if item.id == item_id), None)
    if food_item:
        quantity = int(input("Enter the quantity: "))
        user.add_to_cart(food_item, quantity)
        print('Food item added to cart')
    else:
        print('Invalid food item ID')
    
    # call the function that will return operations done by the user.
    user.view_cart()
    