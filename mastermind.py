#Kevin Tu
#Lea Albano
#Kenny dang
#Aditya Shah

from logic import *
from turtle import pos
from re import A

#colors in position and then the people into the houses

colors = ["red", "blue", "green", "purple"]
positions = ["0","1","2","3"]

symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# A color has a pos
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

#one pos per color
for color in colors:
    for position in positions:
        for position2 in positions:
            if position != position2:
                knowledge.add(
                    Implication(Symbol(f"{color}{position}"), Not(Symbol(f"{color}{position2}")))
                )


#red(0,1) implies that if there is a  red is pos 0, then red is NOT in pos 1


#one color per pos
for position in positions:
    for color in colors:
        for color2 in colors:
            if color != color2:
                knowledge.add(
                    Implication(Symbol(f"{color}{position}"), Not(Symbol(f"{color2}{position}")))
                )


# First Guess (Red, Blue, Green, Purple)
#Two colors representing that they are in order
knowledge.add(
    Or(
    And(Symbol("red0"),(Symbol("blue1"))),#red and blue/blue and red
    And(Symbol("red0"),(Symbol("green2"))),#red and green/green and red
    And(Symbol("red0"),(Symbol("purple3"))),#red and purple/purple and red
    And(Symbol("blue1"),(Symbol("green2"))),#blue and green/green and blue
    And(Symbol("blue1"),(Symbol("purple3"))),#blue and purple/purple and blue
    And(Symbol("green2"),(Symbol("purple3"))),#green and purple/purple and green
    )
)


# Second Guess (Blue, Red, Green, Purple)
#not one option in order
knowledge.add(
    And(
    Not((Symbol("blue0"))),
    Not((Symbol("red1"))),
    Not((Symbol("green2"))),
    Not((Symbol("purple3"))),
    )
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)


#output
#red0
#blue1
#purple2
#green3