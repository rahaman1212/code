import random

while True:
    print("Welcome To my simple trip ticket ")

     # Ask user for pickup and destination
    pickup = input("[+] Enter The pickup Location:  ")
    destination = input("[+] Enter The Destination Location:  ")

    drivers = ["Osman", "Ali", "Ahmed", "Hassan", "Fatima", "Aisha"]
    print("Available Drivers: ", drivers)

    # Get distance
    print("Only numbers allowed")
    locationdistance = int(input("[+] Distance from current location to your destination (in km):  "))

    # fare
    fares = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    fare = random.choice(fares)
    print("your fare is: ", "$",fare)
       
    # Assign a driver
    assigned_driver = random.choice(drivers)

    # Log trip info to a text file
    with open("log-file.txt", "a") as f:
        f.write(f"""
THIS IS YOUR TRIP TICKET
=======================
Pickup Location : {pickup}
Destination     : {destination}
Driver          : {assigned_driver}
Distance        : {locationdistance} km
Fare             : $ {fare}
=======================
""")
    print(f"Driver {assigned_driver} has been assigned to you save journey!!!")
    break  # Exit loop on successful run

    