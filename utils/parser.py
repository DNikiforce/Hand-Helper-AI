emoji_to_card = {
    "🂡": "As", "🂢": "2s", "🂣": "3s", "🂤": "4s", "🂥": "5s", "🂦": "6s",
    "🂧": "7s", "🂨": "8s", "🂩": "9s", "🂪": "Ts", "🂫": "Js", "🂭": "Qs", "🂮": "Ks",
    "🂱": "Ah", "🂲": "2h", "🂳": "3h", "🂴": "4h", "🂵": "5h", "🂶": "6h",
    "🂷": "7h", "🂸": "8h", "🂹": "9h", "🂺": "Th", "🂻": "Jh", "🂽": "Qh", "🂾": "Kh",
    "🃑": "Ac", "🃒": "2c", "🃓": "3c", "🃔": "4c", "🃕": "5c", "🃖": "6c",
    "🃗": "7c", "🃘": "8c", "🃙": "9c", "🃚": "Tc", "🃛": "Jc", "🃝": "Qc", "🃞": "Kc",
    "🃁": "Ad", "🃂": "2d", "🃃": "3d", "🃄": "4d", "🃅": "5d", "🃆": "6d",
    "🃇": "7d", "🃈": "8d", "🃉": "9d", "🃊": "Td", "🃋": "Jd", "🃍": "Qd", "🃎": "Kd",
}

suit_map = {
    "♠": "s", "♥": "h", "♦": "d", "♣": "c",  # Unicode
    "S": "s", "H": "h", "D": "d", "C": "c",  # Text uppercase
    "s": "s", "h": "h", "d": "d", "c": "c"   # ✅ добавлено
}

valid_ranks = {"A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"}


def parse_card(symbol):
    symbol = symbol.strip().replace("️", "")
    if symbol in emoji_to_card:
        return emoji_to_card[symbol]
    if len(symbol) == 2:
        rank = symbol[0].upper()
        suit = symbol[1]
        if rank in valid_ranks and suit in suit_map:
            return rank + suit_map[suit]
    return None


def parse_hand(line):
    parts = line.strip()[3:].split()
    parsed = [parse_card(p) for p in parts if parse_card(p)]
    if len(parsed) != 2:
        return []
    return parsed


def parse_board(line):
    parts = line.strip().split()[1:]
    return [parse_card(p) for p in parts if parse_card(p)]
