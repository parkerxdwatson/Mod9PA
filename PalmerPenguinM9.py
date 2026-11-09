# PalmerPenguinsM9.py
# Benjamin Watson
# 11/8/2026
# Analyze Palmer Penguin observations using classes and objects

import math
from penguin import Penguin

# constants representing the species and count
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"

NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151


# instructor-provided function
# copy and paste into your solution
def read_penguin_row(row_number):
    penguin_row = ""

    # open the CSV file and skip the header row
    with open("PalmerPenguins.csv", "r") as penguin_file:
        penguin_file.readline()

        current_row = 1

        # search for the requested data row
        for row in penguin_file:
            if current_row == row_number:
                penguin_row = row.strip()
                break

            current_row += 1

    # return the requested row as a string
    return penguin_row


# functions for penguin analysis
def calculate_percentage(count, total):
    # return a count as a percentage of a total
    return count / total * 100


def classify_species(percent):
    # return the size category for a species percentage
    if percent < 25:
        return "small"
    elif (percent >= 25) and (percent < 40):
        return "medium"
    else:
        return "large"


def get_position_description(selected_species, largest_species,
                             smallest_species):
    # return whether a species is the largest, smallest, or middle-sized
    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"


def display_species_statistics(names, counts, percentages):
    # display each species with its count and percentage
    for index, species in enumerate(names):
        print(f"{species}: {counts[index]} "
              f"({percentages[index]:.2f}%)")


def display_penguin_observation(sample_number, species, bill_length,
                                bill_depth, body_mass, sex):
    # display one penguin observation with aligned labels
    print("Sample Penguin Observation")
    print(f"{'Sample Number:':<15}{sample_number}")
    print(f"{'Species:':<15}{species}")
    print(f"{'Bill length:':<15}{bill_length} mm")
    print(f"{'Bill depth:':<15}{bill_depth} mm")
    print(f"{'Body mass:':<15}{body_mass} g")
    print(f"{'Sex:':<15}{sex}")


def main():
    # lists about the penguins
    species_names = [SP_CHINSTRAP, SP_GENTOO, SP_ADELIE]
    species_counts = [NUM_CHINSTRAP, NUM_GENTOO, NUM_ADELIE]

    # calculate dataset statistics
    total_species = len(species_names)
    total_penguins = sum(species_counts)
    average_penguins = total_penguins / total_species
    average_penguins_rounded_up = math.ceil(average_penguins)

    chinstrap_percent = \
        calculate_percentage(species_counts[0], total_penguins)
    gentoo_percent = \
        calculate_percentage(species_counts[1], total_penguins)
    adelie_percent = \
        calculate_percentage(species_counts[2], total_penguins)

    # parallel list of species percentages
    species_percentages = [
        chinstrap_percent,
        gentoo_percent,
        adelie_percent
    ]

    largest_count = max(species_counts)
    smallest_count = min(species_counts)

    largest_index = species_counts.index(largest_count)
    smallest_index = species_counts.index(smallest_count)

    largest_species = species_names[largest_index]
    smallest_species = species_names[smallest_index]

    # output species name with intro text
    print("Introducing the Palmer Penguins:")
    print("\t" + SP_CHINSTRAP + "!")
    print("\t" + SP_GENTOO + "!")
    print("and last but not least...")
    print("\t" + SP_ADELIE + "!")
    print()
    print("There are a total of " +
          str(total_species) +
          " penguin species in this dataset.")
    # more census data about the species
    print("There are a total of", total_penguins, "penguins in the dataset.")

    # more data about the penguins
    print(f"The average number of penguins per species is "
          f"{average_penguins:.1f}.")
    print(f"The average rounded up is {average_penguins_rounded_up} "
          f"penguins.\n")

    # display species statistics
    display_species_statistics(species_names, \
        species_counts, species_percentages)
    print()
    print(f"The species with the most observations is "
          f"{largest_species} with {largest_count} penguins.")
    print(f"The species with the fewest observations is "
          f"{smallest_species} with {smallest_count} penguins.\n")

    # retrieve sample penguin data
    penguin_row = read_penguin_row(1)
    print("Sample dataset row:")
    print(penguin_row)
    print()

    # split the CSV row into individual values
    penguin_data = penguin_row.split(",")

    # convert numeric values
    sample_number = int(penguin_data[0])
    species = penguin_data[1]
    bill_length = float(penguin_data[2])
    bill_depth = float(penguin_data[3])
    body_mass = int(penguin_data[5])
    sex = penguin_data[6]

    # display the penguin observation
    display_penguin_observation(sample_number, species, bill_length,
                                bill_depth, body_mass, sex)
    print()

    # retrieve another sample penguin (a different species)
    penguin_row = read_penguin_row(200)

    # split the CSV row into individual values
    penguin_data = penguin_row.split(",")

    # convert numeric values
    sample_number = int(penguin_data[0])
    species = penguin_data[1]
    bill_length = float(penguin_data[2])
    bill_depth = float(penguin_data[3])
    body_mass = int(penguin_data[5])
    sex = penguin_data[6]

    # display the penguin observation
    display_penguin_observation(sample_number, species, bill_length,
                                bill_depth, body_mass, sex)
    print()

    # create a list of sample row numbers
    sample_rows = [1, 2, 3, 4, 5]

    # create an empty list to store the body masses
    body_masses = []

    # collect body masses from the CSV data
    for row_number in sample_rows:
        # retrieve the CSV row
        penguin_row = read_penguin_row(row_number)

        # split the row into individual values
        penguin_data = penguin_row.split(",")

        # convert the body mass to an integer
        body_mass = int(penguin_data[5])

        # append the body mass to the list
        body_masses.append(body_mass)

    print("\nSample Body Masses")
    print(body_masses)

    # calculate summary statistics
    num_observations = len(body_masses)
    total_body_mass = sum(body_masses)
    smallest_body_mass = min(body_masses)
    largest_body_mass = max(body_masses)
    average_body_mass = total_body_mass / num_observations

    # display the body mass summary
    print("\nBody Mass Summary")
    print(f"Observations: {num_observations}")
    print(f"Total body mass: {total_body_mass} g")
    print(f"Smallest body mass: {smallest_body_mass} g")
    print(f"Largest body mass: {largest_body_mass} g")
    print(f"Average body mass: {average_body_mass:.2f} g")

    # associate species names with observation counts
    species_dictionary = {
        SP_CHINSTRAP: NUM_CHINSTRAP,
        SP_GENTOO: NUM_GENTOO,
        SP_ADELIE: NUM_ADELIE
    }

    # display species counts from the dictionary
    print("\nSpecies Counts Using a Dictionary")
    for species in species_dictionary:
        count = species_dictionary[species]
        print(f"{species}: {count}")

    # create one Penguin object from the first CSV observation
    penguin_row = read_penguin_row(1)
    penguin_data = penguin_row.split(",")

    sample_penguin = Penguin(
        int(penguin_data[0]),
        penguin_data[1],
        int(penguin_data[5])
    )

    # display the object's information
    print("\nPenguin Object Demonstration")
    sample_penguin.display_info()

    # create a list of Penguin objects
    penguin_objects = []

    for row_number in sample_rows:
        # retrieve and split the CSV row
        penguin_row = read_penguin_row(row_number)
        penguin_data = penguin_row.split(",")

        # create a Penguin object
        new_penguin = Penguin(
            int(penguin_data[0]),
            penguin_data[1],
            int(penguin_data[5])
        )

        # append the object to penguin_objects
        penguin_objects.append(new_penguin)

    # display each Penguin object
    print("\nPenguin Objects")
    for penguin in penguin_objects:
        penguin.display_info()

    # calculate body mass statistics using object attributes
    total_object_mass = 0
    for penguin in penguin_objects:
        total_object_mass += penguin.body_mass

    average_object_mass = total_object_mass / len(penguin_objects)

    print("\nObject-Based Body Mass Summary")
    print(f"Observations: {len(penguin_objects)}")
    print(f"Total body mass: {total_object_mass} g")
    print(f"Average body mass: {average_object_mass:.2f} g")
    print()

    # initialize the valid selection counter
    valid_selections = 0

    # prompt the user to select a species
    print("Explore the Palmer Penguins")
    species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")

    # repeatedly prompt the user to explore species
    while species_choice != "Done":

        # validate the species selection
        if species_choice not in species_names:
            print(f"{species_choice} is not one of the species "
                  f"in this dataset.")
        else:
            # update the number of valid selections
            valid_selections += 1

            # determine the selected species
            if species_choice == species_names[0]:
                selected_index = 0
            elif species_choice == species_names[1]:
                selected_index = 1
            else:
                selected_index = 2

            # retrieve the selected species data
            selected_species = species_names[selected_index]
            selected_count = species_counts[selected_index]
            selected_percent = species_percentages[selected_index]

            # classify the selected species
            size_category = classify_species(selected_percent)

            # determine the species position
            position_description = \
                get_position_description(selected_species, \
                largest_species, smallest_species)

            # compare the selected count to the average
            average_position = ("above" if selected_count > average_penguins
                                else "below")

            # output selected species statistics
            print(f"{selected_species} has {selected_count} observations, "
                  f"representing {selected_percent:.2f}% of the dataset.")
            print(f"{selected_species} is classified as a {size_category} "
                  f"species group.")
            print(f"{selected_species} is the {position_description} "
                  f"species group.")
            print(f"Its observation count is {average_position} the dataset "
                  f"average of {average_penguins:.1f}.")

        # ask again so the loop can end when the user enters Done
        species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")

    # display the exploration summary
    print(f"You explored {valid_selections} valid species.")
    print("Exploration complete.")


main()