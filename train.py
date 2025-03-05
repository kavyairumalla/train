import random

# Train data: [Train Name, [Seats in Sleeper, Seats in AC, Base Fare (Sleeper), Base Fare (AC)]]
trains = {
    "Rajdhani Express": [50, 30, 500, 1000],
    "Shatabdi Express": [40, 20, 600, 1200],
    "Duronto Express": [60, 25, 550, 1100],
}

# Passenger details (PNR -> [Name, Train, Class, Fare])
bookings = {}

def check_availability(train_name, travel_class):
    if train_name in trains:
        index = 0 if travel_class.lower() == "sleeper" else 1
        return trains[train_name][index]
    return -1  # Train not found

def book_ticket(name, train_name, travel_class):
    if train_name not in trains:
        print("Invalid train name.")
        return
    
    index = 0 if travel_class.lower() == "sleeper" else 1
    if trains[train_name][index] > 0:
        trains[train_name][index] -= 1  # Reduce seat count
        fare = trains[train_name][2 + index]  # Get fare based on class
        pnr = f"PNR{random.randint(10000, 99999)}"
        bookings[pnr] = [name, train_name, travel_class, fare]
        print(f"Ticket booked successfully! PNR: {pnr}")
    else:
        print("No seats available in the selected class.")

def check_pnr(pnr):
    if pnr in bookings:
        print("Booking Details:")
        print(f"Passenger: {bookings[pnr][0]}")
        print(f"Train: {bookings[pnr][1]}")
        print(f"Class: {bookings[pnr][2]}")
        print(f"Fare: ₹{bookings[pnr][3]}")
    else:
        print("Invalid PNR.")

# Example usage:
while True:
    print("\nRailway Ticket Booking System")
    print("1. Check Seat Availability")
    print("2. Book a Ticket")
    print("3. Check PNR Status")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        train_name = input("Enter train name: ")
        travel_class = input("Enter class (Sleeper/AC): ")
        available_seats = check_availability(train_name, travel_class)
        if available_seats >= 0:
            print(f"Seats available in {train_name} ({travel_class}): {available_seats}")
        else:
            print("Invalid train name or class.")
    
    elif choice == "2":
        name = input("Enter passenger name: ")
        train_name = input("Enter train name: ")
        travel_class = input("Enter class (Sleeper/AC): ")
        book_ticket(name, train_name, travel_class)
    
    elif choice == "3":
        pnr = input("Enter PNR number: ")
        check_pnr(pnr)
    
    elif choice == "4":
        print("Thank you for using the Railway Booking System!")
        break
    
    else:
        print("Invalid choice! Please try again.")

