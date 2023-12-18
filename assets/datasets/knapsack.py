import random
import matplotlib.pyplot as plt
import numpy as np

ITEMS = [
    {"name": "laptop", "weight": 1.5, "value": 1500},
    {"name": "camera", "weight": 0.5, "value": 800},
    {"name": "headphones", "weight": 0.3, "value": 250},
    {"name": "sunglasses", "weight": 0.1, "value": 100},
    {"name": "book", "weight": 0.4, "value": 20},
    {"name": "journal", "weight": 0.2, "value": 15},
    {"name": "pen", "weight": 0.05, "value": 3},
    {"name": "water bottle", "weight": 0.5, "value": 10},
    {"name": "snack bar", "weight": 0.1, "value": 2},
    {"name": "toothbrush", "weight": 0.05, "value": 4},
    {"name": "charger", "weight": 0.2, "value": 25},
    {"name": "smartphone", "weight": 0.2, "value": 700},
    {"name": "passport", "weight": 0.05, "value": 200},
    {"name": "wallet", "weight": 0.1, "value": 50},
    {"name": "watch", "weight": 0.2, "value": 250},
    {"name": "keys", "weight": 0.1, "value": 5},
    {"name": "shirt", "weight": 0.2, "value": 30},
    {"name": "pants", "weight": 0.5, "value": 50},
    {"name": "jacket", "weight": 1, "value": 100},
    {"name": "socks", "weight": 0.1, "value": 5},
    {"name": "shoes", "weight": 1, "value": 80},
    {"name": "hat", "weight": 0.2, "value": 25},
    {"name": "umbrella", "weight": 0.5, "value": 15},
    {"name": "novel", "weight": 0.3, "value": 10},
    {"name": "glasses case", "weight": 0.1, "value": 15},
    {"name": "travel pillow", "weight": 0.4, "value": 20},
    {"name": "notebook", "weight": 0.3, "value": 12},
    {"name": "sketchpad", "weight": 0.5, "value": 18},
    {"name": "pencil case", "weight": 0.2, "value": 8},
    {"name": "map", "weight": 0.1, "value": 4},
    {"name": "guidebook", "weight": 0.3, "value": 25},
    {"name": "deck of cards", "weight": 0.1, "value": 6},
    {"name": "flashlight", "weight": 0.2, "value": 20},
    {"name": "hand sanitizer", "weight": 0.1, "value": 5},
    {"name": "face mask", "weight": 0.05, "value": 1},
    {"name": "sunglasses case", "weight": 0.1, "value": 10},
    {"name": "travel mug", "weight": 0.3, "value": 25},
    {"name": "earplugs", "weight": 0.01, "value": 3},
    {"name": "sleeping mask", "weight": 0.05, "value": 10},
    {"name": "travel adapter", "weight": 0.2, "value": 40},
    {"name": "tablet", "weight": 0.5, "value": 500},
    {"name": "e-reader", "weight": 0.2, "value": 120},
    {"name": "portable charger", "weight": 0.25, "value": 60},
    {"name": "GPS device", "weight": 0.2, "value": 200},
    {"name": "travel router", "weight": 0.2, "value": 100},
    {"name": "hairbrush", "weight": 0.1, "value": 10},
    {"name": "makeup bag", "weight": 0.4, "value": 50},
    {"name": "moisturizer", "weight": 0.2, "value": 25},
    {"name": "sunscreen", "weight": 0.2, "value": 15},
    {"name": "deodorant", "weight": 0.15, "value": 8},
    {"name": "shaving kit", "weight": 0.3, "value": 35},
    {"name": "perfume", "weight": 0.1, "value": 90},
    {"name": "lip balm", "weight": 0.02, "value": 2},
    {"name": "hand cream", "weight": 0.1, "value": 8},
    {"name": "soap", "weight": 0.1, "value": 3},
    {"name": "shampoo", "weight": 0.3, "value": 10},
    {"name": "conditioner", "weight": 0.3, "value": 10},
    {"name": "towel", "weight": 0.5, "value": 20},
    {"name": "swimsuit", "weight": 0.2, "value": 30},
    {"name": "flip-flops", "weight": 0.3, "value": 20},
    {"name": "beach towel", "weight": 0.7, "value": 35},
    {"name": "snorkel gear", "weight": 1.5, "value": 100},
    {"name": "beach bag", "weight": 0.4, "value": 25},
    {"name": "novelty souvenir", "weight": 0.5, "value": 15},
    {"name": "travel game", "weight": 0.4, "value": 18},
    {"name": "binoculars", "weight": 0.8, "value": 150},
    {"name": "journal", "weight": 0.3, "value": 25},
    {"name": "disposable camera", "weight": 0.2, "value": 30},
    {"name": "memory card", "weight": 0.01, "value": 50},
    {"name": "power bank", "weight": 0.25, "value": 35},
    {"name": "folding chair", "weight": 2.0, "value": 40},
    {"name": "camping stove", "weight": 1.5, "value": 90},
    {"name": "tent", "weight": 4.0, "value": 150},
    {"name": "sleeping bag", "weight": 2.0, "value": 80},
    {"name": "hiking boots", "weight": 1.5, "value": 120},
    {"name": "backpack", "weight": 1.0, "value": 70},
    {"name": "thermal flask", "weight": 0.5, "value": 25},
    {"name": "first aid kit", "weight": 0.5, "value": 35},
    {"name": "pocket knife", "weight": 0.2, "value": 50},
    {"name": "hiking poles", "weight": 0.6, "value": 80},
    {"name": "compass", "weight": 0.1, "value": 20},
    {"name": "camping lamp", "weight": 0.4, "value": 30},
    {"name": "raincoat", "weight": 0.5, "value": 50},
    {"name": "gloves", "weight": 0.1, "value": 25},
    {"name": "scarf", "weight": 0.1, "value": 20},
    {"name": "wool hat", "weight": 0.1, "value": 20},
    {"name": "sweater", "weight": 0.6, "value": 45},
    {"name": "thermal underwear", "weight": 0.3, "value": 30},
    {"name": "leggings", "weight": 0.2, "value": 25},
]


        

class Knapsack:
    """
    A class to represent a knapsack problem.

    Attributes:
        nb_items (int): Number of items to consider in the knapsack problem.
        weight_limit (float): The weight limit of the knapsack.
        solution (list): List of items that are included in the optimal knapsack solution.
        items (list): List of all items available for the knapsack problem.

    Methods:
        show_state(): Prints the total weight and value if all items are taken.
        get_assets(): Returns the list of items available.
        total_weight(): Calculates the total weight of all items.
        total_value(): Calculates the total value of all items.
        plot_cumulative_knapsack_with_value(): Visualizes the knapsack solution.
    """

    def __init__(self, nb_items, seed=None):
        """
        Initializes the Knapsack class with a specified number of items.

        Parameters:
        nb_items (int): The number of items to include in the knapsack problem.
        seed (int, optional): A seed value for random number generation.
        """
        self.nb_items = nb_items
        self.weight_limit = 0
        self.solution = []

        # Set the random seed if provided
        if seed is not None:
            random.seed(seed)

        # Check if the requested number of items exceeds the available unique items
        if nb_items > len(ITEMS):
            print(f"Number of items requested exceeds available unique items.\n Setting to maximum: {len(ITEMS)}")
            self.nb_items = len(ITEMS)

        # Randomly sample items from the available list
        self.items = random.sample(ITEMS, self.nb_items)

    def show_state(self):
        """
        Prints the total weight and value of all items if taken together.
        """
        print(f"Total weight (taking everything): {self.total_weight()} kg \nTotal value (taking everything): {self.total_value()} $")
    
    def get_assets(self):
        """
        Returns the list of all available items.

        Returns:
        list: A list of items available for the knapsack problem.
        """
        return self.items

    def total_weight(self):
        """
        Calculates the total weight of all items.

        Returns:
        float: Total weight of all items.
        """
        return sum(item['weight'] for item in self.items)

    def total_value(self):
        """
        Calculates the total value of all items.

        Returns:
        float: Total value of all items.
        """
        return sum(item['value'] for item in self.items)
    
    
    def plot_cumulative_knapsack_with_value(self):
        """
        Visualizes the knapsack solution using matplotlib.

        This method plots the cumulative weights and total value of items in the solution,
        comparing it to the total possible value and the weight limit.
        """
        total_value = 0
        current_weight = 0
        cumulative_weights = []
        start_points = [0]

        for item in self.solution:
            current_weight += item['weight']
            total_value += item['value']
            start_points.append(current_weight)
            cumulative_weights.append(min(current_weight, self.weight_limit))

        item_names = [f"{item['name']} (Value: {item['value']}, Weight: {item['weight']}kg)" for item in self.solution]
        colors = plt.cm.viridis(np.linspace(0, 1, len(self.solution)))

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [4, 1, 1]})

        for i, item in enumerate(item_names):
            segment_length = self.solution[i]['weight']
            ax1.barh("Knapsack", segment_length, left=start_points[i], color=colors[i], edgecolor='white', label=item)

        total_weight = cumulative_weights[-1] if cumulative_weights else 0

        ax1.set_title(f'Knapsack Solution (Total Weight: {total_weight:.2f} / {self.weight_limit}kg, Total Value: {total_value})')
        ax1.set_xlabel('Cumulative Weight')
        ax1.axvline(x=self.weight_limit, color='red', linestyle='-')

        total_possible_value = self.total_value()
        ax2.barh("Value", total_value, color='green', edgecolor='white')
        ax2.axvline(x=total_possible_value, color='red', linestyle='-')
        ax2.set_title(f'Solution Value vs Total Possible Value (Solution Value: {total_value}, Total Value: {total_possible_value})')
        ax2.set_xlim(0, max(total_value, total_possible_value) * 1.1)

        handles, labels = ax1.get_legend_handles_labels()
        ax3.legend(handles, labels, loc='upper center', ncol=3)
        ax3.axis('off')

        plt.tight_layout()
        plt.show()

