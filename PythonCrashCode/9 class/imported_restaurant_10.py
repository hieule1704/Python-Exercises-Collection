from restaurant import Restaurant

restaurant_1 = Restaurant("The Golden Dragon", "Chinese")
restaurant_1.describe_restaurant()
restaurant_1.set_number_served(10)
print(f"Number served: {restaurant_1.number_served}")