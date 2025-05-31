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
        allowed = ["TAG", "FISH", "LAG", "NIT", "MANIAC"]
        opp_type = opp_type.strip().upper()
        if opp_type in allowed:
            self.opponent_type = opp_type

    def add_board_cards(self, cards):
        self.board.extend(cards)

    def reset_board(self):
        self.board = []

class GameSessionManager:
    def __init__(self):
        self.sessions = {}

    def get(self, user_id: int) -> SessionContext:
        if user_id not in self.sessions:
            self.sessions[user_id] = SessionContext()
        return self.sessions[user_id]

# ⬇️ Добавь вот эту строку в конце!
session_manager = GameSessionManager()
