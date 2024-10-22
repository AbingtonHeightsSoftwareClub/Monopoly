import random
import json
import pandas as pd
from dataclasses import dataclass, asdict
from typing import List


class Game:
    def __init__(self, players):
        # We'll need to actually define the grid at some point, rn its just the 23 properties
        tiles = read_data("properties.csv")
        self.grid = tiles
        # I made this into a dictionary so all the calls work
        self.players = players
        self.turn = 0
        #not sure what this variable is supposed to be, doesn't the grid contain the properties?
        self.properties = {}

# Both rolls dice, moves player, and prompts player if they landed on a property
    def roll(self, player):
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        self.players[player.title].position += roll1 + roll2
        #change to 40 once we make the acual board
        self.players[player.title].position %= 23
        print(roll1, roll2)
        # If not owned prompt user
        if not self.grid[self.players[player.title].position].owned:
            self.decision(player)
        #need to implement rent cost here
        if roll1 != roll2:
            # This will let you roll again once we implement turns
            self.turn += 1
            self.turn %= len(self.players)

# Doesn't work rn cause of my confusion with the properties variable
# Returns whether the buy was successful
    def buy(self, player, property):
        if self.players[player.title].money >= self.properties[property.title].price:
            self.players[player.title].properties.update({property.title: self.properties[property.title]})
            self.players[player.title].money -= self.properties[property.title].price
            print(player.title, "bought", property.title, "for", self.properties[property.title].price)
            return True
        print("Not Enough Money")
        return False
    
# Prompts the user with whether to buy a property, returns if the property was bought
    def decision(self, player):
        dec = input("Buy Property?").lower()
# Repeats until user enters "yes" or "no"
        while(True):
            match dec:
#Not calling buy method cause it doesn't work
                case "yes":
                    #return self.buy(player, self.grid[self.players[player.title].position])
                    return True#
                case "no":
                    return False
                case _:
                    dec = input("Enter Yes or No").lower()

    def to_json(self):
        out = {
            "turn": self.turn
        }
        for player in self.properties:
            print(player.dict())
            out.update(player.dict())
        print(out)
        with open("sample.json", "w") as outfile:
            json.dump(out, outfile)


class Tile:
    def __init__(self, title, position):
        self.title = title
        self.position = position


@dataclass
class Property:
    title: str
    price: int
    rent_no_set: int
    rent_color_set: int
    rent_1_house: int
    rent_2_house: int
    rent_3_house: int
    rent_4_house: int
    rent_hotel: int
    building_cost: int
    mortgage: int
    unmortgage: int
    color: str
    #I think this is needed to determine if you can buy a property
    owned: bool

    def dict(self):

        return asdict(self).items()


@dataclass
class Player:
    title: str
    piece: str
    position: int
    money: int
    properties: List[Property]

    #Converts dataclass to dictionary
    def dict(self):
        return asdict(self)



def read_data(in_filename: str):
    data = pd.read_csv(in_filename, index_col=0)
    properties = []
    for title in data.index.values:
        values = [int(x) for x in data.loc[title].iloc[0: -1]]
        properties.append(Property(title, *values, data.loc[title].iloc[-1], False))
    return properties

player1 = Player("Seamus", "dog", 10, 1500, [])
# The players are treated as a dict so I figured they should be a dict
game = Game({player1.title: player1})
print(game.players)
game.roll(player1)
game.to_json()


