import re


with open("input.txt") as f:
    input_lines = f.read().strip().split("\n")

hand_pattern = r"^([AKQJT2-9]{5}) (\d+)$"
card_map = "AKQT98765432J"

JOKER = card_map.index("J")

def get_hand_type(hand: tuple[int]):
    counts = {}

    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
    
    counts_sorted = sorted((value for key, value in counts.items() if key != JOKER), reverse=True)

    counts_sorted += [0, 0]

    jokers = counts[JOKER] if JOKER in counts else 0

    if counts_sorted[0] + jokers == 5:
        return 0 # Five of a kind
    if counts_sorted[0] + jokers == 4:
        return 1 # Four of a kind
    if counts_sorted[0] + counts_sorted[1] + jokers == 5:
        return 2 # Full house
    if counts_sorted[0] + jokers == 3:
        return 3 # Three of a kind
    if counts_sorted[0] + counts_sorted[1] + jokers == 4:
        return 4 # Two pair
    if counts_sorted[0] + jokers == 2:
        return 5 # One pair
    
    return 6 # High card

hands = []

for line in input_lines:
    hand_match = re.match(hand_pattern, line)
    cards = tuple(map(card_map.index, hand_match.group(1)))
    bid = int(hand_match.group(2))

    hand_type = get_hand_type(cards)

    hands.append(((hand_type, cards), bid))

hands.sort()
# It doesn't matter that it also sorts the bid,
# because as long as all the hands are distinct (which they should be)
# it will never determine order based on the bid

total_winnings = 0

for i, (hand, bid) in enumerate(hands):
    rank = len(hands) - i
    total_winnings += bid * rank

print(total_winnings)