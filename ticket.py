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
    fares = {50, 60, 70, 80, 90, 100}
    if locationdistance >= 10:
        print("your fare is: ", "$",50)
    elif locationdistance >= 20:
        print("your fare is: ", "$",60)
    elif locationdistance >= 30:
        print("your fare is: ", "$",70)
    elif locationdistance >= 40:
        print("your fare is: ", "$",80)
    elif locationdistance >= 50:
        print("your fare is: ", "$",90)
    elif locationdistance > 60:
        print("your fare is: ", "$",100)
    else:
        print("sorry your fare is insufficient you can't be on this trip 😭👺")
       
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
Fare             : $ {fares}
=======================
""")
    print(f"Driver {assigned_driver} has been assigned to you save journey!!!")
    break  # Exit loop on successful run

    