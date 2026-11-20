
# MILESTONE 3: MODEL SCREENINGS USING OOP

class FestivalScreening:

    # Class variable
    festival_name = "Jammu Film Festival"

    # Constructor
    def __init__(self, screening_id, film_title, genre, capacity, tickets_sold):
        self.screening_id = screening_id
        self.film_title = film_title
        self.genre = genre
        self.capacity = capacity
        self.tickets_sold = tickets_sold
        self.ratings = []

    # Add audience rating
    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Invalid rating! Enter between 1 and 5.")

    # Calculate occupancy
    def occupancy_rate(self):
        return (self.tickets_sold / self.capacity) * 100

    # Calculate average rating
    def average_rating(self):
        if len(self.ratings) == 0:
            return None
        return sum(self.ratings) / len(self.ratings)

    # Calculate ticket revenue
    def ticket_revenue(self, price):
        return self.tickets_sold * price

    # Display screening details
    def __str__(self):
        avg = self.average_rating()

        if avg is None:
            avg = "No ratings available"

        return (
            f"Festival: {self.festival_name}\n"
            f"Screening ID: {self.screening_id}\n"
            f"Film Title: {self.film_title}\n"
            f"Genre: {self.genre}\n"
            f"Occupancy: {self.occupancy_rate():.2f}%\n"
            f"Average Rating: {avg}"
        )


# Create objects
if __name__ == "__main__":

    s1 = FestivalScreening(101, "The Last Signal", "Sci-Fi", 120, 96)
    s2 = FestivalScreening(102, "Dream World", "Fantasy", 100, 75)

    # Add ratings
    s1.add_rating(4)
    s1.add_rating(5)
    s1.add_rating(4.5)

    s2.add_rating(3)
    s2.add_rating(4)
    s2.add_rating(5)

    # Display first screening
    print("===== SCREENING 1 =====")
    print(s1)
    print("Revenue: Rs.", s1.ticket_revenue(150))

    # Display second screening
    print("\n===== SCREENING 2 =====")
    print(s2)
    print("Revenue: Rs.", s2.ticket_revenue(120))

    # Check object type
    print("\nIs s1 a FestivalScreening object?")
    print(isinstance(s1, FestivalScreening))
