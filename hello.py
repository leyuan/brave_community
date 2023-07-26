import pandas as pd


class Player:
    def __init__(self, gems={}, cards=[]):
        self.gems = gems
        self.cards = cards


green_card = {'W': 3, 'G': 6, 'R': 1, 'B': 4}


def can_purchase(p: Player, c: dict) -> bool:
    # for each color of the card, we check the player has enough gems of this color
    # if yes -> keep checking till the end
    # if no -> return False

    for color in c:
        p_gems = p.gems.get(color, 0)

        if p_gems < c[color]:
            return False

        return True


def purchase(p: Player, c: dict) -> bool:
    if can_purchase(p, c):
        for color in c:
            p.gems[color] = p.gems[color] - c[color]

        p.cards.append(c)
        return True
    else:
        return False


rich_guy = Player(gems={'W': 1000, 'G': 1000, 'R': 1000, 'B': 1000,
                  'Y': 1000, 'Y': 1000, 'Y': 1000, 'Y': 1000}, cards=[])

assert can_purchase(rich_guy, green_card) == True

print("Done")
print("New Feature")
