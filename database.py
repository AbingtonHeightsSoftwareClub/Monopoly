from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, registry
import pandas as pd
import numpy as np
engine = create_engine("sqlite:///data.orm")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, Sequence('player_id_seq'), primary_key=True)
    title = Column(String(50))
    piece = Column(Integer)
    position = Column(Integer)
    money = Column(Integer)
    # The player owns a list of properties
    properties = relationship("Property",
                              back_populates="player")  # Backpopulates to other relationship column/variable. Not class object name.

    def __repr__(self):
        return f"Player: ID: {self.id}, Title: {self.title}, Piece: {self.piece}, Money: {self.money}"


class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    user_id = Column(Integer, ForeignKey("players.id"))

    price = Column(Integer)
    rent_no_set = Column(Integer)
    rent_color_set = Column(Integer)
    rent_1_house = Column(Integer)
    rent_2_house = Column(Integer)
    rent_3_house = Column(Integer)
    rent_4_house = Column(Integer)
    rent_hotel = Column(Integer)
    building_cost = Column(Integer)
    mortgage = Column(Integer)
    unmortgage = Column(Integer)
    color = Column(String(10))

    player = relationship("Player",
                          back_populates="properties")  # Must be same as what the other back_populates is called

    def __repr__(self):
        return f"Title: {self.title}, Price: {self.price}"


Base.metadata.create_all(engine)


def add_player(session: Session, title: str, piece: int, position: int, money: int):
    session.add(Player(title=title, piece=piece, position=position, money=money))

def add_properties(session:Session, in_filename: str):
    data = pd.read_csv(in_filename, index_col=0)
    for title in data.index.values:
        #values = [int(x) for x in data.loc[title].iloc[0: -1]]
        session.add(Property(title = title,
                             price=int(data.loc[title][0]),
                             rent_no_set=int(data.loc[title][1]),
                             rent_color_set=int(data.loc[title][2]),
                             rent_1_house=int(data.loc[title][3]),
                             rent_2_house=int(data.loc[title][4]),
                             rent_3_house=int(data.loc[title][5]),
                             rent_4_house=int(data.loc[title][6]),
                             rent_hotel=int(data.loc[title][7]),
                             building_cost=int(data.loc[title][8]),
                             mortgage=int(data.loc[title][9]),
                             unmortgage=int(data.loc[title][10]),
                             color=data.loc[title].iloc[-1]))

add_player(session, "Alice", 10, 10, 10)
add_properties(session, "properties.csv")
session.commit()



for prop in session.query(Property).all():
    print(prop)
