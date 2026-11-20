
# MILESTONE 2: MANAGE A DAY OF SCREENINGS

films = {
    "The Last Signal": {"genre": "Sci-Fi", "capacity": 120, "price": 150},
    "Dream World": {"genre": "Fantasy", "capacity": 100, "price": 120},
    "Dark Night": {"genre": "Thriller", "capacity": 150, "price": 180},
    "Love Story": {"genre": "Romance", "capacity": 80, "price": 100}
}

screenings = []
genres = set()

while True:
    title = input("\nEnter film title (DONE to stop): ").strip()

    if title.upper() == "DONE":
        break

    film_key = next(
        (name for name in films if name.lower() == title.lower()),
        None
    )

    if film_key is None:
        print("Error: Unknown film!")
        continue

    try:
        sold = int(input("Enter tickets sold: "))
        rating = float(input("Enter audience rating (1-5): "))

        capacity = films[film_key]["capacity"]

        if sold < 0 or sold > capacity:
            print("Invalid sold-seat count!")
            continue

        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5!")
            continue

        record = {
            "title": film_key,
            "genre": films[film_key]["genre"],
            "capacity": capacity,
            "tickets_sold": sold,
            "price": films[film_key]["price"],
            "rating": rating
        }

        screenings.append(record)
        genres.add(record["genre"])

        print("Screening added successfully!")

    except ValueError:
        print("Error: Please enter valid numeric values.")
        continue

print("\n===== SCREENING DETAILS =====")

highest = None

for s in screenings:
    occupancy = (s["tickets_sold"] / s["capacity"]) * 100

    if occupancy < 50:
        category = "LOW"
    elif occupancy < 80:
        category = "GOOD"
    elif occupancy < 100:
        category = "HIGH"
    else:
        category = "FULL"

    print("\nFilm:", s["title"])
    print("Genre:", s["genre"])
    print("Occupancy:", round(occupancy, 2), "%")
    print("Category:", category)
    print("Rating:", s["rating"])

    if highest is None or occupancy > highest[1]:
        highest = (s["title"], occupancy)

print("\n===== UNIQUE GENRES =====")
print(genres)

if highest is not None:
    print("\n===== HIGHEST OCCUPANCY =====")
    print("Film:", highest[0])
    print("Occupancy:", round(highest[1], 2), "%")
else:
    print("No valid screenings available.")
