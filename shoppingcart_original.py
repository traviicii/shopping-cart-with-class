
def checkout(cart):  #takes products list and prints the finalized cart
    
    total =  0
    
    print("\n****** Finalized Cart ******")
    print("Items --------------- Price\n")
    for item in cart:
        if cart[item][0] == 0:
            continue
        else:
            price = float(cart[item][1]) * float(cart[item][0])
            total += price
            if item == "ranch dressing":
                print(f"{item.title()} --------- ${cart[item][1]}")
            else:
                print(f"{item.title()}, Qty: {int(cart[item][0])} --------- ${round(price, 2)}")
    print("******************************")
    print(f"Your total for this visit is: ${round(total, 2)}\n")
    print("<3 Thank you sooooo much for shopping here!! <3")
                  
    return

def showcart(cart):

    subtotal = 0

    print("\n****** Shopping Cart ******")
    print("Items --------------- Price\n")
    for item in cart:           #for each item in cart, if Qty == 0, skip it. Otherwise
        if cart[item][0] == 0:
            continue
        else:
            price = float(cart[item][1]) * float(cart[item][0])
            subtotal += price
            if item == "ranch dressing":
                    print(f"{item.title()} --------- ${cart[item][1]}")
            else:
                print(f"{item.title()}, Qty: {int(cart[item][0])} --------- ${round(price, 2)}")
    print("****************************")
    print(f"Your current subtotal is: ${round(subtotal, 2)}\n")

    return



def initiate_cart():

    products = {
    'eggs': [0, 4.99],
    'milk': [0, 4.38],
    'bread': [0, 3.00],
    'coffee': [0, 8.49],
    'cheese': [0, 6.25],
    'oat milk': [0, 3.50],
    'ice cream': [0, 5.99],
    'pizza': [0, 9.99],
    'ranch dressing': [0, 250],
    'seltzer': [0, 2.00],
    'sour cream': [0, 3.00],
}

    print("\nWelcome to Travii's Lil Mini-Marketplace!\n")
    while True:
        action = input("\nWhat would you like to do? (prices/add/remove/view/checkout): ")
        if action.lower() == "checkout":
            checkout(products)
            break
        elif action.lower() == "add":
            additem = input("\nWhat item would you like to add? ")
            if additem not in products:
                number = input("\nWow we don't even have this product, but we'll sell it to you anyways!\nEnter the price. And don't put a $, we'll do that for you. ")
                if "$" in number:
                    print("How dare you add a '$' when we specifically told you not to. You can head right back tot he main menu playing games like that.")
                    continue
                else:
                    products[additem] = [input("How many are you buying? "), number]

            elif additem.lower() in products:
                products[additem][0] = input("How many? ")
        
        elif action.lower() == "remove":

            item = input("\nWhat item would you like to remove from your cart? ")   #assigns item to be romoved
            if item not in products.keys() or int(products[item][0]) == 0:    #catches error if item wasn't added initially
                print("Yo, that's not even in your cart. How you gonna try and remove it, son?")
                #assigns item to be removed
                    
            elif int(products[item.lower()][0]) > 1:       #if the quantity to remove is larger than 1, ask if they wanna remove all of them or a specified number
                decision = input("\nWould you like to remove all of this item or a certain number? (Enter 'all' or the amount you'd like to remove): ")

                if decision.lower() == "all":   #if the respond with all, remove by changing the quantity to 0
                    products[item][0] = 0
                    print(f"\nSuccesfully removed {item} from your cart!")
                
                elif float(decision.lower()) > float(products[item.lower()][0]):  #if quantity to remove is larger than what is actually in the cart, show error and break the loop
                    print("\nSorry but you entered a number larger than the amount of this item currently in your cart.\nTry viewing your cart to see how many items you have, fool.\n")
                    continue

                else:   #otherwise remove the specified amount
                    products[item][0] = float(products[item][0]) - float(decision)
                    print(f"\nSuccesfully removed {decision} {item}!")
            
            else:   #if there's only one of the product in the cart just remove it
                products[item][0] = 0
                print(f"\nSuccesfully removed {item.title()} from your cart!")
        
        elif action.lower() == "prices":
            print("\n-----Products currently available-----")
            print("---Items --------------- Price---\n")
            for item in products:
                if item == "ranch dressing":
                    print(f"   {item.title()} --------- ${products[item][1]} (**It's fancy ranch, no one's forcing you to buy it, but then you won't have any ranch. It's your call.**)")
                else:
                    print(f"   {item.title()} -------------- ${products[item][1]}")
            print("\nIf there's something you wanna buy that isn't in our inventory of products, just add it to your cart anyways, we'd love to take your money!!")

        else:
            if action.lower() == "view":
                showcart(products)
        

initiate_cart()