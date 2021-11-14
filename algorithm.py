# takes in the nft hash, returns the stats for it in the form [ATK, DEF, HP, TYPE]
# hash must be at least 7 characters long, including the 0xe at the start
def get_stats(hash):
    if len(hash) < 7:
        return None
    else:
        stats = []
        last_digits = hash[len(hash)-4:]
        for char in last_digits:
            stats.append(get_stat(char))
        return stats

# computes the stat for a single character in the hash
def get_stat(stat):
    if stat.isnumeric():
        return 100 - stat**2
    elif stat.isalpha():
        return abs(ord(stat)**2-100**2) + 1
    else:
        return -1