import random
import json
from time import sleep

import pandas as pd
from dataclasses import dataclass, asdict
from typing import List
import pickle


class Game:
    def __init__(self, players):
        self.grid = []
        self.players: List[Player] = players
        self.turn: int = 0
        self.properties: List[Property] = []

    def roll(self, player_id):
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        roll = roll1+roll2
        self.players[player_id].position += roll
        self.players[player_id].position %= 22

    def buy(self, player_id):
        player = self.players[player_id]
        property_id = player.position
        property = self.properties[property_id]
        if player.money >= property.price and property.owner==-1:
            player.properties.append(property_id)
            player.money -= self.properties[property_id].price
            property.owner = player_id


    def to_json(self):
        out = {
            "turn": self.turn
        }
        for player in self.properties:
            out.update(player.dict())
        with open("sample.json", "w") as outfile:
            json.dump(out, outfile)


@dataclass
class Property:
    title: str
    price: int
    # Level is the number of houses/hotels on a property. 0: none, 5: hotel
    level: int
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
    # The owner will be the player id
    owner: int

    def dict(self):
        return asdict(self).items()

    # should only be called after making sure that it doesn't have any houses on it
    def mortgage(self):
        self.rent_no_set = 0
        
@dataclass
class Player:
    id: int
    title: str
    piece: str
    position: int
    money: int
    # The player owns a list of property IDs
    properties: List[int]

    def mortgage(self, property) :
        # Make sure the player owns the property they're attempting to mortgage and that it has no houses
        if property in self.properties and property.get('level') == 0 :
            # Mortgage the property
            self.properties.property.mortgage()
            # Give the player the mortgage money
            self.money += property.get('mortgage')

    # Converts dataclass to dictionary
    def dict(self):
        return asdict(self)


def read_data(in_filename: str):
    data = pd.read_csv(in_filename, index_col=0)
    properties = []
    for title in data.index.values:
        values = [int(x) for x in data.loc[title].iloc[0: -1]]
        properties.append(Property(title, *values, data.loc[title].iloc[-1], -1))
    return properties

def get_input() :
    try:
        user_input = str(input('enter c to continue turn, x to stop '))
    except TypeError:
        print('that\'s not a valid input bro')
        get_input()
    return user_input

def get_input() :
    try:
        user_input = str(input('enter c to continue turn, x to stop '))
    except TypeError:
        print('that\'s not a valid input bro')
        get_input()
    return user_input

tiles = read_data("properties.csv")
player1 = Player(0, "Seamus", "dog", 0, 1500, [])
player2 = Player(1, "Nickolai", "dog", 0, 1500, [])
game = Game([player1, player2])
game.properties = tiles

game.to_json()

while get_input() != 'x':
    print('\n\n')
    ID = game.turn % len(game.players)
    print("Turn:", game.turn)
    print('Player:', game.players[ID].title)
    game.roll(ID)
    print('Position:', game.players[ID].position)
    print('Money:', game.players[ID].money)
    game.buy(ID)
    print('\nOwned properties: ')
    for property in game.players[ID].properties:
        print('  ', game.properties[property].title)
    game.turn += 1

    print("\n\n")