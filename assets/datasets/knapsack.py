import random

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


        

class Kackpack:
    def __init__(self, nb_items):
        self.nb_items = nb_items
        
        if nb_items > len(ITEMS):
            raise ValueError("Number of items requested exceeds available unique items.")

        self.items = random.sample(ITEMS, nb_items)
    
    def get_assets(self):
        return self.items


