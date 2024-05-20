import random

def go(players):
    paired = []
    gifted = { player: False for player in players}
    recieved = { player: False for player in players}
    for player in players:
        if gifted[player] == False:
            reciever = [ele for ele in players if ele != player and recieved[ele] == False][-1]
            paired.append([player, reciever])
            gifted[player] = True
            recieved[reciever] = True
    return paired

players = [
    "Freya",
    "Tom",
    "Jess",
    "Maya",
    "Sam"
]

print(go(players))
