import random

# Constants
NUM_TEAMS = 5
NUM_PLAYERS = 100
BUDGET = 100
MIN_PLAYERS = 20
MAX_PLAYERS = 25
BASE_PRICE = 20  # in lakhs
MAX_BID = 150  # in lakhs
BID_INCREMENT = 10  # in lakhs

# Generate players with base price of 20 lakhs
players = [{'id': i + 1, 'price': BASE_PRICE} for i in range(NUM_PLAYERS)]

# Teams initialization
teams = [{'id': i + 1, 'budget': BUDGET * 100, 'players': []} for i in range(NUM_TEAMS)]  # Budget in lakhs

# Auction logic
def auction():
    available_players = players.copy()
    random.shuffle(available_players)

    for player in available_players:
        print(f"Player {player['id']} is up for auction with a base price of {player['price']} lakhs.")
        bids = []

        for team in teams:
            # Teams decide to bid if they have enough budget and room for players
            if team['budget'] >= player['price'] and len(team['players']) < MAX_PLAYERS:
                bid = input(f"Team {team['id']}, do you want to raise the bid for Player {player['id']}? (yes/no): ").strip().lower()
                if bid == 'yes':
                    bids.append(team)

        if not bids:
            print(f"Player {player['id']} is unsold.")
            continue

        # Increment price by 10 lakhs for each bid
        while len(bids) > 1:
            player['price'] += BID_INCREMENT
            print(f"Player {player['id']} price increased to {player['price']} lakhs due to bidding.")
            print("Remaining budgets:")
            for team in teams:
                print(f"Team {team['id']}: {team['budget']} lakhs")
            
            new_bids = []

            for team in bids:
                if team['budget'] >= player['price'] and player['price'] <= MAX_BID:
                    bid = input(f"Team {team['id']}, do you want to continue bidding? (yes/no): ").strip().lower()
                    if bid == 'yes':
                        new_bids.append(team)

            bids = new_bids

        # Finalize the sale
        if bids:
            winning_team = bids[0]
            winning_team['budget'] -= player['price']
            winning_team['players'].append(player)
            print(f"Team {winning_team['id']} bought Player {player['id']} for {player['price']} lakhs.")
            print("Remaining budgets after purchase:")
            for team in teams:
                print(f"Team {team['id']}: {team['budget']} lakhs")

# Determine the winner
def determine_winner():
    winners = []
    max_budget = -1

    for team in teams:
        if len(team['players']) >= MIN_PLAYERS:
            if team['budget'] > max_budget:
                winners = [team]
                max_budget = team['budget']
            elif team['budget'] == max_budget:
                winners.append(team)

    return winners

# Run the auction
auction()

# Display results
print("\nAuction Results:")
for team in teams:
    print(f"Team {team['id']} - Players: {len(team['players'])}, Remaining Budget: {team['budget']} lakhs")

# Announce the winner
winners = determine_winner()
if len(winners) == 1:
    print(f"\nThe winner is Team {winners[0]['id']} with {winners[0]['budget']} lakhs remaining.")
else:
    print("\nIt's a tie between the following teams:")
    for winner in winners:
        print(f"Team {winner['id']} with {winner['budget']} lakhs remaining.")
