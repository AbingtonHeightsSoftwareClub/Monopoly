import random
def ComputerPlays(Computer, ComputerProp, board, Player, PlayerProp, Comp1, Comp1Prop, Comp2, Comp2Prop, Comp3,
                  Comp3Prop, CompNum):  ## Function for the Computer's turn
    def RailroadChecker(user, userProp):
        railroad_counter = 0
        railroads = []
        for x in range(len(user[2:])):
            if user[x + 2][1] == "RR":
                railroad_counter += 1
                railroads.append(x + 2)
        if railroad_counter == 2:
            for x in range(len(userProp)):
                if x + 2 in railroads:
                    userProp[x] = 50
        elif railroad_counter == 3:
            for x in range(len(userProp)):
                if x + 2 in railroads:
                    userProp[x] = 100
        elif railroad_counter == 4:
            for x in range(len(userProp)):
                if x + 2 in railroads:
                    userProp[x] = 200
        return userProp

    def monopolyChecker(user):  ## Checks if the Computer owns a monopoly by checking if they have enough colors
        if len(user) > 2:  ## Sees if the user has any properties
            temp = user[-1][1]  ## Sets temp to the color group of the last property the user got
            monopolies = []
            railroad_counter = 0
            for y in range(len(user[2:])):  ## y goes from 0 to the length of "user" the list
                color = 0
                for x in user[y + 2:]:  ## x goes through all the user's properties
                    if x[1] == temp:  ## Checks if the color group of x is the color group focused on
                        color += 1
                if (
                        temp == "brown" or temp == "dBlue") and color == 2:  ## If there are 2 properties in a color group and the group is dark blue or brown.
                    monopolies.append(temp)  ## adds temp to the list of color groups which have a monopoly
                elif temp == "RR":  ## If user owns a railroad
                    monopolies.append(temp)  ## adds railroad to list of color groups
                elif (
                        temp == "lBlue" or temp == "pink" or temp == "orange" or temp == "red" or temp == "yellow" or temp == "green") and color == 3:
                    monopolies.append(temp)
                if len(user) > y + 3:
                    temp = user[-1 * (y + 2)][
                        1]  ## Changes temp to another property user owns if they have more than y+3
            for y in monopolies:
                if y == "RR":
                    railroad_counter += 1
            if railroad_counter == len(monopolies):  ## If railroad is the only monopoly the user owns
                return monopolies, "Railroad"  ## returns the list of monopoly types (only railroad) and that it is only railroad
            elif len(monopolies) != 0:  ## If railroad isnt the only monopoly and there is more than 0
                return monopolies, "color"  ## returns the list of monopoly colors and that there is at least one color monopoly
            else:
                return "none", "none"  ## returns no monopoly
        else:
            return "none", "none"
    repeated = 0
    while repeated == 0:
        ComputerProp = RailroadChecker(Computer, ComputerProp)
        dice_1, dice_2 = random.randint(1, 6), random.randint(1, 6)  ## sets dice_1 and dice_2 to random numbers from 1 to 6
        print("Computer " + CompNum + " rolled " + str(dice_1) + " and " + str(dice_2) + "!")
        if Computer[1] == "Jail":  ## If the Computer is still in Jail
            if dice_1 == dice_2:
                print("Computer " + CompNum + " rolled a double and got out of Jail!")
                Computer[1] = 8  ## Computer is set to the space on the board of "just visiting"
            else:
                print("Computer " + CompNum + " is still in Jail")
                return ComputerProp, Player, Comp1, Comp2, Comp3, Computer
        Computer[1] += dice_1 + dice_2  ## Computer's space on the board increases by the numbers on the dice
        if Computer[1] > 31:  ## if the computer's space is past the board
            Computer[1] -= 31  ## restarts the computer's space to the beginning
            Computer[0] += 200  ## Computer gets $200 for passing go
            print("Computer " + CompNum + " passed Go! and got $200")
        if board[Computer[1]] == "Go!":
            print("Computer " + CompNum + " landed on Go!")
        elif board[Computer[1]] == "Income Tax":
            if 0.1 * Computer[0] > 200:  ## If 10% of the Computer's money is more than $200
                Computer[0] -= 200
                print("Computer " + CompNum + " landed on Income Tax and lost $200")
            else:  ## if 10% of the Computer's money <= $200
                print("Computer " + CompNum + " landed on Income Tax and lost $" + str(0.1 * Player[0]))
                Computer[0] -= int(round(0.1 * Computer[0]))
        elif board[Computer[1]] == "Luxury Tax":
            print("Computer " + CompNum + " landed on Luxury Tax and lost $75")
            Computer[0] -= 75
        elif board[Computer[1]] == "Just Visiting Jail":
            print("Computer " + CompNum + " is just vising jail!")
        elif board[Computer[1]] == "Free Parking":
            print("Computer " + CompNum + " landed on Free Parking!")
        elif board[Computer[1]] == "Go To Jail":
            print("Computer " + CompNum + " landed on Go To Jail and went to Jail!")
            Computer[1] = "Jail"  ## set's Computer's place to Jail
        else:
            print("Computer " + CompNum + " landed on " + board[Computer[1]][0])  ## The Computer's spot on the board is a property's variable, so it is that property's 0th index
            if board[Computer[1]] in Computer:  ## If the spot Computer landed on is already a property Computer owns.
                print("Computer " + CompNum + " already owns that property!")
            elif board[Computer[1]] in Player:  ## If the spot Computer landed on is already a property Player owns.
                Computer[0] -= PlayerProp[Player.index(board[Computer[1]]) - 2]  ## Computer gets charged the price of rent which is in PlayerProp.
                Player[0] += PlayerProp[Player.index(board[Computer[1]]) - 2]  ## Player gets paid the price of rent
                print("Computer " + CompNum + " paid you $" + str(PlayerProp[Player.index(board[Computer[1]]) - 2]))
                print("You now have $" + str(Player[0]))
                print("Computer " + CompNum + " has $" + str(Computer[0]))
            elif board[Computer[1]] in Comp1 and Computer != Comp1:  ## If the spot Computer landed on is already a property Comp1 owns.
                Computer[0] -= Comp1Prop[Comp1.index(board[Computer[1]]) - 2]  ## Computer gets charged the price of rent which is in Comp1Prop.
                Comp1[0] += Comp1Prop[Comp1.index(board[Computer[1]]) - 2]  ## Comp1 gets paid the price of rent
                print("Computer " + CompNum + " paid Computer 1 $" + str(Comp1Prop[Comp1.index(board[Computer[1]]) - 2]))
                print("Computer 1 has $" + str(Comp1[0]))
                print("Computer " + CompNum + " has $" + str(Computer[0]))
            elif board[Computer[1]] in Comp2 and Computer != Comp2:  ## If the spot Computer landed on is already a property Comp2 owns.
                Computer[0] -= Comp2Prop[Comp2.index(board[Computer[1]]) - 2]  ## Computer gets charged the price of rent which is in Comp2Prop.
                Comp2[0] += Comp2Prop[Comp2.index(board[Computer[1]]) - 2]  ## Comp2 gets paid the price of rent
                print("Computer " + CompNum + " paid Computer 2 $" + str(Comp2Prop[Comp2.index(board[Computer[1]]) - 2]))
                print("Computer 2 has $" + str(Comp2[0]))
                print("Computer " + CompNum + " has $" + str(Computer[0]))
            elif board[Computer[1]] in Comp3 and Computer != Comp3:  ## If the spot Computer landed on is already a property Comp3 owns.
                Computer[0] -= Comp3Prop[Comp3.index(board[Computer[1]]) - 2]  ## Computer gets charged the price of rent which is in Comp3Prop.
                Comp3[0] += Comp3Prop[Comp3.index(board[Computer[1]]) - 2]  ## Comp3 gets paid the price of rent
                print("Computer " + CompNum + " paid Computer 3 $" + str(Comp3Prop[Comp3.index(board[Computer[1]]) - 2]))
                print("Computer 3 has $" + str(Comp3[0]))
                print("Computer " + CompNum + " has $" + str(Computer[0]))
            elif Computer[0] * .4 > board[Computer[1]][2]:  ## If no one owns the property and Computer's money *.4 is greater than the price to buy
                Computer[0] -= board[Computer[1]][2]  ## Computer gets charged the price to buy
                Computer.append(board[Computer[1]])  ## Property gets appended to Computer's property list
                ComputerProp.append(board[Computer[1]][3])  ## Computer's list of rents gets appended the Property's rent
                print("Computer " + CompNum + " has successfully bought " + Computer[-1][0])
                print("Computer " + CompNum + " has $" + str(Computer[0]))
                monopoly_color, monopoly_type = monopolyChecker(Computer)
                if monopoly_type == "color":  ## Checks if the monopoly color that the Player has a monopoly on is the same as the property the Player bought.
                    for x in range(len(Computer[2:])):  ## x goes from 1 to the total number of properties the Player has.
                        if Computer[x + 2][1] == board[Computer[1]][1]:  # Sees if the Property x is scolling though matches the color of the property the Player.
                            ComputerProp[x] = Computer[x + 2][4]  # Changes the current rent price of the selected property to the one when there is a monopoly.
                ComputerProp = RailroadChecker(Computer, ComputerProp)
        repeated = 1
        if dice_1 == dice_2:
            print("Computer " + str(CompNum) + " rolled a double, and gets to roll again!")
            repeated = 0
    mortgages = []
    monopolies = []
    if Computer[0] < 500 and len(Computer) > 2:  ## If Computer has less than $500 and has at least one property
        for y in range(len(Computer[2:])):  ## Y goes from 0 to the length of Computer's list
            if ComputerProp[y] > Computer[y + 2][
                4]:  ## If the price for rent of the selected property is more than it is for the monopoly
                monopolies.append(Computer[y + 2])  ## The property itself gets appended to monopolies.
            if Computer[y + 2][-2] + Computer[0] > 500 and ComputerProp[
                y] != 0:  ## If the mortgage price plus the Computer's money is greater than $500 and the property is not yet mortgaged.
                mortgages.append(Computer[y+2])  ## The property itself gets appended to mortgages.
        if len(monopolies) > 0:  ## If there is at least one element in monopolies
            prop = random.randint(0, len(monopolies) - 1)  ## The selected property is a random integer from monopolies
            for x in range(1, (monopolies[prop].index(ComputerProp[Computer.index(
                    monopolies[prop]) - 2] - 2))):  ## x goes from 1 to the number of houses on the selected property
                if Computer[0] + (monopolies[prop][-3] * x * .5) > 550:  ## If half the selected property's price to buy a house times the number of houses selected plus the Computer's total money is greater than $550
                    Computer[0] += monopolies[prop][-3] * x * .5  ## The computer gets half the selected property's price to buy a house times the number of houses
                    ComputerProp[prop - 2] = monopolies[prop][monopolies[prop].index(ComputerProp[Computer.index(
                        monopolies[
                            prop]) - 2]) + 1 - x]  ## The price of rent is changed to the number of houses -x ( which is the number of houses it changed by)
                    print("Computer " + CompNum + " has successfully sold houses on " + monopolies[prop] + "!")
                    print("Computer " + CompNum + " has $" + str(Computer[0]))
        elif len(mortgages) > 0:  ## If there is at least one element in mortgages
            prop = Computer.index(mortgages[random.randint(0, len(mortgages) - 1)])  ## The selected property is a randomly chosen index from the list mortgages
            ComputerProp[prop - 2] = 0  ## The selected property's rent is set to 0
            Computer[0] += Computer[prop][-2]  ## Computer gets the price to mortgage a property
            print("Computer " + CompNum + " has successfully mortgaged " + Computer[prop][0])
            print("Computer " + CompNum + " has $" + str(Computer[0]))
    mortgages = []
    if Computer[0] > 1000 and 0 in ComputerProp:  ## If Computer has more than $1000 and has properties mortgaged
        print("mortgagedsed")
        for y in range(len(Computer[2:])):  ## Y goes from 0 to the length of Computer's list
            if Computer[0] - Computer[y + 2][-1] > 700 and ComputerProp[y] == 0:  ## if the Computer's money - the price to unmortgage the selected property is still > $700 and the property is mortgaged
                mortgages.append(y)  ## The property itself gets appended to mortgages.
        if len(mortgages) > 0:  ## If there is at least one element in mortgages
            prop = Computer.index(mortgages[random.randint(0,
                                                           len(mortgages) - 1)])  ## The selected property is a randomly chosen index from the list mortgages
            monopoly_color, monopoly_type = monopolyChecker(Computer)
            if Computer[prop][
                1] in monopoly_color:  ## If the selected property's is part of one of the Computer's monopolies.
                ComputerProp[prop - 2] = Computer[prop][
                    4]  ## The selected property's rent is set to the price of rent with a monopoly.
            else:
                ComputerProp[prop - 2] = Computer[prop][
                    3]  ## The selected property's rent is set to the regular price of rent.
            Computer[0] -= Computer[prop][-1]  ## Computer gets charged for the mortgage
            print("Computer " + CompNum + " has successfully unmortgaged " + Computer[prop][0])
            print("Computer " + CompNum + " has $" + str(Computer[0]))

    #TRADING

    colors_has = []
    wanted_prop = []
    Comp_prop = []
    total_wanted = 0
    possible_traders = []
    for x in Computer[2:]:
        colors_has.append(x[1])  ## makes a list of all the colors Computer has.
    for x in [Player, Comp1, Comp2, Comp3]:
        prop = 0
        for y in x[2:]:
            if y[1] in colors_has and x != Computer: ##and y[-1] * 2 + total_wanted >= .7 * Computer[0]: ## Do I need the last check?
                possible_traders.append(x)
                #wanted_prop.append(y)
                #total_wanted += y[-1] * 2
                #prop += 1
        #Comp_prop.append(prop)
        #if total_wanted >= .7 * Computer[0]:
         #   continue
    if len(possible_traders) > 1:
        tradee = possible_traders[random.randint(0, len(possible_traders)-1)]
    else:
        return ComputerProp, Player, Comp1, Comp2, Comp3, Computer
    for y in tradee[2:]:
        if y[1] in colors_has and x != Computer and y[-1] * 2 + total_wanted >= .7 * Computer[0]:
            wanted_prop.append(y)
            total_wanted += y[-1] * 2
    #Computer_traded = [Player, Comp1, Comp2, Comp3][Comp_prop.index(max(Comp_prop))]
    traded_prop = []
    total_traded = 0
    for x in Computer[2:]:
        traded_prop.append(x)
        for y in wanted_prop:
            if x[1] == y[1]:
                traded_prop.pop(-1)
    for x in traded_prop:
        total_traded += x[-1] * 2
    money_wanted = 0
    money_traded = 0
    if total_traded < total_wanted:
        money_wanted = total_wanted - total_traded
    elif total_wanted < total_traded:
        return ComputerProp, Player, Comp1, Comp2, Comp3, Computer


    if tradee == Player and (len(traded_prop) > 0 or len(wanted_prop) > 0):
        print("Computer " + str(CompNum) + " wants to trade with you.")
        print("Computer " + str(CompNum) + " will give:")
        for x in traded_prop:
            print("    ", x[0])
        if len(traded_prop) > 1:
            print("     and $" + str(money_traded))
        else:
            print("$" + str(money_traded))
        print("Computer " + str(CompNum) + " wants:")
        for x in wanted_prop:
            print("    ", x[0])
        if len(traded_prop) > 1:
            print("     and $" + str(money_wanted))
        else:
            print("$" + str(money_wanted))
        trade_command = input("Do you want to trade?")
        while trade_command != "yes" and trade_command != "no":
            print("That is not a proper command!")
            print("Please input 'yes' or 'no'!")
            trade_command = input()
        if trade_command == "no":
            return ComputerProp, Player, Comp1, Comp2, Comp3, Computer
        else:
            print("You have successfully traded with Computer " + str(CompNum))
            Computer[0] += money_wanted  ## Computer gets all the money Player offered
            Player[0] += money_traded  ## Player gets all the money they wanted
            for x in range(len(wanted_prop)):  ## x goes from 0 to the length of traded_properties
                PlayerProp.pop(Player.index(wanted_prop[x]) - 2)  ## Removes the rent price of the selected property
                Player.pop(Player.index(wanted_prop[x]))  ## Property x gets taken from Player
                ComputerProp.append(wanted_prop[x][3])  ## Adds the rent price of the selected property
                Computer.append(wanted_prop[x])  ## Computer gets Property x
            for x in range(len(traded_prop)):  ## x goes from 0 to the length of wanted_properties
                ComputerProp.pop(Computer.index(traded_prop[x]) - 2)
                Computer.pop(Computer.index(traded_prop[x]))  ## Property x gets taken from Player
                Player.append(traded_prop[x])  ## Computer gets Property x
                PlayerProp.append(traded_prop[x][3])  ## Adds the rent price of the selected property
    else:
        if total_traded >= total_wanted:
            print("Computer " + str(CompNum) + "has successfully traded with Computer " + str([Comp1, Comp2, Comp3].index(tradee)))
            Computer[0] += money_traded  ## Computer gets all the money Player offered
            tradee[0] += money_wanted  ## tradee gets all the money they wanted
            for x in range(len(wanted_prop)):  ## x goes from 0 to the length of traded_properties
                PlayerProp.pop(Player.index(wanted_prop[x]) - 2)  ## Removes the rent price of the selected property
                Player.pop(Player.index(wanted_prop[x]))  ## Property x gets taken from Player
                ComputerProp.append(wanted_prop[x][3])  ## Adds the rent price of the selected property
                Computer.append(wanted_prop[x])  ## Computer gets Property x
            for x in range(len(traded_prop)):  ## x goes from 0 to the length of wanted_properties
                ComputerProp.pop(Computer.index(traded_prop[x]) - 2)
                Computer.pop(Computer.index(traded_prop[x]))  ## Property x gets taken from Player
                Player.append(traded_prop[x])  ## Computer gets Property x
                PlayerProp.append(traded_prop[x][3])  ## Adds the rent price of the selected property

    monopolies = []
    monopoly_color, monopoly_type = monopolyChecker(Computer)
    if Computer[0] > 1000 and monopoly_type == "color":  ## If Computer has more than $1000 and at least 1 monopoly
        for x in range(len(Computer[2:])):  ## x goes from 0 to the length of Computer's list
            if Computer[x + 2][1] in monopoly_color and ComputerProp[x] != Computer[x + 2][
                -4]:  ## If the selected property is a monopoly and the property does not have 1 hotel.
                monopolies.append(Computer[x + 2])  ## The property gets appended to monopolies.
    if monopoly_type != "color":  ## If there is not color monopoly
        return ComputerProp, Player, Comp1, Comp2, Comp3, Computer  ## returns any values that may have been changed
    if len(monopolies) > 0:  ## If there is more than one element in monopolies.
        prop = random.randint(0, len(monopolies) - 1)  ## the selected property is a random index from monopolies
        for x in range(5, 1, -1):  ## x decends from 5 to 1
            if (Computer[0] + ((monopolies[prop][
                -3]) * x)) > 700:  ## If Computer still has $700 after building x amount of houses on the selected property
                Computer[0] -= monopolies[prop][-3] * x  ## Computer gets charged x amount of houses
                ComputerProp[prop - 2] = monopolies[prop][
                    4 + x]  ## the price for rent changes to the price for x amount of houses
                if x == 5:  ## If the amount of houses is 5
                    x = "hotel"
                    prop = 1
                else:
                    prop = x
                    x = "houses"
                print("Computer " + CompNum + " has successfully built " + str(prop) + " " + x)
                print("Computer " + CompNum + " has $" + str(Computer[0]))
                return ComputerProp, Player, Comp1, Comp2, Comp3, Computer

    return ComputerProp, Player, Comp1, Comp2, Comp3, Computer


def monopolyChecker(user):  ## Checks if the Player owns a monopoly by checking if they have enough colors
    if len(user) > 2:  ## Sees if the user has any properties
        temp = user[-1][1]  ## Sets temp to the color group of the last property the user got
        monopolies = []
        railroad_counter = 0
        for y in range(len(user[2:])):  ## y goes from 0 to the length of "user" the list
            color = 0
            for x in user[y + 2:]:  ## x goes through all the user's properties
                if x[1] == temp:  ## Checks if the color group of x is the color group focused on
                    color += 1
            if (temp == "brown" or temp == "dBlue") and color == 2:  ## If there are 2 properties in a color group and the group is dark blue or brown.
                monopolies.append(temp)  ## adds temp to the list of color groups which have a monopoly
            elif temp == "RR":  ## If user owns a railroad
                monopolies.append(temp)  ## adds railroad to list of color groups
            elif (temp == "lBlue" or temp == "pink" or temp == "orange" or temp == "red" or temp == "yellow" or temp == "green") and color == 3:
                monopolies.append(temp)
            if len(user) > y + 3:
                temp = user[-1 * (y + 2)][1]  ## Changes temp to another property user owns if they have more than y+3
        for y in monopolies:
            if y == "RR":
                railroad_counter += 1
        if railroad_counter == len(monopolies):  # If railroad is the only monopoly the user owns
            return monopolies, "Railroad"  ## returns the list of monopoly types (only railroad) and that it is only railroad
        elif len(monopolies) != 0:  ## If railroad isnt the only monopoly and there is more than 0
            return monopolies, "color"  ## returns the list of monopoly colors and that there is at least one color monopoly
        else:
            return "none", "none"  ## returns no monopoly
    else:
        return "none", "none"


def RailroadChecker(user, userProp):
    railroad_counter = 0
    railroads = []
    for x in user[2:]:
        if x[1] == "RR":
            railroad_counter += 1
            railroads.append(user.index(x))
    if railroad_counter == 2:
        for x in range(len(userProp)):
            if x + 2 in railroads:
                userProp[x] = 50
    elif railroad_counter == 3:
        for x in range(len(userProp)):
            if x + 2 in railroads:
                userProp[x] = 100
    elif railroad_counter == 4:
        for x in range(len(userProp)):
            if x + 2 in railroads:
                userProp[x] = 200
    return userProp


## Properties are ordered starting with their name, their color group, the price to buy, the price for rent, the price for rent with a monopoly, 1 house - 1 hotel, price to buy 1 house, price from mortgaging, price to unmortgage
MediterraneanAve, BalticAve = ["Mediterranean Avenue", "brown", 60, 2, 4, 10, 30, 90, 160, 250, 50, 30, 33], [
    "Baltic Avenue", "brown", 60, 4, 8, 20, 60, 180, 320, 450, 50, 30, 33]
OrientalAve, VermontAve, ConneticutAve = ["Oriental Avenue", "lBlue", 100, 6, 12, 30, 90, 270, 400, 500, 50, 50, 55], [
    "Vermont Avenue", "lBlue", 100, 6, 12, 30, 90, 270, 400, 500, 50, 50, 55], ["Conneticut Avenue", "lBlue", 120, 8,
                                                                                16, 40, 100, 300, 450, 600, 50, 60, 66]
StCharlesPlace, StatesAve, VirginiaAve = ["St. Charles Place", "pink", 140, 10, 20, 50, 150, 450, 625, 750, 100, 70,
                                          77], ["States Avenue", "pink", 140, 10, 20, 50, 150, 450, 625, 750, 100, 70,
                                                77], ["Virginia Avenue", "pink", 160, 12, 24, 60, 180, 500, 700, 900,
                                                      100, 80, 88]
StJamesPlace, TennesseAve, NewYorkAve = ["St. James Place", "orange", 180, 14, 28, 70, 200, 550, 750, 950, 100, 90,
                                         99], ["Tennessee Avenue", "orange", 180, 14, 28, 70, 200, 550, 750, 950, 100,
                                               90, 99], ["New York Avenue", "orange", 200, 16, 32, 80, 220, 600, 800,
                                                         1000, 100, 100, 110]
KentuckyAve, IndianaAve, IllinoisAve = ["Kentucky Avenue", "red", 220, 18, 36, 90, 250, 700, 875, 1050, 150, 110,
                                        121], ["Indiana Avenue", "red", 220, 18, 36, 90, 250, 700, 875, 1050, 150, 110,
                                               121], ["Illinois Avenue", "red", 240, 20, 40, 100, 300, 750, 925, 1100,
                                                      150, 120, 132]
AlanticAve, VentnorAve, MarvinGardens = ["Alantic Avenue", "yellow", 260, 22, 44, 110, 330, 800, 975, 1150, 150, 130,
                                         143], ["Ventor Avenue", "yellow", 260, 22, 44, 110, 330, 800, 975, 1150, 150,
                                                130, 143], ["Marvin Gardens", "yellow", 280, 24, 48, 120, 360, 850,
                                                            1025, 1200, 150, 140, 154]
PacificAve, NorthCarolinaAve, PennsylvaniaAve = ["Pacific Avenue", "green", 300, 26, 52, 130, 390, 900, 110, 1275, 200,
                                                 150, 165], ["North Carolina Avenue", "green", 300, 26, 52, 130, 390,
                                                             900, 110, 1275, 200, 150, 165], ["Pennsylvania Avenue",
                                                                                              "green", 320, 28, 56, 150,
                                                                                              450, 1000, 1200, 1400,
                                                                                              200, 160, 176]
ParkPlace, BoardWalk = ["Park Place", "dBlue", 350, 35, 70, 175, 500, 110, 1300, 1500, 200, 175, 193], ["Boardwalk",
                                                                                                        "dBlue", 400,
                                                                                                        50, 100, 200,
                                                                                                        600, 1400, 1700,
                                                                                                        2000, 200, 200,
                                                                                                        220]
ReadingRR, PennRR, BORR, ShortLine = ["Reading Railroad", "RR", 200, 25, 100, 110], ["Pennsylvania Railroad", "RR", 200,
                                                                                     25, 100, 110], ["B&O Railroad",
                                                                                                     "RR", 200, 25, 100,
                                                                                                     110], [
                                         "Short Line", "RR", 200, 25, 100, 110]
board = ["Go!", MediterraneanAve, BalticAve, "Income Tax", ReadingRR, OrientalAve, VermontAve, ConneticutAve,
         "Just Visiting Jail", StCharlesPlace, StatesAve, VirginiaAve, PennRR, StJamesPlace, TennesseAve, NewYorkAve,
         "Free Parking", KentuckyAve, IndianaAve, IllinoisAve, BORR, AlanticAve, VentnorAve, MarvinGardens,
         "Go To Jail", PacificAve, NorthCarolinaAve, PennsylvaniaAve, ShortLine, ParkPlace, "Luxury Tax", BoardWalk]
## users are set with their money, space they land on, and any monopoly they owns after that
## userProp is the price for every property in the same order the propeties are listed in user

Player = [1500, 0]
## Every Player has their own list. Index 0 is the amount of $ that the Player has. Index 1 is the space that the player is on (0-31). Indexes 2+ are the names of Properties the Player owns.

PlayerProp = [] 
## Every Player has a property list. This list shows the rent price for each property. The rent price for property at index 0, for example, correlates with the property at Player at index 2.
## The rent price at index 1 correlates with the property at index 3.

Comp1 = [1500, 0]
Comp1Prop = []
Comp2 = [1500, 0]
Comp2Prop = []
Comp3 = [1500, 0]
Comp3Prop = []
repeated = 0  ## value is 0 if the player didn't roll, and is 1 if the Player did
command = ""
double_counter = 0
jail_counter = 0
while Player[0] > 0 or (Comp1[0] > 0 and Comp2[0] > 0 and Comp3[0] > 0):
    PlayerProp = RailroadChecker(Player, PlayerProp)
    if repeated == 0:  ## If the player didn't roll
        command = input("Do you want to 'roll', 'build/sell', 'mortgage/unmortgage', or 'trade' ")
    elif repeated == 1:  ## If the Player did roll
        command = input("Do you want to 'build/sell', 'mortgage/unmortgage', 'trade', or 'end turn'? ")
    if command == "roll" and repeated == 0:
        repeated += 1  ## Sets that the Player did roll
        dice_1, dice_2 = random.randint(1, 6), random.randint(1,6)  ## sets dice_1 and dice_2 to random numbers from 1 to 6
        print("You rolled " + str(dice_1) + " and " + str(dice_2) + "!")
        if Player[1] == "Jail":  ## If the Player is still in Jail
            if dice_1 == dice_2:
                print("You rolled a double and got out of Jail!")
                Player[1] = 8  ## Player is set to the space on the board of "just visiting"
                jail_counter = 0
            elif jail_counter == 3:
                print("You spend three turns in jail and now have to leave, paying a $50 fee!")
                Player[0] -= 50
            else:
                print("You are still in Jail")
                jail_counter += 1
                jail_command = input("Do you want to pay a $50 fee to get out?")
                while jail_command.lower() != "yes" and jail_command.lower() != "no":  ## While the Player did not enter "yes" or "no" as their buy_command
                    print("That is not a command! Please enter 'yes' or 'no'")
                    buy_command = input()
                if jail_command == "yes":
                    Player[0] -= 50
                    Player[1] = 8  ## Player is set to the space on the board of "just visiting"
                    jail_counter = 0
                else:
                    continue
        Player[1] += dice_1 + dice_2  ## Computer's space on the board increases by the numbers on the dice
        if Player[1] > 31:  ## if the Player's's space is past the board
            Player[1] -= 31  ## restarts the Player's space to the beginning
            Player[0] += 200  ## Player gets $200 for passing go
            print("You passed Go! and got $200")
        if board[Player[1]] == "Go!":
            print("You landed on Go!")
        elif board[Player[1]] == "Income Tax":
            if 0.1 * Player[0] > 200:  ## If 10% of the Player's money is more than $200
                Player[0] -= 200
                print("You landed on Income Tax and lost $200")
            else:  ## if 10% of the Player's money <= $200
                print("You landed on Income Tax and lost $" + str(0.1 * Player[0]))
                Player[0] -= int(round(0.1 * Player[0]))
        elif board[Player[1]] == "Luxury Tax":
            print("You landed on Luxury Tax and lost $75")
            Player[0] -= 75
        elif board[Player[1]] == "Just Visiting Jail":
            print("You are just vising jail!")
        elif board[Player[1]] == "Free Parking":
            print("You landed on Free Parking!")
        elif board[Player[1]] == "Go To Jail":
            print("You landed on Go To Jail and went to Jail!")
            Player[1] = "Jail"  ## set's Player's place to Jail
        else:
            print("You landed on " + board[Player[1]][
                0])  ## The Player's spot on the board is a property's variable, so it is that property's 0th index
            if board[Player[1]] in Player:  ## If the spot Player landed on is already a property Player owns.
                print("You already own that property!")
                continue
            elif board[Player[1]] in Comp1:  ## If the spot Player landed on is already a property Comp1 owns.
                Player[0] -= Comp1Prop[
                    Comp1.index(board[Player[1]]) - 2]  ## Player gets charged the price of rent which is in Comp1Prop.
                Comp1[0] += Comp1Prop[Comp1.index(board[Player[1]]) - 2]  ## Comp1 gets paid the price of rent
                print("You paid Computer 1 $" + str(Comp1Prop[Comp1.index(board[Player[1]]) - 2]))
                continue
            elif board[Player[1]] in Comp2:  ## If the spot Player landed on is already a property Comp2 owns.
                Player[0] -= Comp2Prop[
                    Comp2.index(board[Player[1]]) - 2]  ## Player gets charged the price of rent which is in Comp2Prop.
                Comp2[0] += Comp2Prop[Comp2.index(board[Player[1]]) - 2]  ## Comp2 gets paid the price of rent
                print("You paid Computer 2 $" + str(Comp2Prop[Comp2.index(board[Player[1]]) - 2]))
                continue
            elif board[Player[1]] in Comp3:  ## If the spot Player landed on is already a property Comp3 owns.
                Player[0] -= Comp3Prop[
                    Comp3.index(board[Player[1]]) - 2]  ## Player gets charged the price of rent which is in Comp3Prop.
                Comp3[0] += Comp3Prop[Comp3.index(board[Player[1]]) - 2]  ## Comp3 gets paid the price of rent
                print("You paid Computer 3 $" + str(Comp3Prop[Comp3.index(board[Player[1]]) - 2]))
                continue
            buy_command = input("Do you want to buy this property? ")
            is_command = 0
            while buy_command.lower() != "yes" and buy_command.lower() != "no":  ## While the Player did not enter "yes" or "no" as their buy_command
                print("That is not a command! Please enter 'yes' or 'no'")
                buy_command = input()
            if buy_command.lower() == "yes":  ## If the Player said "yes"
                Player[0] -= board[Player[1]][2]  ## The Player gets charged the price to buy the property
                Player.append(board[Player[1]])  ## The property itself gets added to the Player's property list
                PlayerProp.append(Player[-1][3])  ## The rent of the Property gets added to the Player's list of rents
                print("You have successfully bought " + Player[-1][0])
                print("You now have $" + str(Player[0]))
                PlayerProp = RailroadChecker(Player, PlayerProp)
                monopoly_color, monopoly_type = monopolyChecker(Player)
                if monopoly_color == board[Player[1]][1]:  ## Checks if the monopoly color that the Player has a monopoly on is the same as the property the Player bought.
                    for x in range(len(Player[2:])):  ## x goes from 1 to the total number of properties the Player has.
                        if Player[x + 2][1] == board[Player[1]][1]:  # Sees if the Property x is scolling though matches the color of the property the Player.
                            PlayerProp[x] = Player[x + 2][4]  # Changes the current rent price of the selected property to the one when there is a monopoly.
        if dice_1 == dice_2:
            if double_counter >= 1 and  repeated >= 2:
                print("You rolled a double twice and have to go to jail!")
                Player[1] = "Jail"  ## set's Player's place to Jail
            else:
                print("You rolled a double, and get to roll again!")
                double_counter += 1
                repeated = 0

    elif command == "mortgage/unmortgage":
        mortgage_command = ""
        if len(Player) < 3:  ## Checks if there are any properties that the player owns.
            print("You do not have any properties to mortgage!")
            continue
        print("What property do you want to mortgage or unmortgage?")
        for x in Player[2:]:  ## Goes through each one of the player's properties, and printing it out.
            print(x[0])
        mortgage_command = input()
        prop = -1
        for x in Player[
                 2:]:  ## Goes through each one of the player's properties and sees if the mortgage command is one of the property's name.
            if mortgage_command == x[0]:  ## If mortgage_command matches the name of one of the properties Player owns
                prop = Player.index(x)  ## The selected property becomes the index in Player
        if prop == -1:  ## If the selected property variable didn't change
            print("That is not a proper command!")
            continue
        if PlayerProp[prop - 2] > Player[prop][4]:  ## If the price of rent is more than that of a monopoly
            print("You cannot mortgage that property because it is built upon! Sell all the buildings to mortgage!")
            print("You need to sell the buildings before you can mortgage that property!")
            continue
        for x in range(len(Player[2:])):  ## x goes from 0 to the length of Player
            if Player[prop][1] == Player[x + 2][1] and PlayerProp[x] > Player[x + 2][
                4]:  ## If the color of Property x matches the color of the selected property and Property x rent is more than monopoly rent.
                print(
                    "You cannot mortgage that property because one of the other properties in the color group is built upon!")
                print("You need to sell the buildings before you can mortgage that property!")
                prop = -1  ## Sets property to an invalid number
        if prop == -1:  ## If the property is an invalid number.
            continue
        if PlayerProp[prop - 2] == 0:  ## If the rent for the selected property is $0
            monopoly_color, monopoly_type = monopolyChecker(Player)
            if Player[prop][
                1] in monopoly_color:  ## If the selected property's is part of one of the Players's monopolies.
                PlayerProp = Player[prop][
                    4]  ## The selected property's rent is set to the price of rent with a monopoly.
            else:
                PlayerProp[prop - 2] = Player[prop][
                    3]  ## The selected property's rent is set to the regular price of rent.
            Player[0] -= Player[prop][-1]  ## Player gets charged for the mortgage
            print("You have successfully unmortgaged your property!")
            print("You now have $" + str(Player[0]))
        else:
            PlayerProp[prop - 2] = 0  ## The rent for the selected property becomes $0
            Player[0] += Player[prop][-2]  ## The Player gets paid back for the mortgage
            print("You have successfully mortgaged your property!")
            print("You now have $" + str(Player[0]))
    elif command == "build/sell":
        build_command = ""
        monopoly_color, monopoly_type = monopolyChecker(Player)
        if monopoly_type == "none":  ## If there is no monopoly
            print("You do not have any monopolies to build on!")
            continue
        elif monopoly_type == "Railroad":  ## If the only monopoly is a railroad
            print("You cannot build on a Railroad!")
            continue
        else:
            print("Do you want to build or sell houses?")
            build_sell = input()
            if build_sell != "build" and build_sell != "sell":  ## If the Player did not enter build or sell.
                print("That is not a proper command!")
                continue
        sell = []
        if build_sell == "build":
            print("What property do you want to build on?")
            for x in Player[
                     2:]:  ## Goes through each one of the player's properties, and printing the ones with monopolies out.
                if x[1] in monopoly_color:  ## If property x is one of the Player's monopolies.
                    print(x[0])
        else:
            for x in range(len(Player[2:])):  ## Goes through each one of the player's properties, and printing it out.
                if Player[x + 2][1] in monopoly_color and PlayerProp[x] != Player[x + 2][
                    4]:  ## Checks to see if the Property is a monopoly, and that it is not going for rent that a normal monopoly would have, so it must have houses.
                    sell.append(Player[x + 2])  ## Adds property x to sell list.
            if len(sell) == 0:  ## if there is nothing in sell list
                print("You have no houses on any of your properties to sell!")
                continue
            print("What property do you want to sell houses on?")
            for x in sell:
                print(x[0])
        build_command = input()
        prop = -1  ## Sets the selected property index to an invalid number
        for x in Player[2:]:  ## x goes through each one of the Player's properties.
            if build_command == x[0]:  ## If build_command is the name of Property x
                prop = Player.index(x)  ## Prop becomes the index of property x
        if prop == -1:  ## If prop is still an invalid number
            print("That is not a proper command!")
            continue
        if build_sell == "build":  ## If the Player wants to build
            print("What do you want to build to?")
            if PlayerProp[prop - 2] == Player[prop][
                -4]:  ## If the price for rent of the selcted property already has 1 hotel
                print("You already built the maximum amount of buildings!")
                continue
            for x in range(Player[prop].index(PlayerProp[prop - 2]) - 3,
                           5):  ## x goes from the number of houses the property has to 5.
                print(str(x) + " houses")
            print("1 hotel")
            build_command = input()
            if build_command[4] == "u":  ## If the Player wanted to build to a house
                Player[0] -= (int(build_command[0]) - (Player[prop].index(PlayerProp[prop - 2]) - 4)) * Player[prop][
                    -3]  ## Player gets chargd the number of houses the player wants minus how many they have already, times price per house
                PlayerProp[prop - 2] = Player[prop][int(build_command[
                                                            0]) + 4]  ## The selected property's rent changes to the rent price for the desired number of houses
            elif build_command[4] == "t":  ## If the player wanted to build to a hotel
                Player[0] -= (5 - (Player[prop].index(PlayerProp[prop - 2])) - 4) * Player[prop][
                    -3]  ## Player gets chargd the hotel minus how many they have already, times price per house
                PlayerProp[prop - 2] = Player[prop][
                    9]  ## The selected property's rent changes to the rent price for a hotel
            else:
                print("That is not a proper command!")
                continue
            print("You successfully built", build_command, "on", Player[prop][0])
            print("You now have $" + str(Player[0]))
        else:
            print("How many houses do you want to keep?")
            for x in range(Player[prop].index(PlayerProp[prop - 2]) - 4, -1,
                           -1):  ## x decends from number of houses the Player has to 0
                print(str(x) + " houses")
            print("None")
            build_command = input()
            if build_command[2] == "h":
                print(Player[prop].index(PlayerProp[prop - 2]))
                Player[0] += ((int(build_command[0]) - (Player[prop].index(PlayerProp[prop - 2]) - 3)) * Player[prop][-3]) / 2
                PlayerProp[prop - 2] = Player[prop][int(build_command[0]) + 4]
                print("You successfully sold", (int(build_command[0]) - (Player[prop].index(PlayerProp[prop - 2]) - 3)), "houses on", Player[prop][0])
                print("You now have $" + str(Player[0]))
            elif build_command.lower() == "none":  ## If the Player does not want to keep any houses
                Player[0] += (((Player[prop].index(PlayerProp[prop - 2]) - 3)) * Player[prop][
                    -3]) / 2  ## Player gets paid the price of all the houses they got times price per house, divided by 2
                PlayerProp[prop - 2] = Player[prop][3]  ## The selected property's rent becomes the regular rent
                print("You successfully sold", (int(build_command[0]) - (Player[prop].index(PlayerProp[prop - 2]) - 3)),
                      "houses on", Player[prop][0])
                print("You now have $" + str(Player[0]))
            else:
                print("That is not a proper command!")
                continue
    elif command == "trade":
        print("Who do you want to trade with?")
        for x in range(3):  ## x goes from 0 to 2
            print("Computer " + str(x + 1))  ## Prints "Computer 1", "Computer 2", "Computer 3"
        trade_command = input()
        Computers = [Comp1, Comp2, Comp3]
        ComputerProp = [Comp1Prop, Comp2Prop, Comp3Prop]
        if trade_command[0:9] != "Computer ":  ## If the Player didn't type "Computer"
            print("That is not a proper command!")
            continue
        elif trade_command[9] != "1" and trade_command[9] != "2" and trade_command[9] != "3":
            print("That is not a proper command!")
            continue
        print("You have $" + str(Player[0]))
        print("You own:")
        for x in Player[2:]:  ## x goes through all of Player's properties
            print(x[0])
        Computer_traded = [Computers[int(trade_command[9]) - 1], trade_command, ComputerProp[int(trade_command[9]) - 1]]  ## Index 0 becomes the Computer Player wants to trade with, Index 1 is the name of the Computer, and Index 2 being the property rents for the Computer
        trade_command = input("How many properties do you want to trade? ")
        try:
            trade_command = int(trade_command)
        except ValueError:
            print("That is not a proper command!")
            continue
        trade_command = int(trade_command)
        if trade_command > len(Player[2:]):  ## If the number of properties the Player wants to trade off exceedes the number of properties the Player owns
            print("You do not have that many properties to trade!")
            continue
        traded_properties = []
        if int(trade_command) > 0:  ## If the Player wants to trade off at least 1 property
            all_properties = 0  ## Counter is set
            while all_properties < int(trade_command):  ## While counter is less than trade_command
                all_properties += 1
                can_trade = 0
                traded_properties.append(input("What property do you want to trade? "))
                prop = -1  ## The selected property becomes an invalid number
                for y in Player[
                         2:]:  ## Goes through each one of the player's properties and sees if the mortgage command is one of the property's name.
                    if traded_properties[-1] == y[0]:  ## If the property the Player wants to trade matches Property y.
                        prop = Player.index(y)  ## The selected property becomes the index of Property y.
                if prop == -1:  ## If the selected property index is still an invalid number
                    can_trade = 1
                elif PlayerProp[prop - 2] > Player[prop][4]:  ## If the price of rent of the selected property is more than the price with a monopoly
                    print("You cannot trade that property because it is built upon! Sell all the buildings to mortgage!")
                    print("You need to sell the buildings before you can trade that property!")
                    can_trade = 1
                else:
                    for y in range(len(Player[2:])):  ## y goes from 0 to the length of the list Player
                        if Player[prop][1] == Player[y + 2][1] and PlayerProp[y] > Player[y + 2][4]:  ## If the selected property group matches the one of Property y and The rent of property y is more than the rent with a monopoly
                            print("You cannot trade that property because one of the other properties in the color group is built upon!")
                            print("You need to sell the buildings before you can trade that property!")
                            can_trade = 1
                if can_trade == 1:  ## If the Player's selected property was at all invalid
                    print("That is not a property!")
                    all_properties -= 1  ## Counter goes down by 1
                    traded_properties.pop(-1)  ## the new index gets removed from the list
                    continue
                for y in Player[2:]:  ## Y goes through all of Player's properties
                    if traded_properties[-1] == y[0]:  ## If the name of the selected property matches Property y:
                        can_trade = 1
                if can_trade == 0:
                    print("That is not a property!")
                    all_properties -= 1  ## Counter goes down by 1
                    traded_properties.pop(-1)  ## the new index gets removed from the list
                    continue
            for x in Player[2:]:  ## X goes through Players properties
                for y in range(len(traded_properties)):  ## y goes through the traded properties
                    if traded_properties[y] == x[0]:  ## If the traded property matches with property x
                        traded_properties.pop(y)  ## The name of the selected property gets removed
                        traded_properties.append(x)  ## The proeprty x gets appended with all its values
            if len(traded_properties) < trade_command:  ## If the list traded_properties is less than the number of properties the Player wanted to trade
                print("That is not a proper commmand!")
                continue
        trade_command = int(input("How much money do you want to trade? $"))
        try:
            trade_command = int(trade_command)
        except ValueError:
            print("That is not a proper command!")
            continue
        trade_command = int(trade_command)
        if trade_command > Player[0]:  ## If the money Player wants to trade is more than the Player has
            print("You don't have enough money!")
            continue
        print(Computer_traded[1] + " has $" + str(Computer_traded[0][0]))
        print(Computer_traded[1] + " owns")
        for x in range(
                len(Computer_traded[0][2:])):  ## x goes through all of the Computer Player wants to trade's properties
            if Computer_traded[2][x] <= Computer_traded[0][x + 2][4]:
                print(Computer_traded[0][x + 2][0])
        want_command = input("How many properties do you want from " + Computer_traded[1] + "? ")
        try:
            want_command = int(want_command)
        except ValueError:
            print("That is not a proper command!")
            continue
        want_command = int(want_command)
        if want_command > len(Computer_traded[0][2:]):  ## If the number of properties the Player wants to trade off exceedes the number of properties the Player owns
            print(Computer_traded[1] + " does not have that many properties to trade!")
            continue
        wanted_properties = []
        if want_command > 0:  ## If the Player wants at least 1 property from Computer
            all_properties = 0  ## Counter is set
            while all_properties < int(want_command):  ## While counter is less than trade_command
                all_properties += 1
                can_trade = 0
                wanted_properties.append(input("What property do you want? "))
                prop = -1  ## The selected property becomes an invalid number
                for y in Computer_traded[0][
                         2:]:  ## Goes through each one of the player's properties and sees if the mortgage command is one of the property's name.
                    if wanted_properties[-1] == y[0]:  ## If the property the Player wants to trade matches Property y.
                        prop = Computer_traded[0].index(y)  ## The selected property becomes the index of Property y.
                if prop == -1:  ## If the selected property index is still an invalid number
                    can_trade = 1
                else:
                    for y in range(len(Computer_traded[0][2:])):  ## y goes from 0 to the length of the list Player
                        if Computer_traded[0][prop][1] == Computer_traded[0][y + 2][1] and Computer_traded[2][y] > \
                                Computer_traded[0][y + 2][4]:  ## If the selected property group matches the one of Property y and The rent of property y is more than the rent with a monopoly
                            print("You cannot get that property because one of the other properties in the color group is built upon!")
                            print(Computer_traded[1] + " needs to sell the buildings before you can get that property!")
                            can_trade = 1
                if can_trade == 1:  ## If the Player's selected property was at all invalid
                    print("That is not a property!")
                    all_properties -= 1  ## Counter goes down by 1
                    wanted_properties.pop(-1)  ## the new index gets removed from the list
                    continue
                for y in Computer_traded[0][2:]:  ## Y goes through all of Player's properties
                    if wanted_properties[-1] == y[0]:  ## If the name of the selected property matches Property y:
                        can_trade = 1
                if can_trade == 0:
                    print("That is not a property!")
                    all_properties -= 1  ## Counter goes down by 1
                    wanted_properties.pop(-1)  ## the new index gets removed from the list
                    continue
            for x in Computer_traded[0][2:]:  ## X goes through Computers properties
                for y in range(len(wanted_properties)):  ## y goes through the wanted properties
                    if wanted_properties[y] == x[0]:  ## If the wanted property matches with property x
                        wanted_properties.pop(y)  ## The name of the selected property gets removed
                        wanted_properties.append(x)  ## The proeprty x gets appended with all its values
            if len(wanted_properties) < want_command:  ## If the list wanted_properties is less than the number of properties the Player wanted to trade
                print("That is not a proper commmand!")
                continue
        want_command = int(input("How much money do you want? "))
        try:
            want_command = int(want_command)
        except ValueError:
            print("That is not a proper command!")
            continue
        want_command = int(want_command)
        if want_command > Computer_traded[0][0]:  ## Player wants more money than Computer has
            print(Computer_traded[1] + " doesn't have enough money!")
            continue
        total_traded = trade_command
        total_wanted = want_command
        for x in traded_properties:  ## x goes through all the properties Player wants to trade
            total_traded += 2 * x[-1]  ## 2 times the unmortgage rate of Property x gets added to total_traded
        for x in wanted_properties:  ## x goes through all the properties Player wants
            total_wanted += 2 * x[-1]  ## 2 times the unmortgage rate of Property x gets added to total_wanted
        if total_traded >= total_wanted:  ## If the Player is giving more than or equal to what is requested
            print("You have successfully traded with " + Computer_traded[1])
            Computer_traded[0][0] += trade_command  ## Computer gets all the money Player offered
            Player[0] += want_command ## Player gets all the money they wanted
            Player[0] -= trade_command
            Computer_traded[0][0] -= want_command
            for x in range(len(traded_properties)):  ## x goes from 0 to the length of traded_properties
                PlayerProp.pop(
                    Player.index(traded_properties[x]) - 2)  ## Removes the rent price of the selected property
                Player.pop(Player.index(traded_properties[x]))  ## Property x gets taken from Player
                Computer_traded[2].append(traded_properties[x][3])  ## Adds the rent price of the selected property
                Computer_traded[0].append(traded_properties[x])  ## Computer gets Property x
            for x in range(len(wanted_properties)):  ## x goes from 0 to the length of wanted_properties
                Computer_traded[2].pop(Computer_traded[0].index(wanted_properties[x]) - 2)
                Computer_traded[0].pop(
                    Computer_traded[0].index(wanted_properties[x]))  ## Property x gets taken from Player
                Player.append(wanted_properties[x])  ## Computer gets Property x
                PlayerProp.append(wanted_properties[x][3])  ## Adds the rent price of the selected property
        else:  ## If the Player is requesting more than giving
            print(Computer_traded[1] + " declined the trade!")
            continue
        PlayerProp = RailroadChecker(Player, PlayerProp)
    elif command == "end turn" and repeated == 1:
        repeated = 0
        Comp1Prop, Player, Comp1, Comp2, Comp3, Comp1 = ComputerPlays(Comp1, Comp1Prop, board, Player, PlayerProp, Comp1, Comp1Prop, Comp2, Comp2Prop, Comp3, Comp3Prop, "1")
        Comp2Prop, Player, Comp1, Comp2, Comp3, Comp2 = ComputerPlays(Comp2, Comp2Prop, board, Player, PlayerProp, Comp1, Comp1Prop, Comp2, Comp2Prop, Comp3, Comp3Prop, "2")
        Comp3Prop, Player, Comp1, Comp2, Comp3, Comp3 = ComputerPlays(Comp3, Comp3Prop, board, Player, PlayerProp, Comp1, Comp1Prop, Comp2, Comp2Prop, Comp3, Comp3Prop, "3")
    else:
        print("That is not a proper command!")
    print("You own:")
    for x in Player[2:]:
        print("    " + x[0])
    print("    You have $" + str(Player[0]))
    print("Computer 1 owns:")
    for x in Comp1[2:]:
        print("    " + x[0])
    print("    Computer 1 has $" + str(Comp1[0]))
    print("Computer 2 owns:")
    for x in Comp2[2:]:
        print("    " + x[0])
    print("    Computer 2 has $" + str(Comp2[0]))
    print("Computer 3 owns:")
    for x in Comp3[2:]:
        print("    " + x[0])
    print("    Computer 3 has $" + str(Comp3[0]))


