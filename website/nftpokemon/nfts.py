import requests, json, random, os

#rather than get a random list of all nfts we just pull from a few popular colections for simplicity
#this feature would be accounted for in a final version
addresses = [
    '0x60e4d786628fea6478f785a6d7e704777c86a7c6',
    '0xe4605d46fd0b3f8329d936a8b258d69276cba264',]


#Input
#   -address - a crypto collection address with nfts on opensea
#Output
#   returns a json object containing a list of nft token ids
def update_nft_token_ids():
    for address in addresses:
        body = requests.get('https://api.covalenthq.com/v1/1/tokens/' + address + '/nft_token_ids/?key=ckey_644cc507cd5946cb82e4c1e96e5').json()
        f = open(address + '.json', 'w', encoding='utf-8')
        json.dump(body, f, ensure_ascii=False, indent=4)

#Input
#   -address - a crypto collection address with nfts on opensea
#Output
#   returns a json object containing a list of nft token ids
def load_nft_token_ids(address):
    f = open('nftpokemon/' + address + '.json', 'r', encoding='utf-8')
    return json.load(f)

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
    address = addresses[1]
    collection = load_nft_token_ids(address)                                                # returns a list of all tokens for a given randomized collection from our list
    token = random.randrange(int(collection['data']['pagination']['total_count']))          # random token_id out of the collection

    #print("Grabbing nft " + str(token) + "/" + str(collection['data']['pagination']['total_count']) + " from collection of address " + str(address))
    
    nft = get_nft_metadata(address, token)                                                  #gets nft data for token id
    
    #print(json.dumps(nft['data']['items'][0]['nft_data'][0]['external_data'], indent=4))
    
    name = nft['data']['items'][0]['nft_data'][0]['external_data']['name']
    image = nft['data']['items'][0]['nft_data'][0]['external_data']['image_512']

    transactions = get_nft_transactions(address, token)        
    hash = transactions['data']['items'][0]['nft_transactions'][0]['tx_hash']               # gets hash for original minting
    
    result = {'name': name, 'token': token, 'image':image, 'hash': hash}
    return result
