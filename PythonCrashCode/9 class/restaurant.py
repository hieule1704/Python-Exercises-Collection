class Restaurant:
    def __init__(self, name, cuisine, number_served=0):
        self.name = name
        self.cuisine = cuisine
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increase_number_served(self, number_served):
        self.number_served += number_served
# Main
# restaurant_1 = Restaurant("The Golden Dragon", "Chinese")
# restaurant_1.describe_restaurant()
# restaurant_1.set_number_served(10)
# restaurant_1.increase_number_served(5)
# print(f"Number served: {restaurant_1.number_served}")