import requests, json, random

#rather than get a random list of all nfts we just pull from a few popular colections for simplicity
#this feature would be accounted for in a final version
addresses = [
    '0xe4605d46fd0b3f8329d936a8b258d69276cba264',
    '0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb',]

#Input
#   -address - a crypto collection address with nfts on opensea
#Output
#   returns a json object containing a list of nft token ids
def get_nft_token_ids(address):
    return requests.get('https://api.covalenthq.com/v1/1/tokens/' + address + '/nft_token_ids/?key=ckey_644cc507cd5946cb82e4c1e96e5').json()

#Input
#   -address - a crypto collection address with nfts on opensea
#   -token_id - which token in the list of tokens for a given collection
#Output
#   returns a json object containing a list of nft token ids
def get_nft_transactions(address, token_id):
    return requests.get('https://api.covalenthq.com/v1/1/tokens/' + address + '/nft_transactions/' + str(token_id) + '/?key=ckey_644cc507cd5946cb82e4c1e96e5').json()

#Input
#   -address - a crypto collection address with nfts on opensea
#   -token_id - which token in the list of tokens for a given collection
#Output
#   returns a json object containing a list of nft token ids
def get_nft_metadata(address, token_id):
    return requests.get('https://api.covalenthq.com/v1/1/tokens/' + address + '/nft_metadata/' + str(token_id) + '/?key=ckey_644cc507cd5946cb82e4c1e96e5').json()

#Input
#   none
#Output
#   returns an object for an nft with its name, image link, and original minting hash
def get_random_nft():
    collection = get_nft_token_ids(addresses[random.randrange(len(addresses))])         # returns a list of all tokens for a given randomized collection from our list
    r = random.randrange(int(collection['data']['pagination']['total_count']))          # random token_id out of the collection
    
    nft = get_nft_metadata(addresses[0], r)                                             #gets nft data for token id
    name = nft['data']['items'][0]['nft_data'][0]['external_data']['name']
    image = nft['data']['items'][0]['nft_data'][0]['external_data']['image']

    transactions = get_nft_transactions(addresses[0], r)        
    hash = transactions['data']['items'][0]['nft_transactions'][0]['tx_hash']           # gets hash for original minting
    
    result = {'name': name, 'image':image, 'hash': hash}
    return result
