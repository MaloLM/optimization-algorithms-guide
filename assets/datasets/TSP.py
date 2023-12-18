import math
import random
import matplotlib.pyplot as plt

CITIES = {
    "Gotham City": (34, 52),
    "Metropolis": (67, 83),
    "Central City": (29, 56),
    "Star City": (45, 68),
    "Atlantis": (88, 25),
    "Asgard": (77, 94),
    "Vice City": (51, 13),
    "Rapture": (63, 89),
    "Hogsmeade": (20, 75),
    "Diagon Alley": (11, 65),
    "Rivendell": (43, 67),
    "Minas Tirith": (58, 14),
    "Ankh-Morpork": (33, 45),
    "Neverwinter": (39, 59),
    "Whiterun": (85, 47),
    "Solitude": (74, 63),
    "Megaton": (54, 99),
    "Raccoon City": (32, 18),
    "Silent Hill": (62, 38),
    "Hill Valley": (92, 41),
    "Mos Eisley": (16, 82),
    "Coruscant": (29, 10),
    "Gallifrey": (99, 51),
    "Vulcan": (84, 22),
    "Pandora": (47, 64),
    "Lilliput": (3, 77),
    "Westworld": (78, 56),
    "The Shire": (19, 90),
    "Mordor": (60, 34),
    "Gondor": (81, 12),
    "Theed": (42, 28),
    "Cloud City": (91, 73),
    "Bespin": (26, 85),
    "Alderaan": (14, 62),
    "Krypton": (79, 30),
    "Eternia": (65, 9),
    "Castle Rock": (10, 55),
    "Springfield": (35, 21),
    "Quahog": (53, 11),
    "South Park": (23, 44),
    "Bikini Bottom": (31, 70),
    "Bedrock": (48, 2),
    "Elbonia": (95, 87),
    "Zion": (6, 26),
    "New New York": (76, 53),
    "Old New York": (68, 37),
    "The Grid": (82, 69),
    "Zootopia": (59, 49),
    "Emerald City": (17, 92),
    "Pleasantville": (88, 4),
    "Cabot Cove": (71, 24),
    "Stars Hollow": (50, 78),
    "Twin Peaks": (45, 96),
    "Black Mesa": (30, 66),
    "City 17": (27, 60),
    "Inkopolis": (73, 8),
    "Los Santos": (97, 31),
    "Liberty City": (80, 36),
    "San Fierro": (64, 54),
    "Las Venturas": (44, 39),
    "Oakvale": (5, 93),
    "Bowerstone": (52, 20),
    "Riverwood": (69, 57),
    "Falkreath": (40, 80),
    "Vault 101": (75, 6),
    "Vault 111": (98, 61),
    "Narnia": (12, 72),
    "Cyrodiil": (86, 43),
    "Skyloft": (55, 15),
    "Kakariko Village": (22, 81),
    "City of Tears": (7, 88),
    "Hallownest": (70, 33),
    "Bright Moon": (83, 1),
    "Etheria": (37, 58),
    "Mystara": (49, 76),
    "Terminus": (15, 46),
    "Luskan": (61, 29),
    "Baldur's Gate": (9, 67),
    "Sigil": (87, 40),
    "Waterdeep": (24, 95),
    "Undercity": (8, 71),
    "Stormwind": (90, 23),
    "Orgrimmar": (56, 17),
    "Thunder Bluff": (38, 79),
    "Silvermoon City": (66, 50),
    "Darnassus": (100, 32),
    "Ironforge": (72, 19),
    "Exodar": (25, 91),
}

class TravellingSalesman:
    """
    A class representing a Travelling Salesman Problem (TSP) with a given number of cities.

    Attributes:
        cities (list): A list of tuples containing city names and their coordinates.
        distances (dict): A dictionary holding the precomputed distances between each pair of cities.

    Methods:
        calculate_distances(): Computes the distances between each pair of cities.
        distance(point1, point2): Calculates the Euclidean distance between two points.
        get_distance(city1, city2): Retrieves the distance between two cities.
        set_starting_point(city_name): Sets a city as the starting point for the TSP route.
        draw_path(path): Draws the TSP path on a plot.
    """
    def __init__(self, nb_cities, seed=None) -> None:
        """
        Initializes the TravellingSalesman class with a specified number of cities.

        Parameters:
        nb_cities (int): The number of cities to include in the TSP.
        seed (int, optional): A seed value for random number generation.

        Raises:
        ValueError: If the number of cities requested exceeds the available unique cities.
        """
        self.cities = []

        # Set the random seed if provided
        if seed is not None:
            random.seed(seed)

        if nb_cities > len(CITIES):
            raise ValueError("Number of cities requested exceeds available unique cities.")

        self.cities = random.sample(list(CITIES.items()), nb_cities)
        self.distances = self.calculate_distances()

    def calculate_distances(self):
        """
        Calculates the Euclidean distances between each pair of cities.

        Returns:
        dict: A dictionary with city pairs as keys and their distances as values.
        """
        distances = {}
        for i, (city1, (x1, y1)) in enumerate(self.cities):
            for j, (city2, (x2, y2)) in enumerate(self.cities):
                if city1 != city2:
                    distances[(city1, city2)] = self.distance((x1, y1), (x2, y2))
        return distances

    def distance(self, point1, point2):
        """
        Calculates the Euclidean distance between two points.

        Parameters:
        point1 (tuple): The (x, y) coordinates of the first point.
        point2 (tuple): The (x, y) coordinates of the second point.

        Returns:
        float: The Euclidean distance between the two points.
        """
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
    def get_distance(self, city1, city2):
        """
        Retrieves the distance between two cities, considering the distance is symmetric.

        Parameters:
        city1 (str): The name of the first city.
        city2 (str): The name of the second city.

        Returns:
        float: The distance between the two cities.
        """
        # Return the distance, handling the case where the city pair might be reversed
        
        return self.distances.get((city1, city2)) or self.distances.get((city2, city1))

    def set_starting_point(self, city_name):
        """
        Set the starting point of the TSP route by moving the specified city to the beginning of the cities list.

        Parameters:
        city_name (str): The name of the city to be set as the starting point.

        Raises:
        ValueError: If the specified city is not found in the list of cities.
        """
        # Find the index of the city
        city_index = next((index for index, city in enumerate(self.cities) if city[0] == city_name), None)

        # Raise an error if the city is not found
        if city_index is None:
            raise ValueError(f"City '{city_name}' not found in the list of cities.")

        # Move the city to the beginning of the list
        self.cities.insert(0, self.cities.pop(city_index))


    def draw_path(self, path):
        """
        Draws the TSP route on a 2D plot using matplotlib.

        Parameters:
        path (list of int): A list of city indices representing the order of visitation in the TSP route.
        """
        # Extract x and y coordinates of the path
        x = [self.cities[i][1][0] for i in path]  # Extract x-coordinates
        y = [self.cities[i][1][1] for i in path]  # Extract y-coordinates

        # Compute the total distance of the path
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += self.get_distance(self.cities[path[i]][0], self.cities[path[i + 1]][0])

        # Setup the plot
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'o-', mfc='r')  # Plot the points and lines in red
        plt.plot(x[0], y[0], 'o', mfc='g')  # Color the starting point in green

        # Setting the title with total distance
        plt.title(f"Path Traversed in TSP (Total Distance: {total_distance:.2f} units)")

        # Hide the figure border
        for spine in plt.gca().spines.values():
            spine.set_visible(False)

        # Annotate each city in the path
        for i, city in enumerate(path):
            if i < len(path) - 1:  # Avoid annotating the last city
                annotation_label = f"{self.cities[city][0]} ({i + 1})"
                plt.annotate(annotation_label, (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

        # Display the grid and show the plot
        plt.grid(True)
        plt.show()
