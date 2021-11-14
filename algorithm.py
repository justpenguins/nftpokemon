def get_stats(hash):
    if len(hash) < 8:
        return None
    else:
        stats = []
        last_digits = hash[len(hash)-4:]
        for char in last_digits:
            stats.append(get_stat(char))
        return stats

def get_stat(stat):
    if stat.isnumeric():
        return 100 - stat**2
    elif stat.isalpha():
        return abs(ord(stat)**2-100**2) + 1
    else:
        return -1