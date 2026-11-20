
# MILESTONE 5: PRESERVE SCREENING HISTORY

filename = "screening_records.txt"


# Function to calculate average rating
def average_rating(ratings):
    if len(ratings) == 0:
        return None
    return sum(ratings) / len(ratings)


try:
    # Take screening details
    film_title = input("Enter film title: ")
    genre = input("Enter genre: ")
    capacity = int(input("Enter theatre capacity: "))
    tickets_sold = int(input("Enter tickets sold: "))
    price = float(input("Enter ticket price: "))
    rating = float(input("Enter audience rating (1-5): "))

    # Validate inputs
    if capacity <= 0:
        raise ValueError("Capacity must be greater than zero.")

    if tickets_sold < 0 or tickets_sold > capacity:
        raise ValueError("Invalid tickets sold count.")

    if price < 0:
        raise ValueError("Ticket price cannot be negative.")

    if rating < 1 or rating > 5:
        raise ValueError("Rating must be between 1 and 5.")


except ValueError as e:
    print("Input Error:", e)


else:
    # Calculate statistics
    occupancy = (tickets_sold / capacity) * 100
    revenue = tickets_sold * price

    # Create screening summary
    summary = (
        f"{film_title} | {genre} | "
        f"Capacity: {capacity} | "
        f"Tickets Sold: {tickets_sold} | "
        f"Occupancy: {occupancy:.2f}% | "
        f"Revenue: Rs.{revenue:.2f} | "
        f"Rating: {rating}\n"
    )

    # Read previous history
    try:
        with open(filename, "r") as file:
            print("\n===== PREVIOUS HISTORY =====")
            print(file.read())

    except FileNotFoundError:
        print("\nHistory file not found. A new file will be created.")

    # Append new record
    with open(filename, "a") as file:
        file.write(summary)

    print("Screening record saved successfully!")

    # Display saved history
    with open(filename, "r") as file:
        print("\n===== SAVED SCREENING HISTORY =====")
        content = file.read()
        print(content)

        print("Current file position:", file.tell())

        file.seek(0)
        print("Position after seek(0):", file.tell())


# Demonstrate empty and valid rating lists
print("\n===== RATING DEBUGGING =====")

empty_ratings = []
valid_ratings = [4, 5, 3]

result = average_rating(empty_ratings)

if result is None:
    print("Empty Ratings: No ratings available.")

result = average_rating(valid_ratings)

print("Valid Ratings:", valid_ratings)
print("Average Rating:", result)
