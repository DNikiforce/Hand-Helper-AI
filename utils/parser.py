def parse_card(card_emoji):
    ranks = {'A': 'A', 'K': 'K', 'Q': 'Q', 'J': ' 'J', 'T': 'T', '9': '9',
             '8': '8', '7': '7', '6': '6', '5': '5', '4': '4', '3': '3', '2': '2'}
    suits = {'♠': 's', '♥': 'h', '♦': 'd', '♣': 'c'}
    rank, suit = card_emoji[:-1], card_emoji[-1]
    return ranks.get(rank, rank), suits.get(suit, suit)

def parse_hand(line):
    cards = line.strip().replace("PF:", "").split()
    return [parse_card(card) for card in cards]

def parse_board(line):
    cards = line.strip().split()[1:]
    return [parse_card(card) for card in cards]