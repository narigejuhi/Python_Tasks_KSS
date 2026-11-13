#Q2: Develop a Python program for a small shop to process customer purchases. Store product 
##names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
##and product details using tuples. Create functions to display products, add items to the cart, and 
##calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 
##Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError 
##(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product 
##name entered by the user does not exist).


# Product dictionary
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

# Product categories using set
categories = {"Stationery", "Writing", "Books"}

# Product details using tuples
product_details = (
    ("Pen", 10),
    ("Notebook", 50),
    ("Pencil", 5)
)

# Cart using list
cart = []


# Function to display products
def display_products():
    print("\nAvailable Products:")

    for name, price in products.items():
        print(name, ":", price)


# Function to add items to cart
def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError

        price = products[name]

        cart.append((name, quantity, price))

        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")

    except TypeError:
        print("Cart data type error.")


# Recursive function to calculate total
def calculate_total(items):
    if len(items) == 0:
        return 0

    name, quantity, price = items[0]

    return (quantity * price) + calculate_total(items[1:])


# Function to display total bill
def total_bill():
    try:
        if len(cart) == 0:
            print("Cart is empty.")
            return

        print("\nItems in Cart:")

        for name, quantity, price in cart:
            print(name, "x", quantity)

        total = calculate_total(cart)

        print("\nTotal Bill:", total)

    except ZeroDivisionError:
        print("Calculation error: division by zero.")

    except TypeError:
        print("Cart data type error.")


# Main menu
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            total_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")
