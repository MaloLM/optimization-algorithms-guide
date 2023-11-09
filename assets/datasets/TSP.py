import math
import random

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
    Generates a random TSP problem dataset
    """
    def __init__(self, nb_cities) -> None:
        self.cities = []

        if nb_cities > len(CITIES):
            raise ValueError("Number of cities requested exceeds available unique cities.")

        self.cities = random.sample(list(CITIES.items()), nb_cities)
        self.distances = self.calculate_distances()

    def calculate_distances(self):
        distances = {}
        for i, (city1, (x1, y1)) in enumerate(self.cities):
            for j, (city2, (x2, y2)) in enumerate(self.cities):
                if city1 != city2:
                    distances[(city1, city2)] = self.distance((x1, y1), (x2, y2))
        return distances

    def distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
    def get_distance(self, city1, city2):
        return self.distances.get((city1, city2)) or self.distances.get((city2, city1))
