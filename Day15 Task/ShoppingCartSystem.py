##3. Shopping Cart System 
##Scenario: A user adds items to a shopping cart. 
##Task: 
##● Store items in a list 
##● Convert to set to remove duplicates 
##● Use loop + condition to calculate total cost 
##● Handle invalid input using try-except 
##


prices = {
    "apple": 30,
    "banana": 10,
    "orange": 20,
    "mango": 50

}

cart = []

try:
    n = int(input("Enter number of items: "))


    for i in range(n):
        item = input("Enter item name:").lower()
        cart.append(item)


#Remove duplicates

    cart = set(cart)

    total = 0

    for item in cart:
        if item in prices:
            total += prices[item]
            print(item, ":", prices[item])

        else:
            print(item, "is not available")

    print("Total Cost:", total)

except ValueErroe:
    print("Please enter a valid number!")
