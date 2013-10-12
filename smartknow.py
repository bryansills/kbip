from domknow import *

def useStrategicKnowledge(board, side):
    options = winningSpots(board, side)
    if len(options) != 0:
        return (choice(options), "This spot wins the game")

    options = blockLosingSpots(board, side)
    if len(options) != 0:
        return (choice(options), "This spot blocks the opponent")

    options = oppositeCornerSpots(board, side)
    if len(options) != 0:
        return (choice(options), "This spot is opposite of a corner you already claimed")

    options = cornerSpots(board, side)
    if len(options) != 0:
        return (choice(options), "This spot is a corner spot")

    options = openSpots(board, side)
    if len(options) != 0:
        return (choice(options), "This spot is available")