'''Flight Booking System 
A system to search, book, and cancel flight tickets. 
Handle exceptions such as seat not available, invalid passenger details, payment 
failure'''

flights = {
    "AI101": 2,
    "AI202": 1
}

bookings = []

def book_ticket(flight, name, payment):
    try:
        if name == "":
            raise Exception("Invalid passenger details")

        if flights[flight] == 0:
            raise Exception("Seat not available")

        if payment != "paid":
            raise Exception("Payment failure")

        flights[flight] -= 1
        bookings.append((flight, name))

        print("Ticket booked")

    except Exception as e:
        print("Error:", e)


def cancel_ticket(i):
    try:
        flight, name = bookings[i]
        flights[flight] += 1
        print("Ticket cancelled")

    except:
        print("Invalid booking")


book_ticket("AI101", "Riya", "paid")
book_ticket("AI202", "", "paid")
book_ticket("AI202", "Aman", "fail")

cancel_ticket(0)
