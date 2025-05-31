import eval7
import random

def calculate_equity_and_outs(hand, board, num_opponents=1, iterations=1000):
    deck = eval7.Deck()
    hero = [eval7.Card(f"{r}{s}") for r, s in hand]
    known = hero + [eval7.Card(f"{r}{s}") for r, s in board]
    for card in known:
        deck.cards.remove(card)

    wins = 0
    for _ in range(iterations):
        deck.shuffle()
        opps = [[deck.peek(i*2), deck.peek(i*2+1)] for i in range(num_opponents)]
        community = board + [(r,s) for r, s in [(deck.peek(2*num_opponents+i).rank, deck.peek(2*num_opponents+i).suit) for i in range(5-len(board))]]
        hero_hand = hero + [eval7.Card(f"{r}{s}") for r,s in community]
        opp_hands = [[card for card in opp] + [eval7.Card(f"{r}{s}") for r,s in community] for opp in opps]

        hero_val = eval7.evaluate(hero_hand)
        best_opp = max(eval7.evaluate(h) for h in opp_hands)
        if hero_val > best_opp:
            wins += 1
        elif hero_val == best_opp:
            wins += 0.5

    return round(100 * wins / iterations, 1)
