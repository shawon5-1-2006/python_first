shawon = input("Are you play the game[yes/no]:")
if (shawon == "yes"):
    print("Enjoy the game")
    shawon = input("You go to cave or forest[cave/forest]:")
    if (shawon == "forest"):
        print("You see the hunry taiger and game ober")
    elif (shawon == "cave"):
        print("Good job! Ran the game")
        shawon = input("Yor see the bear are you ran or fight[ran/fight]:")
        if (shawon == "fight"):
            print("Bear is a very storing, fnise the game")
        elif (shawon == "ran"):
            print("write dicition! Engoy this game")
            shawon = input("Two road! selet one road or two road[one road/two road]:")
            if (shawon == "one road"):
                print("Your dicition is rang")
            elif (shawon == "two road"):
                print("Wow! excellent")
                shawon = input("You see the rever, you use nouka or car[nouka/car]:")
                if (shawon == "car"):
                    print("car is not perfect and loss the game")
                elif (shawon == "nouka"):
                    print("Osomoy! Good work")
                    shawon = input("You see the three cave! You go one/two/three cave[one/two/three]:")
                    if (shawon == "one"):
                        print("You see the big sneaks and game over")
                    elif (shawon == "two"):
                        print("you see the big hol and road finise")
                    elif (shawon == "three"):
                        print("The road is old raj mohole")
                        shawon = input("You open raj mohola door and see some spider man. You fighat or back to home[fight/back]:")
                        if (shawon == "back"):
                            print("You loss the game")
                        elif (shawon == "fight"):
                            print("Good,,, fighting you are wine")
                            shawon = input("Go to raj mohole sonetime surces and pay the gold \n WOW! you wine the game")


elif (shawon == "no"):
    print("OUT THE GAME")