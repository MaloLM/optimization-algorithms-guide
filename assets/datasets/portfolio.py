import random

ASSETS = [
    {"AssetName": "Stark Industries", "Risk": 5.2, "ExpectedReturn": 14.3, "UnitCost": 220},
    {"AssetName": "Wayne Enterprises", "Risk": 6.8, "ExpectedReturn": 12.1, "UnitCost": 250},
    {"AssetName": "LexCorp", "Risk": 4.9, "ExpectedReturn": 20.5, "UnitCost": 180},
    {"AssetName": "Oscorp", "Risk": 7.1, "ExpectedReturn": 15.6, "UnitCost": 210},
    {"AssetName": "Weyland-Yutani", "Risk": 8.3, "ExpectedReturn": 23.4, "UnitCost": 300},
    {"AssetName": "Cyberdyne Systems", "Risk": 9.7, "ExpectedReturn": 19.0, "UnitCost": 290},
    {"AssetName": "Soylent Corp", "Risk": 3.4, "ExpectedReturn": 9.8, "UnitCost": 160},
    {"AssetName": "Bluth Company", "Risk": 2.8, "ExpectedReturn": 4.2, "UnitCost": 140},
    {"AssetName": "Vandelay Industries", "Risk": 6.1, "ExpectedReturn": 18.5, "UnitCost": 240},
    {"AssetName": "Globex Corporation", "Risk": 4.6, "ExpectedReturn": 12.3, "UnitCost": 190},
    {"AssetName": "ACME Corp", "Risk": 7.9, "ExpectedReturn": 21.7, "UnitCost": 280},
    {"AssetName": "Initech", "Risk": 5.6, "ExpectedReturn": 10.5, "UnitCost": 200},
    {"AssetName": "Umbrella Corporation", "Risk": 9.1, "ExpectedReturn": 6.7, "UnitCost": 270},
    {"AssetName": "Hooli", "Risk": 4.3, "ExpectedReturn": 25.1, "UnitCost": 175},
    {"AssetName": "Massive Dynamic", "Risk": 8.6, "ExpectedReturn": 30.2, "UnitCost": 310},
    {"AssetName": "Pied Piper", "Risk": 1.2, "ExpectedReturn": 35.4, "UnitCost": 120},
    {"AssetName": "Sterling Cooper", "Risk": 6.5, "ExpectedReturn": 16.8, "UnitCost": 230},
    {"AssetName": "Dunder Mifflin", "Risk": 3.9, "ExpectedReturn": 5.4, "UnitCost": 150},
    {"AssetName": "Aperture Science", "Risk": 7.3, "ExpectedReturn": 28.8, "UnitCost": 215},
    {"AssetName": "Gekko & Co", "Risk": 6.9, "ExpectedReturn": 17.2, "UnitCost": 260},
    {"AssetName": "Nakatomi Trading Corp", "Risk": 5.5, "ExpectedReturn": 13.2, "UnitCost": 205},
    {"AssetName": "Tyrell Corporation", "Risk": 7.2, "ExpectedReturn": 19.1, "UnitCost": 225},
    {"AssetName": "Krusty Krab", "Risk": 2.1, "ExpectedReturn": 8.4, "UnitCost": 130},
    {"AssetName": "MomCorp", "Risk": 7.7, "ExpectedReturn": 16.5, "UnitCost": 275},
    {"AssetName": "Planet Express", "Risk": 8.0, "ExpectedReturn": 11.3, "UnitCost": 265},
    {"AssetName": "Rekall Incorporated", "Risk": 6.3, "ExpectedReturn": 20.0, "UnitCost": 245},
    {"AssetName": "Wonka Industries", "Risk": 4.5, "ExpectedReturn": 22.7, "UnitCost": 185},
    {"AssetName": "Daily Planet", "Risk": 1.8, "ExpectedReturn": 6.2, "UnitCost": 110},
    {"AssetName": "Clampett Oil", "Risk": 3.6, "ExpectedReturn": 15.4, "UnitCost": 155},
    {"AssetName": "Shinra Electric Power Company", "Risk": 8.4, "ExpectedReturn": 14.7, "UnitCost": 295},
    {"AssetName": "Primatech Paper Co", "Risk": 3.2, "ExpectedReturn": 7.9, "UnitCost": 145},
    {"AssetName": "Doofenshmirtz Evil Inc", "Risk": 9.0, "ExpectedReturn": 5.5, "UnitCost": 320},
    {"AssetName": "Prestige Worldwide", "Risk": 5.8, "ExpectedReturn": 12.8, "UnitCost": 215},
    {"AssetName": "CHOAM", "Risk": 6.0, "ExpectedReturn": 15.0, "UnitCost": 220},
    {"AssetName": "Virtucon", "Risk": 7.8, "ExpectedReturn": 18.9, "UnitCost": 255},
    {"AssetName": "ZiffCorp", "Risk": 5.1, "ExpectedReturn": 14.0, "UnitCost": 210},
    {"AssetName": "Stay Puft Corporation", "Risk": 6.7, "ExpectedReturn": 10.7, "UnitCost": 205},
    {"AssetName": "Globotech Industries", "Risk": 4.0, "ExpectedReturn": 9.3, "UnitCost": 165},
    {"AssetName": "SPECTRE", "Risk": 9.5, "ExpectedReturn": 21.5, "UnitCost": 330},
    {"AssetName": "Sarif Industries", "Risk": 5.9, "ExpectedReturn": 16.4, "UnitCost": 225},
    {"AssetName": "The Krusty Krab", "Risk": 2.6, "ExpectedReturn": 10.1, "UnitCost": 135},
    {"AssetName": "BiffCo Enterprises", "Risk": 8.5, "ExpectedReturn": 13.3, "UnitCost": 305},
    {"AssetName": "Rich Industries", "Risk": 5.4, "ExpectedReturn": 12.4, "UnitCost": 195},
    {"AssetName": "Blade Runner Replicants", "Risk": 7.5, "ExpectedReturn": 25.8, "UnitCost": 255},
    {"AssetName": "Blue Sun Corporation", "Risk": 6.2, "ExpectedReturn": 18.3, "UnitCost": 235},
    {"AssetName": "Buy n Large", "Risk": 5.0, "ExpectedReturn": 17.9, "UnitCost": 210},
    {"AssetName": "Capsule Corp", "Risk": 3.5, "ExpectedReturn": 20.1, "UnitCost": 175},
    {"AssetName": "Devlin-McGregor Pharmaceuticals", "Risk": 6.1, "ExpectedReturn": 14.5, "UnitCost": 225},
    {"AssetName": "Dinoco", "Risk": 2.9, "ExpectedReturn": 12.0, "UnitCost": 140},
    {"AssetName": "Duff Brewing Company", "Risk": 4.4, "ExpectedReturn": 11.7, "UnitCost": 170},
    {"AssetName": "Frobozz Magic Company", "Risk": 8.1, "ExpectedReturn": 22.0, "UnitCost": 260},
    {"AssetName": "Gadgetron Corporation", "Risk": 7.0, "ExpectedReturn": 15.3, "UnitCost": 220},
    {"AssetName": "Gringotts Wizarding Bank", "Risk": 1.5, "ExpectedReturn": 7.5, "UnitCost": 105},
    {"AssetName": "Hyperion Corporation", "Risk": 9.2, "ExpectedReturn": 27.2, "UnitCost": 340},
    {"AssetName": "Ingolstadt", "Risk": 3.8, "ExpectedReturn": 13.0, "UnitCost": 180},
    {"AssetName": "Kumatsu Motors", "Risk": 4.7, "ExpectedReturn": 9.9, "UnitCost": 165},
    {"AssetName": "Los Pollos Hermanos", "Risk": 5.3, "ExpectedReturn": 12.6, "UnitCost": 200},
    {"AssetName": "Maroon Cartoon Studio", "Risk": 6.6, "ExpectedReturn": 10.9, "UnitCost": 105},
    {"AssetName": "Monarch Playing Card Co.", "Risk": 7.4, "ExpectedReturn": 14.8, "UnitCost": 110},
    {"AssetName": "Nebuchadnezzar Shipping", "Risk": 5.7, "ExpectedReturn": 11.1, "UnitCost": 95},
    {"AssetName": "Ollivander's Wand Shop", "Risk": 2.3, "ExpectedReturn": 8.7, "UnitCost": 80},
    {"AssetName": "Paper Street Soap Company", "Risk": 6.4, "ExpectedReturn": 16.0, "UnitCost": 120},
    {"AssetName": "Planetary Express", "Risk": 7.6, "ExpectedReturn": 14.4, "UnitCost": 115},
    {"AssetName": "Roxxon Energy Corporation", "Risk": 8.2, "ExpectedReturn": 20.3, "UnitCost": 130},
    {"AssetName": "Sirius Cybernetics Corporation", "Risk": 8.9, "ExpectedReturn": 23.7, "UnitCost": 140},
    {"AssetName": "Spacely Space Sprockets", "Risk": 4.1, "ExpectedReturn": 10.4, "UnitCost": 90},
    {"AssetName": "Strickland Propane", "Risk": 3.0, "ExpectedReturn": 9.6, "UnitCost": 85},
    {"AssetName": "The Android's Dungeon & Baseball Card Shop", "Risk": 4.8, "ExpectedReturn": 8.9, "UnitCost": 100},
    {"AssetName": "The Chum Bucket", "Risk": 3.7, "ExpectedReturn": 7.2, "UnitCost": 75},
    {"AssetName": "Umbra Witch Conglomerate", "Risk": 9.8, "ExpectedReturn": 26.5, "UnitCost": 15},
    {"AssetName": "Vehement Capital Partners", "Risk": 6.3, "ExpectedReturn": 19.8, "UnitCost": 125},
    {"AssetName": "Weasley's Wizard Wheezes", "Risk": 2.5, "ExpectedReturn": 15.5, "UnitCost": 105},
    {"AssetName": "Xanatos Enterprises", "Risk": 7.9, "ExpectedReturn": 22.1, "UnitCost": 135},
    {"AssetName": "Zorg Industries", "Risk": 8.7, "ExpectedReturn": 24.6, "UnitCost": 145},
    {"AssetName": "VersaLife", "Risk": 9.3, "ExpectedReturn": 21.2, "UnitCost": 140},
    {"AssetName": "Happy Harry's Pharmacy", "Risk": 3.1, "ExpectedReturn": 8.5, "UnitCost": 80},
]


class Portfolio:
        
    def __init__(self, nb_asset: int) -> None:
        self.nb_asset = nb_asset

        if nb_asset > len(ASSETS):
            raise ValueError("Number of assets requested exceeds available unique assets.")

        self.financial_assets = random.sample(ASSETS, nb_asset)

    def get_assets(self):
        return self.financial_assets