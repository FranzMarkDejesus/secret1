from datetime import datetime
from validate_email import validate_email
from tabulate import tabulate

dataCars = [["Toyota Vios MT", '3,285.00', '3,875.00'], 
        ["Toyota Altis AT", '4,040.00', '4,650.00'],
        ["Toyota Camry", '4,830.00', '5,465.00'], 
        ["Toyota Innova", '4,430.00', '4,705.00'],
        ["Toyota Grandia", '5,550.00', '6,200.00']]

coupons_queue = [
    {"code": "coupon1", "expiration": "9/11/2024"},
    {"code": "coupon2", "expiration": "9/25/2024"},
    {"code": "coupon3", "expiration": "10/2/2024"},
    {"code": "coupon4", "expiration": "10/21/2024"},
    {"code": "coupon5", "expiration": "10/28/2024"}
]

savedRentals = []



def input_credentials():
    name = input('Full Name: ')
    address = input('Address: ')
    e_address = input_credentials_email()
    province = input_credentials_province()
    return name, address, e_address, province.upper()

def input_credentials_email():
    while True:
        e_address = input('Email Address: ')
        if validate_email(e_address):
            return e_address
        print("Invalid email address. Please try again.\n")
        
def input_credentials_province():
    while True:
        province = input("Province (Pampanga/Tarlac/Zambales/Bataan): ")
        if province.upper() in ['PAMPANGA', 'TARLAC', 'ZAMBALES', 'BATAAN']:
            return province.upper()
        print("Invalid province. Please try again.\n")

def choose_car():
    while True:
        chosenUnit = input("Choose a Unit (Enter the car model name): ")
        for car in dataCars:
            if car[0].lower() == chosenUnit.lower():
                print("\nYou have chosen:", car[0])
                print("\nSelf-Drive (24hrs/d) Price: ₱", car[1])
                print("Chauffeur Drive (10hrs/d) Price: ₱", car[2])
                
                # Ask the user to choose the type of service
                while True:
                    serviceType = input("\nPreferred Type of Service: (S - 'Self-Driven'/ C - 'Chauffeur') - ")
                    if serviceType.upper() in ['S', 'C']:
                        if serviceType.upper() == 'S':
                            price = float(car[1].replace(',', '').replace('₱', ''))
                            return car, "Self-Driven", float(price)
                        else:
                            price = float(car[2].replace(',', '').replace('₱', ''))
                            return car, "Chauffeur", float(price)
                    else:
                        print("Invalid input. Please type within the list: [S|C].\n")
                break
        print("Invalid choice. Please enter a valid car model name.\n")

def input_dateOfPickUp():
    while True:
        dateInput = input("Pick-up Date (MM/DD/YYYY): ")
        try:
            datePickUp = datetime.strptime(dateInput, '%m/%d/%Y')
            if datePickUp > datetime.today():
                return dateInput
            print("Date must be in the future.\n")
        except ValueError:
            print("Invalid date format. Please try again.\n")

def price_per_day(price):
    days_rental = int(input("How many days will you rent this vehicle? "))
    total_price = days_rental * price
    return days_rental, total_price






def carsList():
    print(tabulate(dataCars, headers = ["Model", "Self-Drive (24hrs/d) [₱]", "Chauffeur Drive (10hrs/d) [₱]"]))

def addCar():
    if len(dataCars) >= 10:
        print("Cannot add more cars. Maximum limit of 10 cars reached.")
        return
    model = input("Enter the car model: ")
    self_drive_price = input("Enter the self-drive price (24hrs/d): ₱")
    chauffeur_drive_price = input("Enter the chauffeur drive price (10hrs/d): ₱")
    dataCars.append([model, self_drive_price, chauffeur_drive_price])
    print(f"Car '{model}' added successfully!")
    
def remCar():
    global dataCars
    if len(dataCars) <= 1:
        print("Cannot remove any more cars. Must have at least one.")
        return
    
    model = input("Enter the car model to remove: ")
    for car in dataCars:
        if car[0].lower() == model.lower():
            dataCars.remove(car)
            print(f"Car '{model}' removed successfully!")
            return
    print(f"Car '{model}' not found.")





def addCoupon():
    while True:
        try:
            coupon_code = input("Enter the coupon code: ")
            while True:
                try:
                    expiration_date_input = input("Enter the expiration date (MM/DD/YYYY): ")
                    expiration_date = datetime.strptime(expiration_date_input, '%m/%d/%Y')
                    if expiration_date <= datetime.today():
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("Invalid date format or date is not applicable!\n")
            coupons_queue.append({"code": coupon_code, "expiration": expiration_date_input})
            print(f"Coupon '{coupon_code}' added successfully!")
            break
        except Exception as e:
            print("An error occurred: ", str(e))
            
def viewCoupons():
    print("\nAll Coupons:")
    for coupon in coupons_queue:
        print(f"Code: {coupon['code']}, Expiration: {coupon['expiration']}")
        
def remCoupon():
    if not coupons_queue:
        print("No coupons to remove.")
        return
    
    while True:
        try:
            num_to_remove = int(input("Remove codes that are already expired. How many? "))
            if num_to_remove <= 0:
                print("Please enter a positive number.")
                continue
            if num_to_remove > len(coupons_queue):
                print(f"Cannot remove {num_to_remove} coupons. Only {len(coupons_queue)} available.\n")
                continue
            
            for _ in range(num_to_remove):
                coupon = coupons_queue.pop(0)
                print(f"Coupon '{coupon['code']}' removed successfully!")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")






def viewSavedRentals():
    if savedRentals:
        print("\nList of Saved Rentals:")
        for index, rental in enumerate(savedRentals, start=1):
            print(f"{index}. Name: {rental['name']}, Car Model: {rental['car_model']}, "
                  f"Service Type: {rental['service_type']}, "
                  f"Pick-Up Date: {rental['pick_up_date']}, "
                  f"Days Rental: {rental['days_rental']}, "
                  f"Total Price: ₱{rental['total_price']:,.2f}")
    else:
        print("No rental records found.")






def userMenu():
    print("\n- User Menu -")
    print("1. Rent a Car")
    print("2. View Available Cars")
    print("3. View Available Coupons")
    print("4. Exit")

def devMenu():
    print("\n- Developer Menu -")
    print("1. View List of Rental Orders")
    print("2. Add Vehicles")
    print("3. Remove Vehicles")
    print("4. Add Coupons")
    print("5. Remove Coupons")
    print("6. Exit")






while True:
    role = input("Are you a user or a developer? (Enter 'U' or 'D'. Type 'exit' to quit.): ").strip().upper()

    if role == 'U':
        while True:
            userMenu()
            choice = input("\nPlease enter your choice (1-4): ")
            
            if choice == '1':
                print("\nRenting a car...\n")
                name, address, e_address, province = input_credentials()
                print("\n")
                carsList()
                print()
                car_info, service_type, price = choose_car()
                datePickUp = input_dateOfPickUp()
                days_rental, total_price = price_per_day(price)
                print(f"\nTotal rental price for {days_rental} days: ₱{total_price:,.2f}")
                print("Saving info . . .")
                print()
                
                rental_record = {
                "name": name,
                "address": address,
                "email": e_address,
                "province": province,
                "car_model": car_info[0],
                "service_type": service_type,
                "pick_up_date": datePickUp,
                "days_rental": days_rental,
                "total_price": total_price
                }

                savedRentals.append(rental_record)
                
                
            elif choice == '2':
                print("\nViewing available cars...\n")
                carsList()
            elif choice == '3':
                print("\nViewing available coupons...\n")
                viewCoupons()
            elif choice == '4':
                print("Exiting the system. Goodbye!\n")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    elif role == 'D':
        while True:
            devMenu()
            choice = input("\nPlease enter your choice (1-6): ")
            
            if choice == '1':
                print("Viewing list of rental orders...")
                viewSavedRentals()
                print()
            elif choice == '2':
                print("\nAdding a vehicle...\n")
                addCar()
            elif choice == '3':
                print("\nRemoving a vehicle...\n")
                remCar()
            elif choice == '4':
                print("\nAdding a coupon...\n")
                addCoupon()
            elif choice == '5':
                print("\nRemoving a coupon...")
                viewCoupons()
                print()
                remCoupon()
            elif choice == '6':
                print("Exiting the system. Goodbye!\n")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    elif role == 'EXIT':
        break
    else:
        print("Invalid role. Please restart the program and enter either 'U' or 'D'.\n")

