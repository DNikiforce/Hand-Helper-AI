import eval7
import random

def calculate_equity_and_outs(hand, board, num_opponents=1, iterations=1000):
    deck = eval7.Deck()

    # Конвертируем строки в eval7.Card
    hero = [eval7.Card(card) for card in hand]
    known = hero + [eval7.Card(card) for card in board]

    for card in known:
        deck.cards.remove(card)

    wins = 0
    for _ in range(iterations):
        deck.shuffle()

        # Генерация рук оппонентов
        opps = [[deck.peek(i*2), deck.peek(i*2+1)] for i in range(num_opponents)]

        # Заполнение доски
        community_needed = 5 - len(board)
        community = [deck.peek(2 * num_opponents + i) for i in range(community_needed)]

        # Формируем полные руки
        hero_hand = hero + community
        opp_hands = [opp + community for opp in opps]

        hero_val = eval7.evaluate(hero_hand)
        best_opp = max(eval7.evaluate(h) for h in opp_hands)

        if hero_val > best_opp:
            wins += 1
        elif hero_val == best_opp:
            wins += 0.5

    return round(100 * wins / iterations, 1), "?"
