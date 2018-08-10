"""Print a menu and its prices"""
slang = ['Knackered', 'Pip pip', 'Squidgy', 'Smashing']

menu = []
for word in slang:
    menu.append(word + 'Spam')
print("***Menu***")
print(menu)

menu_prices = {}
price = 0.5
for item in menu:
    menu_prices[item] = price
    price += 0.5 

print("***Prices***")
for name, price in menu_prices.items():
    print(name, ': $',format(price,'.2f'), sep='')  

"""Order items"""
orders = []
order = input("What would you like to order? (Q to Quit) ")
while(order.upper() != 'Q'):
    #check if order exists in list
    found = menu.get(order)
    if found == True:
        orders.append(order)
    else:
        print("Menu item doesn't exist")

    #Ask if anything else to order
    order = input("Anything else to order? (Q to quit) ")

print(orders)
