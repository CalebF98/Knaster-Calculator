# hardcoded example data
data = {
    "John": {"Guitar": 40, "Piano": 30, "Bass": 5, "Drums": 15},
    "Paul": {"Guitar": 10, "Piano": 30, "Bass": 35, "Drums": 5},
    "George": {"Guitar": 50, "Piano": 5, "Bass": 5, "Drums": 5},
    "Ringo": {"Guitar": 15, "Piano": 15, "Bass": 15, "Drums": 35},
}

class Asset:
    def __init__(self, name, owner, value):
        this.name = name
        this.owner = owner
        this.value = value

    

class Heir:
    def __init__(self, name, bids):
        self.name = name
        self.bids = bids
        self.assets = []





# main function for performing the Knaster Inheiritance algorithm
def knaster():
    # create initial list of Heirs
    heirs = []
    for key, value in data.items():
        current_heir = Heir(key, value)
        heirs.append(current_heir)

    initial_winners(heirs)
    

    
    
# helper function for knaster()
def initial_winners(list_of_heirs):
    winners = {}
    
    # create a list of items to iterate over,
    # using the 0th heir from list_of_heirs
    items = []
    first_bidder = list_of_heirs[0].bids
    for item in first_bidder:
        items.append(item)



'''
TODO: Right now, the alogrithm fails on the piano item, because the second bid
      is the same value as bid 1. Fix the algorithm so it always chooses
      exactly one winner
'''
    # iterate through each asset, and assign it to the heir that bid the highest
    for item in items:
        highest_bidder = first_bidder[item]
        for heir in list_of_heirs:
                
            # if the current bid is greater than the highest_bidder,
            # create a new entry in the winners dictionary,
            # EX: winners = {'Ringo': {'Drums': 35}, 'George': {'Guitar': 50}}
            if heir.bids[item] > highest_bidder:
                highest_bidder = heir.bids[item]
                winners[item] = [heir.name, heir.bids[item]]

    # create new Asset for each item, and append that Assset
    # to the assets (list) property of its owner

knaster()







### implement this later, once the knaster function works
'''

# initialize lists to create the dictionary from
items = []
heirs = []


# prompt user for the names of heirs and assets to be distributed
def get_data():
    print("Input the heirs to which the assets are being distributed: ")
    print("  (Type 'end' when finished inputing names)")
    while True:
        name = input("Name: ")
        if name == "end":
            break
        else:
            heirs.append(name)
    print()

# prompt user for the list of assets that are being distributed to the heirs
    print("Input the assets to be distributed: ")
    print("   (Type 'end' when finished inputing names)")
    while True:
          asset = input("Item: ")
          if asset == "end":
              break
          else:
              items.append(asset)
    print()
    
    return
'''











