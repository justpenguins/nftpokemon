from algorithm import get_stats, get_stat, get_type


class Battle:
    playerHP = 0 
    enemyHP = 0
    playerAtk = 0
    enemyAtk = 0
    animations = []

    def __init__(self, php, ehp, patk, eatk):
        self.playerHP = php
        self.enemyHP = ehp
        self.playerAtk = patk
        self.enemyAtk = eatk

    # player hash1 attacks hash2
    def attack(hash1, hash2):
        atk = hash1.get_atk()
        hp = hash2.get_hp()

        hp = hp - atk
            

    def round(enemyHP, playerHP):
        turn = 0
        while (enemyHP > 0 and playerHP > 0):
            if turn == 1: # player attacks
                attack(player, enemy)
                turn = 0
            else:         # enemy attacks
                attack(enemy, player)
                turn = 1



class Player:
    player_id = "0xe"
    player_hp, player_atk, player_def = 0
    player_type = ""

    def __init__(self, hashid):
        stats = get_stats(hashid)
        self.player_id = hashid
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

    

