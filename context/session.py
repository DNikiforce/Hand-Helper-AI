class SessionContext:
    def __init__(self):
        self.reset()

    def reset(self):
        self.hand = None
        self.position = None
        self.opponent_type = None
        self.is_multi = False
        self.multi_count = 0
        self.board = []
        self.street = 'preflop'

    def set_hand(self, hand):
        self.hand = hand

    def set_position(self, pos):
        if 'multi' in pos.lower():
            self.is_multi = True
            parts = pos.split()
            if len(parts) > 1 and parts[1].isdigit():
                self.multi_count = int(parts[1])
        else:
            self.position = pos
            self.is_multi = False

    def set_opponent(self, opp_type):
        if not self.is_multi:
            self.opponent_type = opp_type

    def add_board_cards(self, cards):
        self.board.extend(cards)

    def reset_board(self):
        self.board = []