import pytest
import l7

hand_list = l7.read_input("../input7.txt")


def test_hand_determination():
    assert l7.determine_hand_type((['A', 'A', 'A', 'K', 'K'], 1)) == l7.HandType.FULL_HOUSE
    assert l7.determine_hand_type((['A', 'A', 'A', 'A', 'K'], 1)) == l7.HandType.FOUR_OF_A_KIND
    assert l7.determine_hand_type((['A', 'A', 'A', 'K', 'Q'], 1)) == l7.HandType.THREE_OF_A_KIND
    assert l7.determine_hand_type((['A', 'A', 'K', 'K', 'Q'], 1)) == l7.HandType.TWO_PAIR
    assert l7.determine_hand_type((['A', 'A', 'K', 'Q', 'J'], 1)) == l7.HandType.ONE_PAIR
    assert l7.determine_hand_type((['A', 'K', 'Q', 'J', 'T'], 1)) == l7.HandType.HIGH_CARD
    assert l7.determine_hand_type((['A', 'A', 'A', 'A', 'A'], 1)) == l7.HandType.FIVE_OF_A_KIND
    assert l7.determine_hand_type((['6', '2', '3', '4', '5'], 1)) == l7.HandType.HIGH_CARD
    assert l7.determine_hand_type((['2', 'T', '3', '4', '5'], 1)) == l7.HandType.HIGH_CARD
    assert l7.determine_hand_type((['K', 'K', '4', 'J', '4'], 1)) == l7.HandType.TWO_PAIR
    assert l7.determine_hand_type((['J', 'J', 'J', 'J', 'J'], 1)) == l7.HandType.FIVE_OF_A_KIND


def test_total_hand_value():
    numericals = []
    for h in hand_list:
        numericals.append(l7.total_hand_value(h))
    assert len(set(numericals)) == len(hand_list)
