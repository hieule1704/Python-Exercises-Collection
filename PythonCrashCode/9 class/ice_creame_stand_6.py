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

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors):
        super().__init__(name, cuisine)
        self.flavors = flavors

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Main
ice_cream_stand = IceCreamStand("Baskin Robbins", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()