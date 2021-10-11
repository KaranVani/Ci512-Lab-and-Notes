class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print (self.name, self.cuisine)


Object1 = Restaurant("Pizza Hut", "Pizza")
Object1.describe_restaurant()
Object2 = Restaurant("Maccies", "Mcdonalds")
Object2.describe_restaurant()
