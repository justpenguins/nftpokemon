# takes in the nft hash, returns the stats for it in the form [ATK, DEF, HP, TYPE]
# hash must be at least 7 characters long, including the 0xe at the start
def get_stats(hash):
    if len(hash) < 7:
        return None
    else:
        stats = []
        i = 0
        last_digits = hash[len(hash)-4:]
        for char in last_digits:
            if i == 3:
                stats.append(get_type(char))
            else:
                stats.append(get_stat(char))
            i += 1
        return stats

# computes the stat for a single character in the hash
def get_stat(stat):
    if stat.isdecimal():
        return 100 - int(stat)**2
    elif stat.isalpha():
        return abs(ord(stat)**2-100**2) + 1
    else:
        return -1

# computes the type for the given character in the hash
def get_type(stat):
    if stat.isdecimal():
        type = 100 - int(stat)**2
        if type > 90:
            return "FIRE"
        elif type > 60:
            return "WATER"
        else:
            return "WOOD"
    elif stat.isalpha():
        type = ord(stat)
        if type < 106:
            return "FIRE"
        elif type < 115:
            return "WATER"
        else:
            return "WOOD"
    else:
        return "NULL"
