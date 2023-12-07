from enum import Enum

HAND_SIZE = 5


# class Hand:
#     class HandType(Enum):
#         HIGH_CARD = 1
#         ONE_PAIR = 2
#         TWO_PAIR = 3
#         THREE_OF_A_KIND = 4
#         FULL_HOUSE = 5
#         FOUR_OF_A_KIND = 6
#         FIVE_OF_A_KIND = 7
#
#     def __int__(self, cards):
#         self.cards = cards
#         self.hand_type = Hand.determine_hand_type(self.cards)
#
#     def __gt__(self, other):
#         return compare_strengths(self, other) == self
#
#     def __lt__(self, other):
#         return compare_strengths(self, other) == other
#
#     # def __eq__(self, other):
#
#     def hand_type_value(self):
#         match self.hand_type:
#             case HandType.FIVE_OF_A_KIND:
#                 return 7
#             case HandType.FOUR_OF_A_KIND:
#                 return 6
#             case HandType.FULL_HOUSE:
#                 return 5
#             case HandType.THREE_OF_A_KIND:
#                 return 4
#             case HandType.TWO_PAIR:
#                 return 3
#             case HandType.ONE_PAIR:
#                 return 2
#             case HandType.HIGH_CARD:
#                 return 1
#             case _:
#                 print("invalid hand type")
#                 return 0

class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def hand_type_value(hand_type):
    match hand_type:
        case HandType.FIVE_OF_A_KIND:
            return 7
        case HandType.FOUR_OF_A_KIND:
            return 6
        case HandType.FULL_HOUSE:
            return 5
        case HandType.THREE_OF_A_KIND:
            return 4
        case HandType.TWO_PAIR:
            return 3
        case HandType.ONE_PAIR:
            return 2
        case HandType.HIGH_CARD:
            return 1
        case _:
            print("invalid hand type")
            return 0


def determine_hand_type(hand):
    cards, _ = hand
    card_counts = [cards.count(c) for c in cards]
    if max(card_counts) == 5:
        return HandType.FIVE_OF_A_KIND
    elif max(card_counts) == 4:
        return HandType.FOUR_OF_A_KIND
    elif card_counts.count(2) == 2 and card_counts.count(3) == 3:
        return HandType.FULL_HOUSE
    elif max(card_counts) == 3:
        return HandType.THREE_OF_A_KIND
    elif card_counts.count(2) == 4:
        return HandType.TWO_PAIR
    elif card_counts.count(2) == 2:
        return HandType.ONE_PAIR
    else:
        return HandType.HIGH_CARD


def determine_hand_type_part2(hand):
    cards, bet = hand
    no_of_jokers = cards.count('J')
    if no_of_jokers == 5:
        return HandType.FIVE_OF_A_KIND
    if no_of_jokers == 0:
        return determine_hand_type(hand)
    cards_less = [c for c in cards if c != 'J']
    if no_of_jokers == 4:
        return HandType.FIVE_OF_A_KIND
    if no_of_jokers == 3:
        if len(set(cards_less)) == 1:
            return HandType.FIVE_OF_A_KIND
        elif len(set(cards_less)) == 2:
            return HandType.FOUR_OF_A_KIND
        else:
            print("Something mysterious for case 3 jokers")
            raise ValueError
    if no_of_jokers == 1:
        match determine_hand_type((cards_less, bet)):
            case HandType.FOUR_OF_A_KIND:
                return HandType.FIVE_OF_A_KIND
            case HandType.THREE_OF_A_KIND:
                return HandType.FOUR_OF_A_KIND
            case HandType.TWO_PAIR:
                return HandType.FULL_HOUSE
            case  HandType.ONE_PAIR:
                return HandType.THREE_OF_A_KIND
            case HandType.HIGH_CARD:
                return HandType.ONE_PAIR
            case _ :
                print("no handtype for lessened hand")
                raise ValueError
    if no_of_jokers == 2:
        match determine_hand_type((cards_less, bet)):
            case HandType.THREE_OF_A_KIND:
                return HandType.FIVE_OF_A_KIND
            case HandType.ONE_PAIR:
                return HandType.FOUR_OF_A_KIND
            case HandType.HIGH_CARD:
                return HandType.THREE_OF_A_KIND
    raise Exception("something wrong in determine_hand_type_part2")




def card_value(card):
    allowed_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    if card not in allowed_cards:
        print("Card not allowed >:[")
        return None
    match card:
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 1
        case 'T':
            return 10
        case _:
            return int(card)


def parse_hand(line: str):
    cards_string, bet_string = line.strip().split(' ')
    cards = [c for c in cards_string]
    bet = int(bet_string)
    return cards, bet


def high_card_value(hand):
    cards, _ = hand
    # cards = sorted(cards, key=lambda c: card_value(c))
    cards = list(reversed(cards))
    value = 0
    for i in range(HAND_SIZE):
        card = cards[i]
        value += card_value(card) * 14 ** i
    # print(hand, value)
    return value


def total_hand_value(hand):
    hand_type = determine_hand_type_part2(hand)
    value = hand_type_value(hand_type) * 14**5
    value += high_card_value(hand)
    return value


def sort_hands(hands: list):
    return sorted(hands, key=lambda tpl: total_hand_value(tpl))


def read_input(filename: str) -> list:
    hands = []
    with open(filename, 'r') as inp:
        for line in inp:
            cards, bet = parse_hand(line)
            hands.append((cards, bet))
    return hands


def main():
    hands = read_input("input7.txt")
    print(len(hands))
    # print(len(set(hands)))
    # print(hands)
    hands = sort_hands(hands)
    total_winnings = 0
    for i, (_, bet) in enumerate(hands):
        total_winnings += (i+1)*bet
    print(total_winnings)
    return total_winnings


if __name__ == "__main__":
    main()
