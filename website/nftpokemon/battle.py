from .algorithm import get_stats

# player1 attacks player2
def attack(p1, p2):
    p2.hp -= p1.hp
        
# one battle round, pass in two Players, the player and the enemy
def round(player_id, enemy_id):
    player = Player(player_id)
    enemy = Player(enemy_id)
    print(player)
    print(enemy)
    turn = 1 # enemy starts
    while (player.hp > 0 and enemy.hp > 0):
        if turn % 2 == 1: # player attacks
            attack(player, enemy)
        else: # enemy attacks
            attack(enemy, player)
        turn = turn + 1
    
    if player.hp > 0:
        return "Player Wins"
    else:
        return "Enemy Wins"


class Player:
    hp = 0
    atk = 0
    defence = 0
    typ = ""

    def __str__(self):
        return "HP: " + str(self.hp) + " atk: " + str(self.atk) + " def: " + str(self.defence) + " type: " + self.type

    def __init__(self, hash):
        stats = get_stats(hash)
        self.hp = stats[0]
        self.atk = stats[1]
        self.defence = stats[2]
        self.type = stats[3]