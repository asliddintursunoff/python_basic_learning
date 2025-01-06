import art

print(art.logo)
customers = {}
is_end = True
highest_price = 0
holder = ""
while is_end:
    name = input("Enter your name: ")
    price = int(input("Enter your price: $"))
    customers[name] = price
    if highest_price < customers[name]:
        highest_price = customers[name]
        holder = name
    choice = input("if there is another customer 'YES' , else 'NO': ")
    if choice == "NO":
        print (f"It sold to MR. or MS. {holder} for {highest_price} dollars.")
        print("Thank you for your auction")
        is_end = False




