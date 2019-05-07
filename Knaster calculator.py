# hardcoded example data
data = {
    "Piano": {"John":15, "Paul":20, "George":5, "Ringo":10},
    "Guitar": {"John":25, "Paul":20, "George":15, "Ringo":5},
    "Drums": {"John":15, "Paul":20, "George":5, "Ringo":30},
    "Bass": {"John":20, "Paul":30, "George":5, "Ringo":20}
}


# main function for performing the Knaster Inheiritance algorithm
def knaster():
    assets = initial_winners()
    print(assets)
    fair_shares = {}
    kitty = 0
    
    
    
    
# helper function for knaster()
# for object in data, find the highest bidder, and return a list of
# items in the format of winners = [{"asset1:"heir1"}, {"asset2":"heir2"}...etc]
def initial_winners():   
    winners = []

    for item in data:
        winner = {}
        highest_bid = 0
        current_item = data[item]
        for x in current_item:
            bid = current_item[x]
            if bid > highest_bid:
                highest_bid = bid
                winner[x] = current_item
        winners.append(winner)
    return winners





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











