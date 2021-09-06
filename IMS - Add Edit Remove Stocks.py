import time
import json

#Dictionary to store stock details
stock_details = {}

file = open("stock.json", "r") #Reading JSON file
stock = file.read()
file.close()

stock_details = json.loads(stock)

#Main Interface
print("--------------------------------------------")
print("INVENTORY MANAGEMENT SYSTEM FOR STORE KEEPER")
print("--------------------------------------------")
c = ""
print("Enter    A - Add new product")
print("         E - Edit existing product")
print("         R - Remove existing product")
print("--------------------------------------------")
c = input("Enter your option: ")

#To add new products 
if c == "a" or c == "A" :
    #No. of new products to add
    n = int(input("Enter the no. of entries: "))
    #Product ID - Note the previous ID in the JSON
    prod_id = int(input("Enter the product ID: "))
    
    if str(prod_id) in stock_details:
        print("Product ID is already there!")
    else:
        for i in range(n):
            #Getting Product details
            prod_name = input("Enter Product name: ") # Product Name
            prod_price = input("Enter %s price: "%prod_name) # Product Price
            prod_quantity = input("Enter No. of Quantity: ") # Product Quantity
            last_update_time = time.ctime() # Time added
            print("\n")
            #Adding to Dictionary
            stock_details[prod_id] = {"name": prod_name, "price": prod_price, "quantity": prod_quantity, "last update" : last_update_time}
            #Next product ID            
            prod_id += 1

#To edit existing product details            
elif c == "e" or c == "E" :
    flag = input("Do you want to edit? (Y/N) : ")
    while(flag == "Y" or flag == "y"):
        prod_id = input("Enter Product ID: ")

        if prod_id in stock_details:
            #Displaying existing values
            print("Product Name:",stock_details[prod_id]["name"])
            print("Product Price:",stock_details[prod_id]["price"])
            print("Product Quantity:",stock_details[prod_id]["quantity"])
            print("\n")
            #Asking for the change in values
            print("What do you want to edit? ")
            print("Enter    N - Name")
            print("         P - Price")
            print("         Q - Quantity")
            choice = input("Enter your option: ")
        
            #Change in product name
            if choice == "N" or choice == "n":
                New_Name = input("Enter New Name: ")
                stock_details[prod_id]["name"] = New_Name
                last_update_time = time.ctime()
                stock_details[prod_id]["last update"] = last_update_time
            #Change in product price
            elif choice == "P" or choice == "p":
                New_Price = input("Enter New Price: ")
                stock_details[prod_id]["price"] = New_Price
                last_update_time = time.ctime()
                stock_details[prod_id]["last update"] = last_update_time
            #Change in product quantity
            elif choice == "Q" or choice == "q":
                print("Note: You have",stock_details[prod_id]["quantity"], "of",stock_details[prod_id]["name"])
                print("You are about to add new stock!")
                are_u_sure = input("Are you sure? (Y/N) : ")
            
                if are_u_sure == "Y" or are_u_sure == "y":
                    #Note: This will add new quantity with existing count of that product
                    New_Quantity = int(input("Enter New Quantity: "))
                    stock_details[prod_id]["quantity"] = int(stock_details[prod_id]["quantity"]) + New_Quantity
                    last_update_time = time.ctime()
                    stock_details[prod_id]["last update"] = last_update_time
            
        #Incorrect Product ID
        else:
            print("Product ID Not Found!")
            
        flag = input("Do you have any other change? (Y/N) : ")
        print("\n")

#To remove existing product
elif c == "r" or c == "R" :

    flag = input("Do you want to remove stocks? (Y/N) : ")

    while(flag == "Y" or flag == "y"):
        prod_id = input("Enter Product ID: ")
        
        if prod_id in stock_details:
            print("Product Name:",stock_details[prod_id]["name"])
            print("Product Price:",stock_details[prod_id]["price"])
            print("Product Quantity:",stock_details[prod_id]["quantity"])
            are_you_sure = input("Are you sure you want to remove %s? (Y/N) : " %stock_details[prod_id]["name"])
            
            if are_you_sure == "Y" or are_you_sure == "y":
                stock_details.pop(prod_id)
            
        else:
            print("Product ID Not Found!")
            
        flag = input("Do you have any other stock to remove? (Y/N) : ")
        print("\n") 

else:
    print("Command Not Found!")

#Creating JSON with updated dictionary    
stocks = json.dumps(stock_details)

file = open("stock.json", "w") #Updating JSON file
file.write(stocks)
file.close()

#BY - Nitheesh Kumaar M V