
import random

print("====================================")
print("     CLOUD-BASED BUS PASS SYSTEM")
print("====================================")

bookings = []

while True:
    print("\n1. Book Bus Pass")
    print("2. View All Bookings")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        name = input("Enter passenger name: ")
        route = input("Enter bus route: ")

        print("\nSelect Pass Type")
        print("1. Daily Pass - Rs. 50")
        print("2. Weekly Pass - Rs. 250")
        print("3. Monthly Pass - Rs. 800")

        choice = input("Enter pass choice: ")

        if choice == "1":
            pass_type = "Daily"
            price = 50
        elif choice == "2":
            pass_type = "Weekly"
            price = 250
        elif choice == "3":
            pass_type = "Monthly"
            price = 800
        else:
            print("Invalid pass choice!")
            continue

        booking_id = random.randint(10000, 99999)

        booking = {
            "Booking ID": booking_id,
            "Name": name,
            "Route": route,
            "Pass Type": pass_type,
            "Price": price
        }

        bookings.append(booking)

        print("\n----- BOOKING SUCCESSFUL -----")
        print("Passenger Name:", name)
        print("Bus Route:", route)
        print("Pass Type:", pass_type)
        print("Ticket Price: Rs.", price)
        print("Booking ID:", booking_id)
        print("Thank you for booking!")

    elif option == "2":
        if len(bookings) == 0:
            print("No bookings available.")
        else:
            print("\n----- ALL BUS BOOKINGS -----")

            for booking in bookings:
                print("----------------------------")
                print("Booking ID:", booking["Booking ID"])
                print("Passenger:", booking["Name"])
                print("Route:", booking["Route"])
                print("Pass Type:", booking["Pass Type"])
                print("Price: Rs.", booking["Price"])

    elif option == "3":
        print("Thank you for using Bus Pass System!")
        break

    else:
        print("Invalid choice! Please try again.")
