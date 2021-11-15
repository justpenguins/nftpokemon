from algorithm import *


class Battle:
    # player hash1 attacks hash2
    def attack(hash1, hash2):
        hash1.player_hp -= hash2.player_atk
        
    # one battle round, pass in two Players, the player and the enemy
    def round(player_id, enemy_id):
        battle = Battle()
        player = get_stats(player_id)
        enemy = get_stats(enemy_id)
        player_hp = player[2]
        enemy_hp = enemy[2]
        turn = 0 # enemy starts
        while (enemy_hp > 0 and player_hp > 0):
            if turn == 1: # player attacks
                battle.attack(player_id, enemy_id)
            else: # enemy attacks
                battle.attack(enemy_id, player_id)


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

    

