# penguin.py
# Benjamin Watson
# 11/8/2026
# Class representing a penguin

class Penguin:
    def __init__(self, sample_number, species, body_mass):
        # store the attributes of one penguin observation
        self.sample_number = sample_number
        self.species = species
        self.body_mass = body_mass

    def display_info(self):
        # display the sample number, species, and body mass
        print(f"Sample Number: {self.sample_number}")
        print(f"Species: {self.species}")
        print(f"Body Mass: {self.body_mass} g")
