def recommend_bet(equity, street, is_multi, position):
    if street == 'flop':
        if is_multi:
            return "чек или 1/3"
        if equity > 70:
            return "2/3"
        elif equity > 50:
            return "1/2"
        else:
            return "чек"
    elif street == 'turn':
        if equity > 80:
            return "2/3 или пуш"
        elif equity > 50:
            return "1/2"
        else:
            return "чек или фолд"
    elif street == 'river':
        if equity > 90:
            return "пуш"
        elif equity > 60:
            return "2/3"
        else:
            return "чек или фолд"
    return "чек"
