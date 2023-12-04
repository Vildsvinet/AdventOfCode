content_dict = {}
cardlist = []

with open("input4.txt", 'r') as inp:
    tot_sum = 0
    data = inp.readlines()

    for i in range(len(data)):
        line = data[i].strip()                  # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        s1 = line.split(':')                    # ['Card 1', ' 41 48 83 86 17 | 83 86  6 31 17  9 48 53']
        card_nr = s1[0].split(' ')[-1]          # 1
        numbers = s1[1].split('|')              # [' 41 48 83 86 17 ', ' 83 86  6 31 17  9 48 53']
        # print("numbers: ", numbers)
        winning = set(numbers[0].split(' '))
        possessed = set(numbers[1].split(' '))
        winning.remove('')                      # {'86', '17', '48', '83', '41'}
        possessed.remove('')                    # {'48', '53', '31', '83', '6', '17', '9', '86'}
        joint = possessed.intersection(winning) # {'86', '83', '48', '17'}
        content_dict[card_nr] = len(joint)      # {'1': 4}
        cardlist.append((int(card_nr), len(joint)))

        if len(joint) != 0:
            # print(joint)
            tot_sum += 2 ** (len(joint) - 1)
#     print(tot_sum)

# print(cardlist)     # [(1, 4), (2, 2), (3, 2), (4, 1), (5, 0), (6, 0)]

def calculate_scratchcards(card: tuple, cardlist: list):
    card_nr, no_of_matches = card
    no_of_cards = 1
    for i in range(card_nr, card_nr + no_of_matches):
        if card_nr == len(cardlist):
            return no_of_cards
        no_of_cards += calculate_scratchcards(cardlist[i], cardlist)
    return no_of_cards

def main():
    tot = 0
    for c in cardlist:
        tot += calculate_scratchcards(c, cardlist)
    return tot

print(main())
