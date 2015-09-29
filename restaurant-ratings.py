# your code goes here
def get_restaurant_ratings(filepath):
    """gets .txt file with restaurants and ratings, prints list of ratings.
    """

    restaurant_ratings = {}
    ratings_log = open(filepath)

    for line in ratings_log:
        line = line.strip()
        # each line in the file is like "taco bell:7"
        restaurant, rating = line.split(":")

        # restaurant_ratings['taco bell'] = 7
        restaurant_ratings[restaurant] = rating

    new_restaurant = str(raw_input("Enter a restaurant name: "))
    new_restaurant = new_restaurant.capitalize()
    new_restaurant_score = raw_input("Enter a restaurant rating (1-10): ")
    count = 0
    while count < 5:
        try:
            new_restaurant_score = int(new_restaurant_score)
            break
        except ValueError:
            print "Ratings must be between 1 and 10."
            new_restaurant_score = raw_input("Enter a restaurant rating (1-10: ")
            count += 1
        if count == 4:
            print "Please try again later."
            return None
    restaurant_ratings[new_restaurant] = new_restaurant_score
    restaurants = sorted(restaurant_ratings.keys())
    # restaurants = ["applebee's", "david's cafe", "zen cafe"]
    for restaurant in restaurants:
        # restaurant = "applebee's" first time
        #                                 "taco bell",   rr['taco bell'] => 3          
        print "{} is rated at {}.".format(restaurant, restaurant_ratings[restaurant])
    ratings_log.close()