
# MILESTONE 4: BUILD REUSABLE FESTIVAL ANALYTICS

# Import class and functions
from milestone3 import FestivalScreening
from festival_utils import occupancy_metric, rating_metric, discounted_price


# Create screening objects
s1 = FestivalScreening(101, "The Last Signal", "Sci-Fi", 120, 96)
s2 = FestivalScreening(102, "Dream World", "Fantasy", 100, 75)
s3 = FestivalScreening(103, "Dark Night", "Thriller", 150, 120)


# Add audience ratings
s1.add_rating(4)
s1.add_rating(5)

s2.add_rating(3)
s2.add_rating(4)

s3.add_rating(5)
s3.add_rating(4.5)


# Store objects in a list
screenings = [s1, s2, s3]


# Dictionary mapping functions
analytics = {
    "occupancy": occupancy_metric,
    "rating": rating_metric
}


# Ask user to select analytics
choice = input("Enter metric (occupancy/rating): ").lower().strip()


if choice in analytics:
    print("\n===== SELECTED ANALYTICS =====")

    for s in screenings:
        result = analytics[choice](s)
        print(s.film_title, ":", result)

else:
    print("Invalid metric selected!")


# Demonstrate default and keyword arguments
print("\n===== DISCOUNTED PRICE =====")

print("Default 10% discount:", discounted_price(150))
print("20% discount:", discounted_price(150, discount=0.20))


# Sort screenings using lambda
sorted_screenings = sorted(
    screenings,
    key=lambda s: s.average_rating() or 0,
    reverse=True
)


print("\n===== SCREENING RANKING =====")

for s in sorted_screenings:
    print(s.film_title, "- Rating:", s.average_rating())
