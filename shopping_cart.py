# shopping_cart.py
from datetime import datetime
import os   

# bonus challenge configuring sales tax rate 
TAX_RATE = os.getenv("TAX_RATE", default="0.085")
print("The assumed tax rate is", TAX_RATE)
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


matching_products = []
# TODO: write some Python code here to produce the desired output

# Prompt users for valid input
print("Please enter product ID range from 1 through 20.")
print("Please ebter 'DONE' when you are finished. ")

while True:

# Ask for a user input 

    product_id = input("Please input a product identifier: ")

    if product_id == "DONE" :
        break

    # Look up corresponding products 
    # Print the product that has an id attribute equal to "0"
    
    # variable to test if the input is valid or not
    n = 0

    for x in products:
        #if x == 3:
        #    ___.append(x)
        #print(x)
        #print(x["id"])
        if str(x["id"]) == str(product_id):
            # this is a match
            matching_products.append(x)    
        else:
            # increment n by 1 if this is not a match
            n = n + 1
    # if n reaches 20, then none of the product ID is a match
    if n == 20:
        print("Please enter a valid input!")

            

# print(matching_products)
# print(type(matching_products))
# print(len(matching_products))
# print the name of the matching product
matching_product = matching_products[0]
print("#> ---------------------------------")
print("#> GU FRESH FOOD")
print("#> WWWW.GUFOOD.COM")
print("#> ---------------------------------")
# print the date and time
Time1 = datetime.now()
print("#> CHECKOUT AT: ", Time1.strftime("%d/%m/%Y %H:%M:%S"))
print("#> SELECTED PRODUCTS")
total_price = 0.00
for y in matching_products:

    print("#> ...", y["name"], "(", to_usd((y["price"])), ")")
    total_price = total_price + y["price"]
print("#> ---------------------------------")
print("#> SUBTOTAL:", to_usd(total_price))
# assume that the tax rate is 8.5% of the total price
TAX_RATE = float(TAX_RATE)
print("#> TAX:", to_usd(total_price*TAX_RATE))
print("#> TOTAL:", to_usd(total_price*(1+TAX_RATE)))
print("#> ---------------------------------")
print("#> THANK YOU, SEE YOU NEXT TIME!!")
print("#> ---------------------------------")
