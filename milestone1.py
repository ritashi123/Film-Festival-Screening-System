
# MILESTONE 1: ANALYSE ONE FILM SCREENING

# Taking input from user
film_title = input("Enter film title: ")
genre = input("Enter genre: ")

capacity = int(input("Enter theatre capacity: "))
tickets_sold = int(input("Enter tickets sold: "))
ticket_price = float(input("Enter ticket price: "))
duration = int(input("Enter duration in minutes: "))

# Display data types
print("\n--- DATA TYPES ---")
print("Tickets Sold:", type(tickets_sold))
print("Ticket Price:", type(ticket_price))

# Validate inputs
if capacity <= 0:
    print("Error: Capacity must be greater than zero.")

elif tickets_sold < 0 or tickets_sold > capacity:
    print("Error: Invalid number of tickets sold.")

elif ticket_price < 0 or duration <= 0:
    print("Error: Invalid ticket price or duration.")

else:
    # Calculate statistics
    occupancy = (tickets_sold / capacity) * 100
    vacant_seats = capacity - tickets_sold
    gross_revenue = tickets_sold * ticket_price

    # Convert duration
    hours = duration // 60
    minutes = duration % 60

    # Generate screening code
    screening_code = film_title[:3].upper() + str(duration)[-2:]

    # Display results
    print("\n===== SCREENING REPORT =====")
    print("Film Title:", film_title.title())
    print("Genre:", genre.title())
    print("Theatre Capacity:", capacity)
    print("Tickets Sold:", tickets_sold)
    print("Ticket Price: Rs.", ticket_price)
    print("Occupancy:", round(occupancy, 2), "%")
    print("Vacant Seats:", vacant_seats)
    print("Gross Revenue: Rs.", gross_revenue)
    print("Duration:", hours, "hours", minutes, "minutes")
    print("Screening Code:", screening_code)
