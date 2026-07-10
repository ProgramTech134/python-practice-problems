status = input("Enter your shopping status ").lower()

match status:

    case "pending" :
        print("Your order is currently being processed.")
    case "shipped" :
        print("Your order has been shipped and is on the way.")
    case "Delivered" :
        print("Order received. Thank you!")
    case "cancelled" :
        print("Your order has been cancelled.")
    case _:
        print("Invalid status code! Please enter a correct code.")
