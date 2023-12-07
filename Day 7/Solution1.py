import re


with open("input.txt") as f:
    input_lines = f.read().strip().split("\n")

hand_pattern = r"^([AKQJT2-9]{5}) (\d+)$"
card_map = "AKQJT98765432"

def get_hand_type(hand: tuple[int]):
    counts = {}

    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
    
    counts_sorted = sorted(counts.values(), reverse=True)

    if counts_sorted[0] == 5:
        return 0 # Five of a kind
    if counts_sorted[0] == 4:
        return 1 # Four of a kind
    if counts_sorted[0] == 3 and counts_sorted[1] == 2:
        return 2 # Full house
    if counts_sorted[0] == 3: # (and not full house)
        return 3 # Three of a kind
    if counts_sorted[0] == 2 and counts_sorted[1] == 2:
        return 4 # Two pair
    if counts_sorted[0] == 2: # (and not two pair)
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