# OLUWAFISAYO ADABS 30141541, KAMEEL KASUMU 30141921
import numpy as np  # importing numpy module
import matplotlib.pyplot as plt  # importing matplotlib module
import math as m  # importing math module


class printCountryInfo:
    """
    A class used to create a School object.

        Attributes:
            country_name (str): String that represents the country's name (input given)
            UN_region (str): String that represents the UN region the given coountry is in
            area (str): String that represents the country's size in square kilometers
            pop_ave (int): Integer that represents the calculated average population over the given rannge of years
            total_threatened (int): Integer that represents the calculated total amount of threatened species over the given rannge of years   

    """

    def __init__(self, country_name, UN_region, area, pop_ave, total_threatened):
        self.name = country_name
        self.region = UN_region
        self.area = area
        self.population = pop_ave
        self.threatened = total_threatened

    def print_stats(self):
        """
        A function that prints selected statistics for the inputted country given

        Parameters: None
        Return: None

        """
        print()  # empty print line for visual appeal
        # Statement telling the user that the requested statistics are below
        print(f'These are the requested statistics for {self.name}.')
        # determining field width between values in the table
        table_format = '{name:<31}{region:<13}{area:<26}{population:<22}{threatened:<28}'
        print(table_format.format(name='Country', region='UN Region', area='Size of Country (Sq Km)',
              population='Average Population', threatened='Total Threatened Species'))  # Title for the table
        print('-'*116)  # seperate title from data values in table
        print(table_format.format(name=self.name, region=self.region, area=self.area, population=self.population,
              threatened=self.threatened))  # printing the data values in the table for given countries


def average_pop(country_index, population_data):
    """
    Takes in the index of the inputted country, and the numpy array for the population data for all countries and calculates and returns the average population across the given range of years for the inputted country

    Arguments:
    country_index(int): Integer representing index of the given country 
    population_data(array): Array representing data read in from a CSV file (population data from 2000-2020 for all UN countries)

    Returns:
    Returns the calculated average population for the given country
    """
    country_pop_row = [int(pop) for pop in population_data[country_index, 1:]
                       ]  # list comprehension to turn all values from strings to ints
    # uses numpy.mean to calculate average population for inputted country
    average_population = m.floor(np.mean(country_pop_row))
    return average_population  # returns the average population


def total_threatened(country_index, threatened_data):
    """
    Takes in the index of the inputted country, and the numpy array for the threatened species data for all countries and calculates and returns the total amount of threatened species for the inputted country

    Arguments:
    country_index(int): Integer representing index of the given country 
    threatened_data(array): Array representing data read in from a CSV file (threatened species data for all UN countries)

    Returns:
    Returns the calculated total amount of threatened species for the given country
    """
    threatened_country_row = [int(species) for species in threatened_data[country_index, 1:]
                              ]  # list comprehension to turn all values from strings to ints
    # uses numpy.sum to calculate total amount of threatened species
    threatened_total = np.sum(threatened_country_row)
    return threatened_total  # returns total amount of threatened species


def pop_density(country_index, population_data, country_size):
    """
    Takes in the index of the inputted country, the numpy array for the population data for all countries, and the area (in sq km) of the given country and calculates and returns a list of all the population densities for the inputted country over the given range of years

    Arguments:
    country_index(int): Integer representing index of the given country 
    threatened_data(array): Array representing data read in from a CSV file (threatened species data for all UN countries)
    country_size(int): Integer representing the size of the country in square kilometers

    Returns:
    Returns a list containing all the population densities for the inputted country for the given range of years
    """
    list_country_pop = [int(pop) for pop in population_data[country_index, 1:]
                        ]  # list comprehension to turn all values from strings to ints
    # List comprehension to calculate the population density for each population value
    population_density = [m.floor((pop/country_size))
                          for pop in list_country_pop]
    # returns a list of all the population densities.
    return population_density


def main():

    # reading in a csv file representing the school data for the 2018-2019 school year
    country_data = np.genfromtxt('Country_Data.csv', delimiter=',', dtype=str)
    # reading in a csv file representing the school data for the 2019-2020 school year
    pop_data = np.genfromtxt('Population_Data.csv', delimiter=',', dtype=str)
    # reading in a csv file representing the school data for the 2020-2021 school year
    threatened_species = np.genfromtxt(
        'Threatened_Species.csv', delimiter=',', dtype=str)
    # dictionary mapping each country to an index value
    country_index_dict = dict(zip(country_data[:, 0], list(range(0, 195))))
    # dictionary mapping an index value to each country
    index_reverse_dict = dict(zip(list(range(0, 195)), country_data[:, 0]))

    print('Welcome to UN Database Statistics Program!')  # welcome statement
    print()  # empty print statement for visual appeal
    while True:  # Loop that runs the whole program
        # clear nstructions for user
        print('You will be prompted to enter two countries of your choice that are in the UN. The program will not continue until you have given two valid inputs.')
        # User input that either continues or ends the loop
        user_choice = input(
            'To continue please enter any key and to exit please enter "X": ')
        print()  # empty print statement for visual appeal
        if user_choice != 'X':  # If statement to run the program based on the user's input
            while True:  # Loop that allows the user multiple entries until the country is a valid input
                # User's input asking for a country
                request_country = input(
                    'Please enter the first country: ').strip()
                # If statement to ensure the inputed country is in the dictionary (hence a valid country in the UN)
                if request_country in country_index_dict and request_country != index_reverse_dict[0]:
                    # Variable that stores the user's country as an index number
                    index_req = country_index_dict[request_country]
                    break  # Terminates the loop
                else:  # Else statement if country not found in the dictionary
                    # Print statement that describes why the program did not run and asks the user to enter a valid input
                    print('Country not found! Please enter a country in the UN')
                    True  # Restarts loop given user another chance to enter a valid country

            while True:  # Loop that allows the user multiple entries until the country you want to compare is a valid country in the UN
                # User's input asking for a country
                compare_country = input(
                    'Please enter the second country: ').strip()
                # If statement to ensure the inputed country is in the dictionary (hence a valid country in the UN)
                if compare_country in country_index_dict and compare_country != index_reverse_dict[0]:
                    # Variable that stores the user's country as the index number
                    index_com = country_index_dict[compare_country]
                    break  # Terminates the loop
                else:  # Else statement if country not found in the dictionary
                    # Print statement that describes why the program did not run and asks the user to enter a valid input
                    print('Country not found! Please enter a country in the UN')
                    True  # Restarts loop given user another chance to enter a valid country

            # variable that equals the calculated average population for the first inpuuted country
            calculated_ave_pop1 = average_pop(index_req, pop_data)
            # variable that equals the calculated average population for the second inpuuted country
            calculated_ave_pop2 = average_pop(index_com, pop_data)

            # variable that equals the calculated total amount of threatened species for the first inpuuted country
            calculated_threatened1 = total_threatened(
                index_req, threatened_species)
            # variable that equals the calculated total amount of threatened species for the second inpuuted country
            calculated_threatened2 = total_threatened(
                index_com, threatened_species)

            # creating an instance of the printCountryInfo class for the first inputted country
            asked_country_stats1 = printCountryInfo(
                request_country, country_data[index_req][1], country_data[index_req][3], calculated_ave_pop1, calculated_threatened1)
            # creating an instance of the printCountryInfo class for the second inputted country
            asked_country_stats2 = printCountryInfo(
                compare_country, country_data[index_com][1], country_data[index_com][3], calculated_ave_pop2, calculated_threatened2)

            # printing out the statistics for the first inputted country using the printCountryInfo class's instance method
            asked_country_stats1.print_stats()
            # printing out the statistics for the second inputted country using the printCountryInfo class's instance method
            asked_country_stats2.print_stats()
            print()  # empty print statement for visual appeal

            # variable that equals the list of population densities for the first inputted country
            pop_density_list1 = pop_density(
                index_req, pop_data, int(country_data[index_req][3]))
            # converting the list to an array so numpy max method can be used
            pop_density_array1 = np.array(pop_density_list1)
            # getting the maximum value in the population densities and setting that value equal to a variable
            max1 = pop_density_array1.max()
            # printing out a statisitc stating the highest population density value for the first inpuuted country
            print(
                f'The highest population density in the given range of years for {request_country} was {max1} people per sq km.')

            # variable that equals the list of population densities for the second inputted country
            pop_density_list2 = pop_density(
                index_com, pop_data, int(country_data[index_com][3]))
            # converting the list to an array so numpy max method can be used
            pop_density_array2 = np.array(pop_density_list2)
            # getting the maximum value in the population densities and setting that value equal to a variable
            max2 = pop_density_array2.max()
            # printing out a statisitc stating the highest population density value for the second inpuuted country
            print(
                f'The highest population density in the given range of years for {compare_country} was {max2} people per sq km.')

            print()  # empty print statement for visual appeal

            # List of years based on the headers in the array
            years = pop_data[0, 1:]
            # List comprehension to obtain a list that turns all the population values for the first inputted country as intergers
            population_years1 = [int(a) for a in pop_data[index_req, 1:]]
            # List comprehension to obtain a list that turns all the population values for the second inputted country as intergers
            population_years2 = [int(a) for a in pop_data[index_com, 1:]]

            # Plots the population by year with a red line
            plt.plot(years, population_years1, c='red', label=request_country)
            # Plots the population by year with a purple line
            plt.plot(years, population_years2,
                     c='purple', label=compare_country)
            # Ensures only the years from the list are ploted with no spaces and prints the x-axis labels in an almost vertical format
            plt.xticks(years, rotation=75)
            # Provides the title of the graph based on the inputted countries
            plt.title(
                f'Comparison of Population by Year for {request_country} and {compare_country}')
            plt.xlabel('Years')  # Labels the x-axis
            plt.ylabel('Number of People')  # Labels the y-axis
            # Moves the x-axis labels and scale up so it can be seen on the screen
            plt.subplots_adjust(bottom=0.20)
            plt.legend(shadow=True)  # shows legend for the graph

            fig, sub = plt.subplots()  # Figure module that allows for subplot image
            # Defines the title of the graph based the inputted countries
            fig.suptitle(
                f"Comparison between {request_country}'s and {compare_country}'s Threatened Species")
            # List of species name base on the headers in the array
            species_names = threatened_species[0, 1:]
            numbers = list(range(1, 5))  # List that counts up to 4
            # Width calculation that determines the size of the bar
            width = np.min(np.diff(numbers))/5
            # List comprehension to obtain a list that turns all the threatened species data values for the first inputted country as intergers
            species = [int(b) for b in threatened_species[index_req, 1:]]
            # List comprehension to obtain a list that turns all the threatened species data values for the second inputted country as intergers
            species_two = [int(c) for c in threatened_species[index_com, 1:]]
            # Plots a bar graph of the first inputted country with the colour orange and labels the bar. The x-axis is subtracted by the width to ensure that the bar graph is side by side
            sub.bar(numbers-width, species, width, color='orange',
                    align='edge', label=request_country)
            # Plots a bar graph of the second inpuuted country with the colour blue and labels the bar.
            sub.bar(numbers, species_two, width, color='blue',
                    align='edge', label=compare_country)
            # Ensures only the numbers from the given list are ploted and changes the scale values from numbers to species type
            plt.xticks(numbers, species_names)
            plt.legend(shadow=True)  # Shows the legend for the graph
            sub.set_xlabel('Species Type')  # Labels the x-axis
            sub.set_ylabel('Number of Threatened Species')  # Labels the y-axis

            fig, sub_2 = plt.subplots()  # Figure module that allows for subplot image
            # plots the population density for the first inputted country by year with a green line and also labels the line
            sub_2.plot(years, pop_density_list1, 'go-', label=request_country)
            # plots the population density for the second inputted country by year with a magenta line and also labels the line
            sub_2.plot(years, pop_density_list2, 'mo-', label=compare_country)
            # Ensures only the years from the list are ploted with no spaces and prints the x-axis labels in an almost vertical format
            plt.xticks(years, rotation=75)
            # Title for the graph based on the inputted countries
            plt.title(
                f'Comparison of Population Density by Year for {request_country} and {compare_country}')
            sub_2.set_xlabel('Years')  # Labels the x-axis
            # Labels the y-axis
            sub_2.set_ylabel('Number of People per Square Kilometer')
            # Moves the x-axis labels and scale up so it can be seen on the screen
            plt.subplots_adjust(bottom=0.20)
            plt.legend(shadow=True)  # shows the legend for the graph

            plt.show()  # Draws all three graphs

        else:  # Else statement that breaks the loop if the user inputed 'X'
            # Nice print statement that thanks the user
            print('Thank you for exploring the UN countries! Bye Now!!')
            break  # Terminates the loop


if __name__ == '__main__':
    main()
