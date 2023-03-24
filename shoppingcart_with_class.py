class Shoppingcart():
    def __init__(self):
        self.products = {
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
        
    def checkout(self):  #takes products list and prints the finalized cart
    
        total =  0
    
        print("\n****** Finalized Cart ******")
        print("Items --------------- Price\n")
        for item in self.products:
            if self.products[item][0] == 0:
                continue
            else:
                price = float(self.products[item][1]) * float(self.products[item][0])  
                total += price
                if item == "ranch dressing":
                    print(f"{item.title()} --------- ${self.products[item][1]}")
                else:
                    print(f"{item.title()}, Qty: {int(self.products[item][0])} --------- ${round(price, 2)}")
        print("******************************")
        print(f"Your total for this visit is: ${round(total, 2)}\n")
        print("<3 Thank you sooooo much for shopping here!! <3\n")
        return 
    
    def showCart(self):

        subtotal = 0

        print("\n****** Shopping Cart ******")
        print("Items --------------- Price\n")
        for item in self.products:           #for each item in cart, if Qty == 0, skip it. Otherwise
            if self.products[item][0] == 0:
                continue
            else:
                price = float(self.products[item][1]) * float(self.products[item][0])
                subtotal += price
                if item == "ranch dressing":
                        print(f"{item.title()} --------- ${self.products[item][1]}")
                else:
                    print(f"{item.title()}, Qty: {int(self.products[item][0])} --------- ${round(price, 2)}")
        print("****************************")
        print(f"Your current subtotal is: ${round(subtotal, 2)}\n")

        return
    
    def addItem(self):
        additem = input("\nWhat item would you like to add? ")
        if additem not in self.products:
            number = input("\nWow we don't even have this product, but we'll sell it to you anyways!\nEnter the price. And don't put a $, we'll do that for you. ")
            if "$" in number:
                print("How dare you add a '$' when we specifically told you not to. You can head right back tot he main menu playing games like that.")
                #continue
            else:
                self.products[additem] = [input("How many are you buying? "), number]

        elif additem.lower() in self.products:
            self.products[additem][0] = input("How many? ")
    
    def removeItem(self):
        item = input("\nWhat item would you like to remove from your cart? ")   #assigns item to be romoved
        if item not in self.products.keys() or int(self.products[item][0]) == 0:    #catches error if item wasn't added initially
            print("Yo, that's not even in your cart. How you gonna try and remove it, son?")
            #assigns item to be removed
                
        elif int(self.products[item.lower()][0]) > 1:       #if the quantity to remove is larger than 1, ask if they wanna remove all of them or a specified number
            decision = input("\nWould you like to remove all of this item or a certain number? (Enter 'all' or the amount you'd like to remove): ")

            if decision.lower() == "all":   #if the respond with all, remove by changing the quantity to 0
                self.products[item][0] = 0
                print(f"\nSuccesfully removed {item} from your cart!")
            
            elif float(decision.lower()) > float(self.products[item.lower()][0]):  #if quantity to remove is larger than what is actually in the cart, show error and break the loop
                print("\nSorry but you entered a number larger than the amount of this item currently in your cart.\nTry viewing your cart to see how many items you have, fool.\n")
                #continue

            else:   #otherwise remove the specified amount
                self.products[item][0] = float(self.products[item][0]) - float(decision)
                print(f"\nSuccesfully removed {decision} {item}!")

        else:   #if there's only one of the product in the cart just remove it
            self.products[item][0] = 0
            print(f"\nSuccesfully removed {item.title()} from your cart!")

    def showPrices(self):
        print("\n-----Products currently available-----")
        print("---Items --------------- Price---\n")
        for item in self.products:
            if item == "ranch dressing":
                print(f"   {item.title()} --------- ${self.products[item][1]} (**It's fancy ranch, no one's forcing you to buy it, but then you won't have any ranch. It's your call.**)")
            else:
                print(f"   {item.title()} -------------- ${self.products[item][1]}")
        print("\nIf there's something you wanna buy that isn't in our inventory of products, just add it to your cart anyways, we'd love to take your money!!")

    def initiate_Cart(self):

        print("\nWelcome to Travii's Lil Mini-Marketplace!\n")
        while True:
            action = input("\nWhat would you like to do? (prices/add/remove/view/checkout): ")
            if action.lower() == "checkout":
                self.checkout()
                break
            elif action.lower() == "add":
                self.addItem()
            
            elif action.lower() == "remove":
                self.removeItem()
            
            elif action.lower() == "prices":
                self.showPrices()

            else:
                if action.lower() == "view":
                    self.showCart()


travii = Shoppingcart()

print(travii.initiate_Cart())