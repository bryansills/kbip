from domknow import *

def useStrategicKnowledge(board, side):
    options = winningSpots(board, side)
    if len(options) != 0:
        return (choice(options), "This spot wins the game.")

    options = openSpots(board, side)
    if len(options) != 0:
        return (choice(options), "This spot is available.")
