from algorithm import *


class Battle:
    playerHP = 0 
    enemyHP = 0
    animations = []

    # player hash1 attacks hash2
    def attack(hash1, hash2):
        hp1 = hash1.get_hp()
        hp2 = hash2.get_hp()

    def round():
        while (enemyHP > 0 and playerHP > 0):
            if turn == 1: # player attacks
                attack(player, enemy)
            else:         # enemy attacks
                attack(enemy, Player)


class Player:
    player_id = "0xe"
    player_hp, player_atk, player_def = 0
    player_type = ""

    def __init__(self, hash):
        stats = get_stats(hash)
        self.player_id = hash
        self.player_hp = stats[0]
        self.player_atk = stats[1]
        self.player_def = stats[2]
        self.player_type = stats[3]

    def get_id():
        return player_id

    def get_hp():
        return player_hp
    
    def get_atk():
        return player_atk

    def get_def():
        return player_def

    def get_type():
        return player_type

    

