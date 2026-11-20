
# MILESTONE 4: REUSABLE FESTIVAL ANALYTICS

# Function to calculate occupancy percentage
def occupancy_metric(screening):
    return (screening.tickets_sold / screening.capacity) * 100


# Function to calculate average rating
def rating_metric(screening):
    return screening.average_rating()


# Function to calculate discounted ticket price
def discounted_price(price, discount=0.10):
    return price - (price * discount)
