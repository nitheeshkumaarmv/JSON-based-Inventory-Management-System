import time
import json

#Opening the stocks file
file = open("stock.json", "r")
stocks = file.read()
file.close()

stock_details = json.loads(stocks)

#Main Menu to list all available products for customer to choose
print("----------------------------------------------------------")
print("Main Menu".center(56))
print("----------------------------------------------------------")
print("  Product ID\t    Name \t                 Price ")
print("----------------------------------------------------------")
    
for i in stock_details:
    y = stock_details[i]
    print("  %4s\t\t    %-25s\t %-5.2f"%(i,y["name"],float(y["price"])))
    
print("----------------------------------------------------------")
    
  
c = "Y"   
cart = [] #Customer's shopping cart

print("\n")
print("Did you find what to buy?")
    
while(c=="Y" or c=="y"):
    
    user_prod_id = input("Enter the Product ID of the item you want: ")
    
    if user_prod_id in stock_details: #Adding product to customer's cart
    
        user_quantity = int(input("How much do you need? "))
        
        if user_quantity <= int(stock_details[user_prod_id]["quantity"]):
            
            purchase = user_prod_id + "#" + str(user_quantity)
            cart.append(purchase) #List format: ProductID#Quantity - ex: 1001#25
        
            c = input("Do you want to purchase more? (Y/N) : ")
            
        else: #When our available stock is less than customer's need
            print("We have just %s %s left"%(stock_details[user_prod_id]["quantity"],stock_details[user_prod_id]["name"]))
         
    else:
        print("Product ID Not Found!")
    
    print("\n")
    
#Displaying the products in the cart 
print("-------------------------------------------------")
print(" Items in your Cart: ")
print("-------------------------------------------------")
print("    Name \t\t\t     Quantity  \t\t")
print("-------------------------------------------------")

for j in range(len(cart)):
    x = cart[j]
    prod_id,quantity = x.split("#") #splitting product ID and Quantity to two variables
    print("%-2d. %-30s \t%-3s"%(j+1,stock_details[prod_id]["name"],quantity))
print("-------------------------------------------------")    
    
#If user want to remove some product from cart
remove_cart = input("Do you want to remove any item? (Y/N) : ")
while(remove_cart=="y" or remove_cart=="Y"):
    num = int(input("Enter Product number from your cart: "))
    cart.pop(num-1)
    remove_cart = input("Do you want to remove any other item? (Y/N) : ")
    

print("\n")
print("You are about to check out your items!") #About to Billing process

amount = 0           #product price x quantity
total_cost = 0       #sum of all products' amount

print("***********************************************************")
print("Your Bill".center(56))
print("***********************************************************")
print(" Date & Time: %s"%(time.ctime())) #Time and Date of purchasing
print("-----------------------------------------------------------")
print("     Name \t\t  Quantity \t Price     Amount ")
print("-----------------------------------------------------------")

#Generating Bill of purchased items    
for j in range(len(cart)):
    x = cart[j]
    prod_id,quantity = x.split("#")
    quantity = int(quantity)
    amount = float(stock_details[prod_id]["price"])*quantity
    total_cost += amount
    print("%-2d. %-20s    %-3d \t %-5.2f     %-5.2f"%(j+1,stock_details[prod_id]["name"],quantity,float(stock_details[prod_id]["price"]),amount))    
    
print("***********************************************************")
print("\t\t\t\t    Total Amount: %-8.2f"%(float(total_cost)))          #Total Amount to be paid
print("***********************************************************")
print("\n")
print("Happy Purchasing!!".center(56))
print("\n")

#Update to Inventory JSON
for i in range(len(cart)):
    x = cart[i]
    prod_id,quantity = x.split("#")
    quantity = int(quantity)
    #Updating stock quantity
    stock_details[prod_id]["quantity"] = int(stock_details[prod_id]["quantity"]) - quantity

stock = json.dumps(stock_details)    
    
file = open("stock.json", "w")
file.write(stock)
file.close() 

#To create sales.json
file = open("sales.json", "r")
sale = file.read()
file.close()

#Dictionary that have all sales details
sales_report = {}

sales_report = json.loads(sale)

#Writing sales details into JSON
for i in range(len(cart)):
    x = cart[i]
    prod_id,quantity = x.split("#")
    y = stock_details[prod_id]
    #To generate Transaction ID based on time
    now_time = time.ctime()
    year = now_time[-4:]
    day = now_time[4:10]
    date = day.replace(" ","")
    clock = now_time[11:19]
    #Transaction ID format example: 2021sep5#21:28#1001  - YYYY + Month&Date + # + time + # + Product ID
    transaction_id = year + date +"#"+ clock +"#"+ prod_id   #this is the generated transaction_id for each purchase
    if transaction_id in sales_report:
        transaction_id = year + date +"#"+ clock +"#"+ prod_id +"#"+ str(i)
    sales_report[transaction_id] = {"product ID" : prod_id, "name" : y["name"], "quantity" : quantity, "total price" :str(int(quantity)*float(y["price"])) }
    
sale = json.dumps(sales_report)

file = open("sales.json", "w")
file.write(sale)
file.close()

#BY - Nitheesh Kumaar M V