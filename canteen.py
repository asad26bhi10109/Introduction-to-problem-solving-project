# VIT Bhopal Canteen Billing System
def show_menu():
    print("\n--- Canteen Menu ---")
    print("1. Masala Dosa - Rs.120")
    print("2. Veg sandwich - Rs.60")
    print("3. coffee - Rs.30")
    print("4. Finish order")

def menu():
    total = 0
    print("Welcome to the VIT Bhopal Canteen")
    name = input("Enter your name:")
    
    while True:
        show_menu()
        choice = input("Choose an option:")

        if choice =="4":
            break
        elif choice =="1":
            item ="Masala Dosa"
            price =120
        elif choice == "2":
            item ="Veg sandwich"
            price =60
        elif choice == "3":
            item ="coffee"
            price =30
        else:
            print("Invalid choice")
            continue

        quantity = int(input("Enter quantity: "))
        cost = price * quantity
        total = total + cost
        print(quantity, item, "added. Cost:Rs.",cost)

    print("\n--- Bill ---")
    print("Student name:", name)
    print("Total amount: Rs.", total)
    print("Thank you for visiting the canteen!")

menu()
